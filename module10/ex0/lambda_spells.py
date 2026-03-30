def mages_and_artifacts() -> tuple:
    return (
        [
            {'name': 'Rowan', 'power': 67, 'element': 'earth'},
            {'name': 'Sage', 'power': 92, 'element': 'fire'},
            {'name': 'Zara', 'power': 66, 'element': 'fire'},
            {'name': 'Nova', 'power': 88, 'element': 'shadow'},
            {'name': 'Ember', 'power': 88, 'element': 'water'}
        ],
        [
            {'name': 'Ice Wand', 'power': 81, 'type': 'weapon'},
            {'name': 'Water Chalice', 'power': 97, 'type': 'relic'},
            {'name': 'Shadow Blade', 'power': 91, 'type': 'weapon'},
            {'name': 'Earth Shield', 'power': 104, 'type': 'weapon'}
        ]
    )


# sorted() vs .sort()
# Function	What it does
# sorted(list)	Returns a new sorted list
# list.sort()	Sorts the original list
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    # artifacts.sort(key=lambda x: x["power"])
    # return artifacts
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


# map() → change values
# filter() → remove values
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "*" + x + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    if len(mages) > 0:
        return {
            "max_power": max(mages, key=lambda x: x["power"])["power"],
            "min_power": min(mages, key=lambda x: x["power"])["power"],
            "avg_power": round(
                sum(map(lambda x: x["power"], mages)) / len(mages), 2)
        }


def main() -> None:
    print("Testing lambda_spells.py\n")
    mages, artifacts = mages_and_artifacts()
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        "The most powerfull arifact is: ",
        sorted_artifacts[0]["name"], "-",
        sorted_artifacts[0]["power"],
        "power"
        "\n"
        )
    filtered = power_filter(mages, 90)
    print("Filterd mages by min power of 90: ", filtered, "\n")
    spells = ['meteor', 'tsunami', 'blizzard', 'freeze']
    new_spells = spell_transformer(spells)
    print("Transformed spells: ", new_spells, "\n")
    stats = mage_stats(mages)
    print("Mages stats: ", stats)
    print()


if __name__ == "__main__":
    main()
