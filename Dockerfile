
FROM python:3.11-slim

# Install system libraries required by OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /app

# Configure Python and application port
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8181

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into the container
COPY . .

# Expose the Flask application port
EXPOSE 8181

# Start the SafeStridee server
CMD ["python", "server.py"]
