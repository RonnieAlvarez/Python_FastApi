from pydantic import BaseModel
from typing import List


class Skill(BaseModel):
    name:str
    years:int
