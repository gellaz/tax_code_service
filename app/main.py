from datetime import date

from codicefiscale import codicefiscale
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Person(BaseModel):
    surname: str
    name: str
    sex: str
    birthdate: str
    birthplace: str


app = FastAPI()


@app.get("/")
def root():
    return "Hello World"


@app.get("/api/{tax_code}")
def get_person_from_tax_code(tax_code: str):
    try:
        res_dict = codicefiscale.decode(tax_code)
    except ValueError as e:
        return str(e)

    ret_value = {
        "first_name": res_dict['raw']['name'],
        "las    t_name": res_dict['raw']['surname'],
        "birthdate": res_dict['birthdate'].strftime("%d/%m/%Y"),
        "sex": res_dict['sex'],
        "birthplace": f"{res_dict['birthplace']['name']} ({res_dict['birthplace']['province']})",
    }

    return ret_value


@app.post("/api/")
def get_tax_code_from_person(person: Person):
    try:
        ret_value = codicefiscale.encode(
            surname=person.surname,
            name=person.name,
            sex=person.sex,
            birthdate=person.birthdate,
            birthplace=person.birthplace)
    except ValueError as e:
        return str(e)

    return ret_value
