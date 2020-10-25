# Base image
FROM python:3.6

# Install pipenv
RUN pip install pipenv

# Set working directory
WORKDIR /api/

# Copy Pipfile and Pipfile.lock to container
COPY Pipfile /api/
COPY Pipfile.lock /api/
COPY server.py /api

# Install pipenv dependencies
RUN pipenv install

# Expose port for api
EXPOSE 5000

# Add flask app entrypoint to ENV
#ENV FLASK_APP=api/api.py
#ENV FLASK_ENV=development

ENV FLASK_APP=server.py
#ENV FLASK_ENV=development

# Default command
CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
#CMD ["python", "-m", "api.py"]