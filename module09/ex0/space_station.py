from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from datetime import datetime
# import inspect


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
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime(2000, 3, 20),
        "is_operational": True,
        "notes": None
    }

    print("Space Station Data Validation")
    print("========================================")
    our_station = SpaceStation(**istation)
    print("Valid station created:")
    print(f"ID: {our_station.station_id}")
    print(f"Name: {our_station.name}")
    print(f"Crew: {our_station.crew_size} people")
    print(f"Power: {our_station.power_level}%")
    print(f"Oxygen: {our_station.oxygen_level}%")
    if our_station.is_operational is True:
        is_operational = "Operational"
    else:
        is_operational = "Not Operational"
    print(f"Status: {is_operational}")
    print()
    print("========================================")
    bad_station = {
        "station_id": "3i1",
        "name": "ABC",
        "crew_size": "a",
        "power_level": 3,
        "oxygen_level": 2,
        "last_maintenance": datetime(2000, 3, 20),
        "is_operational": True,
        "notes": None
    }
    print("Expected validation error:")
    try:
        their_station = SpaceStation(**bad_station)
        print("Station Name:", their_station.name)
    except ValidationError as e:
        print(str(e))


if __name__ == "__main__":
    main()
