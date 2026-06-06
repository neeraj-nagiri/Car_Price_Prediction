from pydantic import BaseModel

class CarData(BaseModel):

    name: str
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    year: int
    km_driven: int
    seats: int
    Mileage: float
    Engine_CC: float
    max_power_bph: float
    Mileage_Unit: str