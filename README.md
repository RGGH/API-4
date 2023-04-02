# API-4

### Using FastAPI with spaCy to identify entities

clone repo

install requirements and the spaCy 'en_core_web_sm' file

`# python3 -m spacy download en_core_web_sm`

run

`❯ uvicorn main:app --reload`

open ents.html on localhost "http://127.0.0.1:8000/ents/html"

### ~~Deploy to Google Cloud~~

`docker pull rggh/spacy_ner:v1`
`<br>`
`<br>`
![spacy-ml](https://github.com/RGGH/API-4/blob/main/api-spaCy.png)
