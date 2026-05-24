"""
pytest configuration for raizmitierra Flask app tests.
Provides a `client` fixture backed by Flask's test_client.
"""

import os
import sys
from pathlib import Path

import pytest

# Ensure the project root is on sys.path so we can import the app module
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def app():
    """Create the Flask application configured for testing."""
    # Minimal env vars that the app needs (load_dotenv reads .env if present)
    os.environ.setdefault("RAIZ_SECRET", "test-secret-key-for-pytest")

    from raizmitierra_server import app as flask_app

    flask_app.config.update(
        TESTING=True,
        # Use a simple filesystem-based session backend so sessions work in tests
        SESSION_COOKIE_NAME="session_raiz_test",
    )

    # Override the PrefixMiddleware to be a no-op during tests
    # (the real one rewrites Location headers which can confuse assertions)
    original_wsgi = flask_app.wsgi_app
    # Unwrap PrefixMiddleware to get the raw app
    if hasattr(original_wsgi, "__closure__") or hasattr(original_wsgi, "app"):
        # Try to get the inner app from PrefixMiddleware
        inner = getattr(original_wsgi, "app", original_wsgi)
        flask_app.wsgi_app = inner

    yield flask_app


@pytest.fixture
def client(app):
    """Flask test client — no auth session by default."""
    return app.test_client()
