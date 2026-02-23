import time


class Event():
    def __init__(self, id, owner, name):
        self.id = id
        self.owner = owner
        self.name = name

    def get_event(self, id):
        return f"Event {id}: Player {self.owner} {self.name}"


class Player():
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl

    def __str__(self):
        return f"{self.name} (level {self.lvl})"


def fibo(n: int):
    a = 0
    b = 1
    for i in range(n):
        yield a
        old_a = a
        a = b
        b = old_a + b


def event_generator(n: int):
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
    for i in range(0, n):
        current_player = players[i % len(players)]
        current_event = events[i % len(events)]
        if current_player.lvl >= 10:
            top_players = 1
        else:
            top_players = 0
        result = f"Event {i + 1}: Player {current_player}, {current_event}"
        yield (
            result, current_event, top_players, current_player
            )


def data_stream() -> float:
    # events = [
    #     "logged in", "leveled up", "found treasure",
    #            "killed monster", "died", "logged out"
    # ]
    # charlie = Player("charlie", 10)
    # alice = Player("alice", 8)
    # bob = Player("bob", 12)
    # frank = Player("frank", 2)
    # players = [charlie, alice, bob, frank]
    number_of_events = 1000
    lvl_up = 0
    trs_fnd = 0
    top_players = 0
    start = time.time()
    for event in event_generator(number_of_events):
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


if __name__ in "__main__":
    elapced_time = data_stream()
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {elapced_time:.3f} seconds")
    print("\n=== Generator Demonstration ===")
    fibo_demo = 10
    print(f"Fibonacci sequence (first {fibo_demo}):")
    for _ in fibo(fibo_demo):
        print(_, end=" ")
    prime_demo = 5
    
