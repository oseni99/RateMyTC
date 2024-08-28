# Use the specified Python version as the base image
ARG PYTHON_VERSION=3.12-bullseye
FROM python:${PYTHON_VERSION} as python

# STAGE 1: Build dependencies wheels
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local 

# Install build dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

# Copy the requirements file from the host machine to the Docker container
COPY ./requirements .

# Create the dependencies wheels
RUN pip wheel --wheel-dir /usr/src/app/wheels -r ${BUILD_ENVIRONMENT}.txt

# STAGE 2: Run our app
FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local 

# Set the working directory inside the container
ARG APP_HOME=/app  
WORKDIR ${APP_HOME}

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

# Install runtime dependencies
RUN apt-get update --fix-missing && apt-get install --no-install-recommends -y \ 
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy the wheels from the build stage to the current stage
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Install the dependencies using the wheels
RUN find /wheels -name "*.whl" -exec pip install --no-cache-dir --no-index --find-links=/wheels {} + \
    && rm -rf /wheels/

# Set up the entrypoint and start script
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i "s/\r$//g" /entrypoint && chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i "s/\r$//g" /start && chmod +x /start

# Copy the application code to the container
COPY . ${APP_HOME}

# Specify the default command to run
ENTRYPOINT ["/entrypoint"]
