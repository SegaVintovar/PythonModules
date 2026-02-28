import time
from typing import Any, Generator, NoReturn


class Event():
    def __init__(self, id, owner, name):
        self.id = id
        self.owner = owner
        self.name = name

    def get_event(self, id) -> str:
        return f"Event {id}: Player {self.owner} {self.name}"


class Player():
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl

    def __str__(self):
        return f"{self.name} (level {self.lvl})"


def fibo():
    a = 0
    b = 1
    while True:
        yield a
        old_a = a
        a = b
        b = old_a + b


def prime() -> Generator[int, Any, None]:
    i = 2
    p = 0
    while True:
        j = i
        while (j > 0):
            if j == 1:
                p += 1
                yield i
            if i != j and i % j == 0:
                break
            else:
                j -= 1
        i += 1


def event_generator() -> Generator[
    tuple[str, str, bool, Player], Any, NoReturn
]:
    """
    Generator[YieldType, SendType, ReturnType]
    ReturnType also can be None
    """
    events = [
        "logged in", "leveled up", "found treasure",
        "killed monster", "died", "logged out"
    ]
    charlie = Player("charlie", 10)
    alice = Player("alice", 8)
    bob = Player("bob", 12)
    frank = Player("frank", 2)
    players = [charlie, alice, bob, frank]
    top_players = 0
    i = 0
    while True:
        i += 1
        current_player = players[(i + 1) % len(players)]
        current_event = events[(i - 1) % len(events)]
        if current_player.lvl >= 10:
            top_players = True
        else:
            top_players = False
        result = f"Event {i}: Player {current_player}, {current_event}"
        yield (
            result, current_event, top_players, current_player
            )


def data_stream() -> float:
    print("=== Game Data Stream Processor ===\n")
    number_of_events = 10
    lvl_up = 0
    trs_fnd = 0
    top_players = 0
    start = time.time()
    print(f"Processing {number_of_events} game events...\n")
    gen_event = event_generator()
    for _ in range(number_of_events):
        event = next(gen_event)
        print(event[0])
        if event[1] == "leveled up":
            lvl_up += 1
            event[3].lvl += 1
        if event[1] == "found treasure":
            trs_fnd += 1
        if event[2]:
            top_players += 1
    end = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {number_of_events}")
    print(f"High-level players (10+): {top_players}")
    print(f"Treasure events: {trs_fnd}")
    print(f"Level-up events: {lvl_up}")
    return end - start


if __name__ == "__main__":
    elapced_time = data_stream()
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {elapced_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    fibo_demo = 10
    print(f"Fibonacci sequence (first {fibo_demo}): ", end="")
    i = 0
    fibo_gen = fibo()
    while i < fibo_demo:
        print(next(fibo_gen), end=" ")
        i += 1
    prime_demo = 10
    print()
    print(f"Prime numbers: (first {prime_demo}): ", end="")
    prime_gen = prime()
    for _ in range(prime_demo):
        print(next(prime_gen), end=" ")
    print()
