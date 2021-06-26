from codicefiscale import codicefiscale
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class Person(BaseModel):
    surname: str
    name: str
    sex: str
    birthdate: str
    birthplace: str


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/api/{tax_code}")
def get_person_from_tax_code(tax_code: str):
    try:
        res_dict = codicefiscale.decode(tax_code)
    except ValueError as e:
        return str(e)

    ret_value = {
        "first_name": res_dict['raw']['name'],
        "last_name": res_dict['raw']['surname'],
        "birthdate": res_dict['birthdate'].strftime("%d/%m/%Y"),
        "sex": res_dict['sex'],
        "birthplace": f"{res_dict['birthplace']['name']} ({res_dict['birthplace']['province']})",
    }

    return ret_value


@app.post("/api/dd")
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
