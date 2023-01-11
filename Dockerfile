FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run manage.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

