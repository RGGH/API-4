FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL author="redandgreen"

ENV LANG             en_core_web_sm
ENV SPACY_VERSION    3.2.1

COPY . /app
ENV APP_HOME /app

WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

# spacy
RUN \
    pip3 install -U spacy==${SPACY_VERSION} \
    && python3 -m spacy download en

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
