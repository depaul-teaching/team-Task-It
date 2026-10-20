# =============================================================================
# STARTER Dockerfile for order-service  (IT 390, Week 2)
#
# This Dockerfile BUILDS and RUNS, but it has several problems we covered in
# lecture. Your job is to rewrite it into a clean Dockerfile that fixes them.
#
# Rename your finished version to just "Dockerfile" (no extension) so that
# `docker build` picks it up automatically.
#
# Do NOT submit this file unchanged. See the handout for the full rubric.
# =============================================================================

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir  -r requirements.txt

COPY . .

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app"]

CMD ["--host", "0.0.0.0", "--port", "8000"]
