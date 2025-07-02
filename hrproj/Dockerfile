# Use official Python image
FROM python:3.11-slim

# Prevent Python buffering (so logs show up in real time)
ENV PYTHONUNBUFFERED=1

# Create & set working directory
WORKDIR /code

# Install pip dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project code
COPY . .

# Default command: run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:60511"]
