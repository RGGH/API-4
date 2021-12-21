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
    res_org = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "ORG"
    ]
    res_fac = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "FACILITY"
    ]
    res_per = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "PERSON"
    ]
    res_mon = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "MONEY"
    ]
    res_qua = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "QUANTITY"
    ]
    res_woa = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "WORK_OF_ART"
    ]
    res_ord = [
        (token_ent.text) for token_ent in mytk.ents if token_ent.label_ == "ORDINAL"
    ]

    

    return {"date": res_date, 
            "country": res_country, 
            "organization":res_org,
            "facility":res_fac, 
            "people":res_per, 
            "money":res_mon, 
            "weight_distance":res_qua,
            "work_of_art":res_woa,
            "ordinal":res_ord
    }


# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
