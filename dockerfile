FROM python:3.12.2-slim as base

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set environment variables
ENV FLASK_APP=app.run:create_app()
ENV FLASK_ENV=development

# Expose port 5004
EXPOSE 5004

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
