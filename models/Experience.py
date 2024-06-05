from pydantic import BaseModel
from typing import List


class Experience(BaseModel):
    title:str
    location:str
    start_date:str
    end_date:str
    organization:str
