# Random float generator

The backend API for random float generator.


## Introduction
The backend API supports user management and authentication along with random float generation.The application is currently developed and tested
on python 3.8.

Features

* User management and authentication using jwt tokens
* Random float generation

A full list of supported api endpoints can be found at /swagger-ui#/ on the server

## Usage

* [Quick start](#quick-start)
* [Setup](#setup)
* [Documentation](#documentation)

### Quick start
For Quick start on API use docker. Run
```
docker compose
```

This should spin up docker container for a quick look at http://localhost:5000.

### Setup

#### Install dependencies
For dev dependencies including pytest use.
```
   pip install -r requirements_dev.txt
```
For production run
    ```
    pip install -r requirements.txt
    ```

#### Update environment
    The environment variables used by the application along with development values can be found at .flaskenv file
        Modify the values to match the environment. The application currently uses sqlite for basic testing. Postgres or other
        more robust db should be used for further development or in production

#### Install backend api application
    Install the backend api package by
```
    pip install .
```

#### Migrate schema
    The database migrations for user and token management are added to the repo.
    Upgrade database schema by
    
```
    flask db upgrade
```

#### Test
    Pytest is used to write tests for the application.
    Run tests by

```
    pytest .
```

#### Initialise test user
    Initialise test user by
```
    flask init
```
    This creates an admin user with
        username: admin
        password: admin
        email: jithintom1@gmail.com

#### Start development server
    Run development server by
    
```
    flask run -h 0.0.0.0
```

    The server should now be running at http://localhost:5000

### Documentation
    The API uses swagger apispec to generate swagger documentation
    Documentation for supported API endpoints can be found at http://localhost:5000/swagger-ui#/

    Also a hosted version of key API endpoints can be found at https://documenter.getpostman.com/view/2804988/2s9Y5YRNFd

### Entry point to the API
    https://github.com/jithintomz/random-float-generator/blob/master/core/api/views.py

### Core API
    https://github.com/jithintomz/random-float-generator/blob/master/core/api/resources/random_generator.py
