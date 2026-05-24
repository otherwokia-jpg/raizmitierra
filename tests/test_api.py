"""
Tests for raizmitierra_server.py Flask application.

These tests use the Flask test client (no real HTTP server needed).
"""

import json


class TestHealth:
    """GET /health → 200 JSON with status ok"""

    def test_health_returns_200(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200

    def test_health_returns_json(self, client):
        resp = client.get("/health")
        assert resp.is_json

    def test_health_has_status_ok(self, client):
        resp = client.get("/health")
        data = resp.get_json()
        assert data["status"] == "ok"

    def test_health_has_port(self, client):
        resp = client.get("/health")
        data = resp.get_json()
        assert data["port"] == 9500

    def test_health_has_portal_key(self, client):
        resp = client.get("/health")
        data = resp.get_json()
        assert data["portal"] == "raizmitierra"


class TestIndex:
    """GET / → 200 (public page, serves index.html)"""

    def test_index_returns_200(self, client):
        resp = client.get("/")
        assert resp.status_code == 200

    def test_index_is_html(self, client):
        resp = client.get("/")
        assert resp.mimetype == "text/html"


class TestAdminDashboard:
    """GET /admin/ → 302 redirect to login (no auth session)"""

    def test_admin_redirects_without_auth(self, client):
        resp = client.get("/admin/")
        assert resp.status_code == 302

    def test_admin_redirects_to_login_url(self, client):
        resp = client.get("/admin/")
        assert resp.status_code == 302
        # Should redirect to the external login page
        location = resp.headers.get("Location", "")
        assert "login" in location.lower()

    def test_admin_redirect_location_contains_next(self, client):
        resp = client.get("/admin/")
        location = resp.headers.get("Location", "")
        assert "next=" in location

    def test_admin_with_auth_returns_200(self, app, client):
        """When a valid session exists, /admin/ should render the dashboard."""
        with client.session_transaction() as sess:
            sess["authenticated"] = True
            sess["role"] = "admin"
            sess["username"] = "testadmin"
            sess["full_name"] = "Test Admin"

        resp = client.get("/admin/")
        assert resp.status_code == 200


class TestLogin:
    """GET /login → 302 (redirects to external SSO login)"""

    def test_login_redirects(self, client):
        resp = client.get("/login")
        assert resp.status_code == 302

    def test_login_redirects_to_external_login(self, client):
        resp = client.get("/login")
        location = resp.headers.get("Location", "")
        assert "login" in location.lower()


class TestSSOLogin:
    """GET /sso_login → redirect behavior"""

    def test_sso_login_redirects_without_token(self, client):
        """Without an sso_token, /sso_login redirects to external login."""
        resp = client.get("/sso_login")
        assert resp.status_code == 302
        location = resp.headers.get("Location", "")
        assert "login" in location.lower()

    def test_sso_login_with_token(self, client, monkeypatch):
        """With an sso_token, it processes the token and redirects to /admin/."""
        # We need a valid JWT token for this test.
        # Since get_sso_secret() reads a file, monkeypatch it.
        import jwt
        import raizmitierra_server as server

        secret = "test-sso-secret-for-pytest"

        # Monkeypatch get_sso_secret to return our test secret
        monkeypatch.setattr(server, "get_sso_secret", lambda: secret)

        # Create a valid token
        payload = {
            "username": "pytest_user",
            "full_name": "PyTest User",
            "email": "pytest@test.local",
            "role": "admin",
            "allowed_portals": ["raizmitierra"],
        }
        token = jwt.encode(payload, secret, algorithm="HS256")

        resp = client.get(f"/sso_login?sso_token={token}")
        # After processing token, it redirects to /admin/ (or next param)
        assert resp.status_code == 302


class TestAdminStatus:
    """GET /api/admin-status without session → JSON with is_admin: false"""

    def test_admin_status_returns_json(self, client):
        resp = client.get("/api/admin-status")
        assert resp.is_json

    def test_admin_status_no_session_is_not_admin(self, client):
        resp = client.get("/api/admin-status")
        data = resp.get_json()
        # session.get("authenticated") returns None (→ null in JSON)
        # because the expression `None and role_check` short-circuits to None
        assert data["is_admin"] is None or data["is_admin"] is False

    def test_admin_status_has_username_empty(self, client):
        resp = client.get("/api/admin-status")
        data = resp.get_json()
        assert data["username"] == ""

    def test_admin_status_has_full_name_empty(self, client):
        resp = client.get("/api/admin-status")
        data = resp.get_json()
        assert data["full_name"] == ""

    def test_admin_status_with_session_is_admin(self, client):
        """With a valid admin session, is_admin should be true."""
        with client.session_transaction() as sess:
            sess["authenticated"] = True
            sess["role"] = "admin"
            sess["username"] = "testadmin"
            sess["full_name"] = "Test Admin"

        resp = client.get("/api/admin-status")
        data = resp.get_json()
        assert data["is_admin"] is True
        assert data["username"] == "testadmin"
        assert data["full_name"] == "Test Admin"

    def test_admin_status_viewer_is_not_admin(self, client):
        """A session with role='viewer' should not count as admin."""
        with client.session_transaction() as sess:
            sess["authenticated"] = True
            sess["role"] = "viewer"
            sess["username"] = "viewer_user"

        resp = client.get("/api/admin-status")
        data = resp.get_json()
        assert data["is_admin"] is False
