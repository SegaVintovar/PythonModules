from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict, Protocol


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
    result += [word]
    return result


class ProcessingStage(Protocol):
    def process(data) -> Any:
        pass


class InputStage(ProcessingStage):
    name = "Input validation and parsing"

    def __init__(self):
        print(f"Stage 1: {self.name}")

    def process(self, data: Any) -> Dict:
        if isinstance(data, Dict):
            print(f"Input: {data}")
            return data
        if isinstance(data, str):
            print(f"Input: {data}")
            return {"CSV data": [my_split(data, ',')]}
        if isinstance(data, List):
            print("Input: Real-time sensor stream")
            return {"sensor data": data}
        else:
            raise TypeError("Input stage Error: invalid data type")


class TransformStage(ProcessingStage):
    """Should call Adapter according to the class"""
    name = "Data transformation and enrichment"

    def __init__(self):
        print(f"Stage 2: {self.name}")

    def process(self, data: Any) -> Dict:
        if isinstance(data, Dict):
            JSONAdapter.process(data)
            print("Transform: Enriched with metadata and validation")
            return data
        if isinstance(data, str):
            CSVAdapter.process(data)
            print("Transform: Parsed and structured data")
            return {"CSV data": [my_split(data, ',')]}
        if isinstance(data, List):
            StreamAdapter.process(data)
            print("Transform: Aggregated and filtered")
            return {"sensor data": data}
        else:
            raise TypeError("Transform stage Error: invalid data type")


class OutputStage(ProcessingStage):
    name = "Output formatting and delivery"

    def __init__(self):
        print(f"Stage 3: {self.name}")

    def process(self, data: Any) -> str:
        if isinstance(data, Dict):
            result1 = f"Output: Processed {data['sensor']} reading:"
            result2 = f" {data['value']}{data['unit']}"
            print(result1 + result2)
            return result1 + result2
        if isinstance(data, str):
            my_list = my_split(data, ',')
            i = 0
            for element in my_list:
                if element == "action":
                    i += 1
            result = f"Output: User activity logged: {i} actions processed"
            print(result)
            return result
        if isinstance(data, List):
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
            return result
        else:
            raise TypeError("Output stage Error: invalid data type")


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages = []

    # @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    def add_stage(self, stage: ProcessingStage):
        self.stages += [stage]


class NexusManager():
    def __init__(self):
        print("Initializing Nexus Manager...")
        print("Pipeline capacity: 1000 streams/second")
        self.pipelines = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines += [pipeline]

    def process_data(self, data: Any) -> None:
        for stage in self.pipelines:
            stage.process(data)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.data = {}

    def process(data: Dict) -> Union[str, Any]:
        result = {key: value for key, value in data.items()}
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.data = {}

    def process(data: str) -> Any:
        my_list = my_split(data, ",")
        result = {
            "user": my_list[0],
            "action": my_list[1],
            "timestamp": my_list[2]
            }
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.id = pipeline_id
        self.data = {}

    def process(data: List) -> Any:
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
        print(result)
        return result


def main():
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
    err_data = (1, 2)
    print(
        "\n=== Error Recovery Test ===",
        "\nSimulating pipeline failure..."
        )
    try:
        nexus.process_data(err_data)
    except Exception as e:
        print(str(e))
    finally:
        print(
            "\nRecovery initiated: Switching to backup processor",
            "\nRecovery successful: Pipeline restored, processing resumed"
            )
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
