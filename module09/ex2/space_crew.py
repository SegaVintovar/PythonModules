from enum import Enum
from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
# from .generated_data import SPACE_MISSIONS


mission1 = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'captain',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'cadet',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }

mission2 = {
        'mission_id': 'M2024_TITAN',
        'mission_name': 'Solar Observatory Research Mission',
        'destination': 'Solar Observatory',
        'launch_date': '2024-03-30T00:00:00',
        'duration_days': 451,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Williams',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Mission Command',
                'years_experience': 19,
                'is_active': True
            },
            {
                'member_id': 'CM002',
                'name': 'James Hernandez',
                'rank': 'cadet',
                'age': 43,
                'specialization': 'Pilot',
                'years_experience': 30,
                'is_active': True
            },
            {
                'member_id': 'CM003',
                'name': 'Anna Jones',
                'rank': 'cadet',
                'age': 35,
                'specialization': 'Communications',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM004',
                'name': 'David Smith',
                'rank': 'cadet',
                'age': 27,
                'specialization': 'Security',
                'years_experience': 15,
                'is_active': True
            },
            {
                'member_id': 'CM005',
                'name': 'Maria Jones',
                'rank': 'cadet',
                'age': 55,
                'specialization': 'Research',
                'years_experience': 30,
                'is_active': True
            }
        ],
        'mission_status': 'planned',
        'budget_millions': 2208.1
    }

# if nested validation fails, your parent model validator may not run,
# because model creation stops at validation errors first.


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(max_length=12, min_length=1)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    # any() is a built-in Python function.
    # It returns True if at least one item in an iterable is truthy,
    # otherwise False.
    @model_validator(mode="after")
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID has to start with 'M'")
        has_commander = any(
            member for member in self.crew if member.rank == Rank.commander
            )
        has_captain = any(
            member for member in self.crew if member.rank == Rank.captain
            )
        if has_captain is False and has_commander is False:
            raise ValueError(
                "Crew must contain at least one Captain or Cammander"
                )
        # if (CrewMember.rank.commander not in self.crew or
        #         CrewMember.captain not in self.crew):
        #     raise ValueError(
        #         "Crew must contain at least one Captain or Cammander"
        #         )
        total = len(self.crew)
        if self.duration_days > 365:
            experienced_members = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_members += 1
            if experienced_members / total < 0.5:
                raise ValueError(
                   ("Long missions (> 365 days)" +
                    " need 50% experienced crew (5+ years)")
                )
        active = 0
        for member in self.crew:
            if member.is_active:
                active += 1
        if active != total:
            raise ValueError(
                "All crew members must be active"
            )
        return self


def main() -> None:
    sp_1 = SpaceMission(**mission1)
    print("Space Mission Crew Validation")
    print("========================================")
    print("Valid mission created:")
    print("Mission:", sp_1.mission_name)
    print("ID:", sp_1.mission_id)
    print("Destination:", sp_1.destination)
    print("Budget:", f"${sp_1.budget_millions}M")
    print("Crew size:", len(sp_1.crew))
    print("Crew members:")
    for member in sp_1.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        sp_2 = SpaceMission(**mission2)
    except ValidationError as e:
        print(str(e.errors()[0]["msg"]))
    else:
        print("Mission:", sp_2.mission_name)


if __name__ == "__main__":
    main()
