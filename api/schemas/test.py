from pydantic import BaseModel
from api.schemas.answer import AnswerBaseModel

class TestBaseModel(BaseModel):
    id : int
    text : str
    answer : list[AnswerBaseModel]
    is_many_answer : bool

    class Config:
        orm_mode = True

