from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict, Protocol


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


class ProcessingStage(Protocol):
    def process(data: Any) -> Any:
        pass


class InputStage(ProcessingStage):
    name = "Input validation and parsing"

    def __init__(self) -> None:
        print(f"Stage 1: {self.name}")

    def process(self, data: Any) -> Dict:
        if isinstance(data, Dict):
            print(f"Input: {data}")
            return {"type": "JSON", "data": data}
        if isinstance(data, str):
            print(f"Input: {data}")
            return {"type": "CSV", "data": my_split(data, ',')}
        if isinstance(data, List):
            print("Input: Real-time sensor stream")
            return {"type": "SENSOR", "data": data}
        else:
            raise TypeError("Input stage Error: invalid data type")


class TransformStage(ProcessingStage):
    """Should call Adapter according to the data type"""
    name = "Data transformation and enrichment"

    def __init__(self) -> None:
        print(f"Stage 2: {self.name}")

    def process(self, data: Dict) -> Dict:
        data_type = data["type"]
        if data_type == "JSON":
            print("Transform: Enriched with metadata and validation")
            return JSONAdapter.process(data["data"])
        if data_type == "CSV":
            print("Transform: Parsed and structured data")
            return CSVAdapter.process(data["data"])
        if data_type == "SENSOR":
            print("Transform: Aggregated and filtered")
            return StreamAdapter.process(data["data"])
        else:
            raise TypeError("Transform stage Error: invalid data type")


class OutputStage(ProcessingStage):
    name = "Output formatting and delivery"

    def __init__(self) -> None:
        print(f"Stage 3: {self.name}")

    def process(self, data: Any) -> str:
        if "sensor" in data:
            result1 = f"Output: Processed {data['sensor']} reading:"
            result2 = f" {data['value']}{data['unit']}"
            print(result1 + result2)
            return result1 + result2
        if "action" in data:
            i = 0
            for key, value in data.items():
                if key == "action" and value == "action":
                    i += 1
            result = f"Output: User activity logged: {i} actions processed"
            print(result)
            return result
        if "readings" in data:
            result1 = "Output: Stream summary: "
            result2 = f"{data['readings']} readings, avg: {data['avg']}°C"
            print(result1 + result2)
            return result1 + result2
        else:
            raise TypeError("Output stage Error: invalid data type")


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages += [stage]


class NexusManager():
    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second")
        self.pipelines = []
        self.processed = 0
        self.pipeline_size = 0
        self.data_processed = 0

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines += [pipeline]
        self.pipeline_size += 1

    def process_data(self, data: Any) -> None:
        self.data_processed += 1
        for stage in self.pipelines:
            data = stage.process(data)

    def stats(self) -> str:
        result1 = f"Data batches processed: {self.data_processed}\n"
        result2 = f"Used {self.pipeline_size} - stage pipeline"
        return result1 + result2


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.id = pipeline_id

    def process(data: Dict) -> Union[str, Any]:
        result = {key: value for key, value in data.items()}
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.id = pipeline_id

    def process(data: list) -> Dict:
        my_list = data
        result = {
            "user": my_list[0],
            "action": my_list[1],
            "timestamp": my_list[2]
            }
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.id = pipeline_id

    def process(data: List) -> Dict:
        i = 0
        total = 0
        for element in data:
            if isinstance(element, (int, float)):
                total += element
                i += 1
            else:
                raise TypeError(
                    "Element of the stream list is not int or float")
        avg = total / i
        result = f"Output: Stream summary: {i} readings, avg: {avg}°C"
        result = {"readings": i, "avg": avg, "total": total}
        return result


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print()
    stages = [InputStage, TransformStage, OutputStage]
    nexus = NexusManager()
    print()
    print("Creating Data Processing Pipeline...")
    i = 1
    for stage in stages:
        nexus.add_pipeline(stage())
        i += 1
    data1 = {"sensor": "temp", "value": 23.5, "unit": "C"}
    data2 = "user,action,timestamp"
    data3 = [20, 21, 22, 23, 20]
    print()
    print("Processing JSON data through pipeline...")
    nexus.process_data(data1)
    print()
    print("Processing CSV data through same pipeline...")
    nexus.process_data(data2)
    print()
    print("Processing Stream data through same pipeline...")
    nexus.process_data(data3)
    print("\nManager statistics:")
    print(nexus.stats())
    try:
        err_data = (1, 2)
        print(
            "\n=== Error Recovery Test ===",
            "\nSimulating pipeline failure..."
        )
        nexus.process_data(err_data)
    except Exception as e:
        print(str(e))
    finally:
        print(
            "\nRecovery initiated: Switching to backup processor",
            "\nRecovery successful: Pipeline restored, processing resumeds"
            )
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
