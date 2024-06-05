from pydantic import BaseModel
from typing import List


class Language(BaseModel):
    name:str
    level:str
