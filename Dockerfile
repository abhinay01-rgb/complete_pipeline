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

# Pull model file using DVC
RUN dvc pull

# Ensure correct permissions for DVC and model
RUN chmod -R 755 /app/models

# Configure Git inside Docker for DVC remote storage (if needed)
RUN git config --global user.email "your-email@example.com" && \
    git config --global user.name "Your Name"

# Set a non-root user for better security
USER nobody

# Expose Flask port (default: 5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/app.py"]
