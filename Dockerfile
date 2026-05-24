# ── RaízMiTierra CMS — Dockerfile ──
FROM python:3.11-slim

WORKDIR /app

# Install system deps needed by Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    libjpeg62-turbo-dev libwebp-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Fix ownership so nobody user can write to data files
RUN chown -R nobody:nogroup /app/database/

# Run as non-root user for security
USER nobody

# Expose portal port
EXPOSE 9500

# Run with Gunicorn (production)
CMD ["gunicorn", "raizmitierra_server:app", "--bind", "0.0.0.0:9500", "--workers", "2", "--timeout", "120"]