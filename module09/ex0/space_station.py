from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime
import inspect


# @field_validator, @model_validator
class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=1, lt=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200)

    # @model_validator
    # def check_station():
    #     ...

def main() -> None:
    istation = {
        "station_id": "123",
        "name": "ABC",
        "crew_size": 5,
        "power_level": 3,
        "oxygen_level": 2,
        "last_maintenance": datetime(2000, 3, 20),
        "is_operational": True,
        "notes": None
    }
    print(inspect.getmembers(SpaceStation(**istation)))
    

main()