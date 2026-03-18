from pydantic import BaseModel, constr

class SectorRequest(BaseModel):
    sector: constr(min_length=3, max_length=50)