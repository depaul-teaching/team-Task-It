FROM python:3.12-slim

# Keep Python output unbuffered and avoid .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Install dependencies before copying application code for fast rebuilds
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code and templates with non-root ownership
COPY --chown=appuser:appgroup . .

# Switch to non-root user before starting the container
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]