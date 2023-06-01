from pydantic import BaseModel

class AnswerBaseModel(BaseModel):
    id : int
    num : int
    text : str
    class Config:
        orm_mode = True
