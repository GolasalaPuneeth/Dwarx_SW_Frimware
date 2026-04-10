FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better caching)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev

COPY req.txt .
# COPY . .
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the code
COPY . .

# Expose FastAPI port
EXPOSE 3000

# Command to run with live reload enabled
CMD ["python","-m","main"]