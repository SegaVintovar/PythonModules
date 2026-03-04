from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class StreamBase(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(StreamBase):
    def __init__(self, id: str, data_type: str):
        super().__init__()
        self.id = id
        self.type = data_type
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.id}, Type: {self.type}")
        self.data = {"readings": 0, "avg temp": None}

    def process_batch(self, data_batch: List[Any]) -> str:
        result = ""
        total_temp = 0
        temps = 0
        i = 0
        for data in data_batch:
            result += data[0] + ":" + str(data[1]) + ", "
            if data[0] == "temp":
                total_temp += data[1]
                temps += 1
            i += 1
        self.data["readings"] = i
        self.data["avg temp"] = total_temp / temps
        return result

    def sensor_analysis(self) -> str:
        result1 = "Sensor analysis: "
        result2 = f"{self.data['readings']} readings processed, "
        result3 = f"avg temp: {self.data['avg temp']}"
        return result1 + result2 + result3
        
        


class TransactionStream(StreamBase):
    def __init__(self, id: str, data_type: str):
        super().__init__()
        self.id = id
        self.type = data_type
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.id}, Type: {self.type}")
        self.data = {"buy": 0, "sell": 0, "total_actions": 0, "delta": 0}

    def process_batch(self, data_batch: List[Any]) -> str:
        i = 0
        for data in data_batch:
            if data[0] == "buy":
                self.data["buy"] += data[1]
            if data[0] == "sell":
                self.data["sell"] += data[1]
            i += 1
        self.data["total_actions"] = i
        self.data["delta"] = self.data["sell"] - self.data["buy"]
        res_str = "Processing transaction batch: "
        proc = [f"{data[0]}: {data[1]}" for data in data_batch]
        return res_str + str(proc)

    def sensor_analysis(self):
        


class EventStream(StreamBase):
    def process_batch(self, data_batch: List[Any]) -> str:
        ...


class StreamProcessor():
    ...


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor = SensorStream("SENSOR_001", "Enviromental Data")
    sensor_data_batch = [("temp", 22.5), ("humidity", 65), ("pressure", 1013)]
    print("Processing sensor batch:", [sensor.process_batch(sensor_data_batch)])
    print(sensor.sensor_analysis())
    print()
    transaction = TransactionStream("TRANS_001", "Financial data")
    transaction_data = [("buy", 100), ("sell", 150), ("buy", 75)]
    print(transaction.process_batch(transaction_data))


if __name__ == "__main__":
    main()