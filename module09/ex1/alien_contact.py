from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
# from typing import Optional


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(max_length=15, min_legth=5)
    timestamp: datetime
    location: str = Field(max_length=100, min_legth=3)
    contact_type: ContactType
    signal_stregth: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: (str | None) = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_contact(self) -> AlienContact:
        if self.contact_id[:2] != "AC":
            raise ValidationError(
                "ValidationError:",
                "Contact ID must start with 'AC' (Alien Contact)"
                )
        if self.contact_type == "physical":
            if self.is_verified is False:
                raise ValidationError(
                    "ValidationError:",
                    "Physical contact reports must be verified"
                )
        if self.contact_type == "telepathic":
            if self.witness_count < 3:
                raise ValidationError(
                    "ValidationError:",
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_stregth > 7.0:
            if self.message_received is None:
                raise ValidationError(
                    "ValidationError",
                    "Strong signals (> 7.0) should include received messages"
                )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    contact_report = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime(2000, 4, 1),
        "location": "Codam",
        "contact_type": "radio",
        "signal_stregth": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }
    valid = AlienContact(**contact_report)
    print("Valid contact report:")
    print(f"")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")