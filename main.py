""" ML Example for spaCy Ents - API-4
    "Processing raw text intelligently is difficult"
    Author : redandgreen
    version 1.0
"""
import uvicorn
import spacy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

output = {}

origins = ["http://redandgreen.co.uk"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class request_body(BaseModel):
    features: str


@app.post("/ents")
def vars(data: request_body) -> dict:
    """Gets the DATE from features (input paragraph)
    use POST to allow >=255 chars
    """
    mytk = nlp(data.features)
    res_date = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "DATE"
    ]
    res_country = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "GPE"
    ]

    return {"date": res_date, "country": res_country}


# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
