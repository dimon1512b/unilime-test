ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}
# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONFAULTHANDLER 1


# FROM base AS python-deps
# RUN apt-get update
# RUN apt-get install -y --no-install-recommends build-essential gcc git

RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

# FROM base as unilime-test
# COPY --from=python-deps /.venv /.venv
# ENV PATH="/.venv/bin:$PATH"
ENV PYTHONPATH=./application
COPY . .
CMD [ "python", "./application/server.py" ]