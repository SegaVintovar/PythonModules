from ex3 import FantasyCardFactory, GameEngine, AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory("FantasyCardFactory")
    engine = GameEngine()
    strategy = AggressiveStrategy()
    print("Factory: ", factory.name)
    print("Strategy: ", strategy.get_strategy_name())
    print("Avaliable types: ", factory.get_supported_types())
    engine.configure_engine(factory, strategy)
    engine.simulate_turn()
    print("\nGame report:")
    print(engine.get_engine_status())
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )


if __name__ == "__main__":
    main()
