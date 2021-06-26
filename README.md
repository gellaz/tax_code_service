# Tax Code Service
JSON API that allows a client to extrapolate data from a tax code string and viceversa.

There are two ways to run the application:
1. [Running application locally](#running-application-locally)
2. [Running application as a Docker container](#running-application-as-a-docker-container) (the fastest)

## Running application locally

> Prerequisites

* Python 3.7+
* pipenv

> Installing Requirements

To create the virtual environment and install all libraries and packages open the terminal in the root folder of this project (same place where the `Pipfile` is) and type `pipenv install`.

> Launch the application

Once the pipenv environment is installed, enter the app folder and type `uvicorn main:app --host 0.0.0.0 --port 5000` to start the web aplication on port 5000.

The application will be available on `localhost:5000` and the API documentation on `localhost:5000/docs`.

## Running application as a Docker container

> Prerequisites

* Docker

Open the terminal in the root folder of this project and run the following commands:

```
docker build -t tax_code_service .
docker run -d -p 5000:5000 tax_code_service
```