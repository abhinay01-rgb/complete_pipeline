# Use Python 3.11 base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git

# Copy necessary files first (helps with caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Install DVC
RUN pip install --no-cache-dir dvc[all]

# Copy the entire project
COPY . .

# Ensure correct permissions for DVC
RUN chmod -R 777 /app

# Initialize DVC inside the container (if .dvc is missing)
RUN if [ ! -d "/app/.dvc" ]; then dvc init; fi

# Configure Git inside Docker for DVC remote storage (if needed)
RUN git config --global user.email "your-email@example.com" && \
    git config --global user.name "Your Name"

# Set a non-root user (for better security)
USER nobody

# Expose Flask port
EXPOSE 5000

# Run the Flask app instead of DVC pipeline
ENTRYPOINT ["python", "src/app.py"]
