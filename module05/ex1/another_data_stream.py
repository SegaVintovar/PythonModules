from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


def my_split(data: str, separator: str) -> List[str]:
    result = []
    word = ""
    for char in data:
        if char == separator:
            if word != "":
                result += [word]
                word = ""
        elif char != separator:
            word += char
    if word != "":
        result += [word]
    return result


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        filtered_data = []
        for data in data_batch:
            elements = my_split(data)
            if elements[0] == criteria:
                filtered_data.append(data)
        return filtered_data

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.id = stream_id
        self.type = "Environmental Data"
        self.temp = 0
        self.alerts = 0
        self.readings = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        i = 0
        for data_entry in data_batch:
            data = my_split(data_entry, ":")
            if data[0] == "temp":
                self.temp = float(data[1])
            if data[0] == "humidity":
                if int(data[1]) < 70:
                    self.alerts += 1
            i += 1
        self.readings = i
        return f"{i} readings processed, avg temp: {self.temp}°C"

    def get_stats(self) -> None:
        print(f"- Sensor data: {self.readings} readings processed")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.id = stream_id
        self.type = "Financial Data"
        self.operations = 0
        self.expences = 0
        self.income = 0
        self.net_flow = 0
        self.big_t = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        i = 0
        for data_entry in data_batch:
            data = my_split(data_entry, ":")
            if data[0] == "buy":
                self.expences += int(data[1])
            if data[0] == "sell":
                self.income += int(data[1])
            if int(data[1]) > 100:
                self.big_t += 1
            i += 1
        self.operations = i
        self.net_flow = self.income - self.expences
        return f"{i} operations, net flow {self.net_flow}"

    def get_stats(self) -> None:
        print(f"- Transaction data: {self.operations} operations processed")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.id = stream_id
        self.type = "System Events"
        self.errors = 0
        self.events = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        i = 0
        for data_entry in data_batch:
            if data_entry == "error":
                self.errors += 1
            i += 1
        self.events = i
        return f"{i} events, {self.errors} errors detected"

    def get_stats(self) -> None:
        print(f"- Event data: {self.events} readings processed")


class StreamProcessor():
    def __init__(self) -> None:
        pass

    def stats(self, stream) -> None:
        stream.get_stats()


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.id}, Type: {sensor.type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    result = sensor.process_batch(sensor_batch)
    print("Sensor analysis: ", result)
    print()
    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.id}, Type: {transaction.type}")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    result = transaction.process_batch(transaction_batch)
    print("Transaction analysis: ", result)
    print()
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.id}, Type: {event.type}")
    event_batch = ["login", "error", "logout"]
    result = event.process_batch(event_batch)
    print("Event analisys: ", result)
    print()
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    print("Batch 1 Results:")
    batch_1 = [sensor, transaction, event]
    stream_proc = StreamProcessor()
    for stream in batch_1:
        stream_proc.stats(stream)
    print()
    print("Stream filtering active: High-priority data only")
    print(f"Filtered results: {sensor.alerts} sensor alerts, ",
          f"{transaction.big_t} large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()