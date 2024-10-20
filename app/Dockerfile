
#FROM python:3.9

#LABEL maintainer="Tuyen Huynh <tuyenhtgcs220307@fpt.edu.vn>"
#LABEL app="Task Service"

#WORKDIR /app

#COPY ./requirements.txt /app/requirements.txt


#RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


#COPY . /app


#CMD ["fastapi", "run", "main.py", "--port", "8000", "--workers", "3"]

# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 to allow external access
EXPOSE 8000

# Command to run the FastAPI app using uvicorn
CMD ["fastapi", "run", "main.py", "--port", "8000", "--workers", "3"]