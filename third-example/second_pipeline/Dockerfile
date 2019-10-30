FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"

COPY ./src/pyproject.toml /deps/
COPY ./src/poetry.lock /deps/
RUN cd /deps && \
    poetry config settings.virtualenvs.create false && \
    poetry install --no-interaction && \
    rm -rf /deps

ENV PYTHONPATH="/src/"

COPY ./src /src
WORKDIR /src

CMD ["python", "data_process.py"]
