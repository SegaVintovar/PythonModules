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
    contact_id: str = Field(max_length=15, min_length=5)
    timestamp: datetime
    location: str = Field(max_length=100, min_length=3)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = False

    # AI suggetsed validation
    # if not self.contact_id.startswith("AC"):
    # raise ValueError("Contact ID must start with 'AC' (Alien Contact)")
    @model_validator(mode='after')
    def validate_contact(self):
        if self.contact_id[:2] != "AC":
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
                )
        if self.contact_type == ContactType.physical:
            if self.is_verified is False:
                raise ValueError(
                    "Physical contact reports must be verified"
                )
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                )
        return self

    def report(self) -> None:
        print(f"ID: {self.contact_id}")
        print("Type:", self.contact_type.value)
        print("Location:", self.location)
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: {self.message_received}\n")


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    contact_report = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime(2000, 4, 1),
        "location": "Codam",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }
    valid = AlienContact(**contact_report)
    print("Valid contact report:")
    valid.report()
    print("======================================")
    print("Expected validation error:")
    invalid_report = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime(2000, 4, 1),
        "location": "Codam",
        "contact_type": "telepathic",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 2,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }
    try:
        invalid = AlienContact(**invalid_report)
    except ValidationError as e:
        # print(str(e.errors()[0]["msg"]))
        print(str(e.errors()[0]["ctx"]["error"]))
    else:
        invalid.report()


if __name__ == "__main__":
    main()
