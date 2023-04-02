# API-4

### Using FastAPI with spaCy to identify entities

clone repo

install requirements and the spaCy 'en_core_web_sm' file

`# python3 -m spacy download en_core_web_sm`

run

`❯ uvicorn main:app --reload`

open ents.html on localhost "http://127.0.0.1:8000/ents/html"

### Docker

`sudo docker pull rggh/spacy_ner:7`<br>
`sudo docker run -it -p 8000:8000 rggh/spacy_ner:7`<br> 

#### check it works :
`http://127.0.0.1:8000/docs#/default/vars_ents_post`

![Spacy](https://github.com/RGGH/API-4/blob/main/api-spaCy.png)
