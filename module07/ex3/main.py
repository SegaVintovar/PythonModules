from ex3 import FantasyCardFactory, GameEngine, AggressiveStrategy

def main() -> None:
    factory = FantasyCardFactory("test")
    new_creature = factory.create_creature()
    deck = factory.create_themed_deck(6)
    enemy = factory.create_themed_deck(2)
    # print(deck["creature_cards"], deck["spell_cards"], deck["artifacts"])
    # print(new_creature.name)
    strategy = AggressiveStrategy()
    # print(strategy.execute_turn(deck["creature_cards"], enemy["creature_cards"]))
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    engine.simulate_turn()

if __name__ == "__main__":
    main()