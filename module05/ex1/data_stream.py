from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class StreamBase(ABC):
    def __init__(self, id: str):
        self.id = id
        self.data = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    @abstractmethod
    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        ...

    @abstractmethod
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(StreamBase):
    def __init__(self, id: str):
        super().__init__(self)
        self.id = id
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.id}, Type: Enviromental Data")
        self.data = {
            "readings": 0, "avg temp": None, "humidity": 0, "pressure": 0
            }

    def process_batch(self, data_batch: List[Any]) -> str:
        result = ""
        total_temp = 0
        temps = 0
        i = 0
        for data in data_batch:
            entry = data.items()
            for key, value in entry:
                result += str(key) + ":" + str(value) + ", "
                if key == "temp":
                    total_temp += value
                    temps += 1
                if key == "humidity":
                    self.data["humidity"] = value
                if key == "pressure":
                    self.data["pressure"] = value
            i += 1
        self.data["readings"] = i
        self.data["avg temp"] = total_temp / temps
        pref = "Processing sensor batch: "
        return pref + result[:-2]

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        result = []
        for data in data_batch:
            entry = data.items()
            for key, value in entry:
                if key == criteria:
                    result += [{key: value}]
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        # result1 = "Sensor analysis: "
        # result2 = f"{self.data['readings']} readings processed, "
        # result3 = f"avg temp: {self.data['avg temp']}"
        return {key: value for key, value in self.data.items()
                }


class TransactionStream(StreamBase):
    def __init__(self, id: str):
        super().__init__(self)
        self.id = id
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.id}, Type: Financial data")
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

    def filter_data(
            self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        
        result = []
        for data in data_batch:
            entry = data.items()
            for key, value in entry:
                if value == criteria:
                    result += [{key: value}]
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {key: value for key, value in self.data.items()
                }


class EventStream(StreamBase):
    def __init__(self, id: str):
        self.id = id
        self.events: List = []
        self.number_of_events = 0
        self.data = {"login": 0, "logout": 0, "error": 0}
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Processing event batch: ", data_batch)
        i = 0
        for data in data_batch:
            if data == "error":
                self.data["error"] += 1
            if data == "login":
                self.data["login"] += 1
            if data == "logout":
                self.data["logout"] += 1
            self.events += [data]
            i += 1
        self.number_of_events = i
        result1 = f"Event analysis: {i} events, "
        result2 = f"{self.data['error']} errors detected"
        return result1 + result2

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
            ) -> List[Any]:
        result = []
        for data in data_batch:
            if data == criteria:
                result += data
        return result

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.data


class StreamProcessor():
    def __init__(self):
        self.important_data = {"sensor alerts": 0, "big transactions": 0}

    def process(
            self, stream: EventStream | TransactionStream | SensorStream):
        # for stream in data_batch:
        if isinstance(stream, SensorStream):
            print(
                f"- Sensor data: {stream.data['readings']}",
                " readings processed"
            )
            for key, value in stream.data.items():
                if key == "pressure":
                    if value > 1000:
                        self.important_data["sensor alerts"] += 1
        if isinstance(stream, TransactionStream):
            print(
                f"- Transaction data: {stream.data['total_actions']}",
                " operations processed"
            )
            for key, value in stream.data.items():
                if value > 100:
                    self.important_data["big transactions"] += 1
        if isinstance(stream, EventStream):
            print(
                f"- Event data: {stream.number_of_events}",
                " events processed"
            )
    
    def stream_filter(self):
        print("Stream filtering active: High-priority data only")
        print(
            "Filtered results: ",
            f"{self.important_data['sensor alerts']} critical sensor alerts,",
            f" {self.important_data['big transactions']} large transaction")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    sensor_data_batch = [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
    print(
        sensor.process_batch(sensor_data_batch)
        )
    sens_analysis = sensor.get_stats()
    print(
        "Sensor analysis: ",
        f"{sens_analysis['readings']} readings processed",
        f"avg_temp: {sens_analysis['avg temp']}°C")
    humid_filter = sensor.filter_data(sensor_data_batch, "humidity")
    print("Data filter test(humidity): ", humid_filter)

    print()

    transaction = TransactionStream("TRANS_001")
    transaction_data = [("buy", 100), ("sell", 150), ("buy", 75)]
    print(transaction.process_batch(transaction_data))
    trans_stats = transaction.get_stats()
    print(
        "Transaction analysis: ",
        f"{trans_stats['total_actions']} operations, ",
        f"net flow: {trans_stats['delta']}"
    )

    print()

    evets = ["login", "error", "logout"]
    event = EventStream("EVENT_001")
    print(event.process_batch(evets))

    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    my_streams = [sensor, transaction, event]
    print("Batch 1 Results:")
    st_proc = StreamProcessor()
    for stream in my_streams:
        st_proc.process(stream)
    print()
    st_proc.stream_filter()
    print()
    print("All streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    main()


data = ['temp:25', 'buy:40', 'buy:100', 'login', ]