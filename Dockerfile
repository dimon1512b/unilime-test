ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

ENV PYTHONPATH=./application
COPY . .
CMD [ "python", "./application/server.py" ]