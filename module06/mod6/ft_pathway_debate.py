from alchemy.transmutation import lead_to_gold, stone_to_gem
from alchemy.transmutation import philosophers_stone, elixir_of_life
import alchemy.transmutation


# here we see absolute import
# but advanced.py used relative import
# to import modules better to use absolute import, just like here
# relative import is better to use inside the package
def main() -> str:
    print("\n=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py): ")
    print("lead_to_gold(): ", lead_to_gold())
    print("stone_to_gem(): ", stone_to_gem())

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): ", philosophers_stone())
    print("elixir_of_life(): ", elixir_of_life())
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): ",
          alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): ",
          alchemy.transmutation.philosophers_stone())
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
