# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose API port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]