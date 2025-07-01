# Use a lightweight official Python image as base
FROM python:3.11-slim

# Set the directory in the container where app code will live
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 5000 (Flask runs on 5000)
EXPOSE 5000

# Start the app when the container launches
CMD ["python", "run.py"]
