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

    def process(data: Any) -> Dict:
        print(f"Input: {data}")
        if isinstance(data, Dict):
            return {"json": data}
        if isinstance(data, str):
            return {"csv": data}
        if isinstance(data, List):
            return {"stream": data}


class TransformStage(ProcessingStage):
    name = "Data transformation and enrichment"

    def process(data: Dict) -> Dict:
        if "json" in data:
            message = "Enriched with metadata and validation"
        if "csv" in data:
            message = "Parsed and structured data"
        if "stream" in data:
            message = "Aggregated and filtered"
        else:
            message = "Unknown data"
        print(f"Transform: {message}")
        return data


class OutputStage(ProcessingStage):
    name = "Output formatting and delivery"

    def process(data: Any) -> str:
        if "json" in data:
            result1 = "Output: Processed temperature reading: "
            result2 = f"{data["json"]["value"]} {data["json"]["unit"]}"
            message = result1 + result2
        if "csv" in data:

            message = "Parsed and structured data"
        if "stream" in data:
            message = "Aggregated and filtered"
        else:
            message = "Unknown data"
        print(message)
        return message


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        print("Creation of the pipeline")
        self.stages = []

    @abstractmethod
    def process(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        self.pipeline_id = pipeline_id

    def process(self, data: Any):
        print("\nProcessing JSON data through pipeline...")
        return self.pipeline_id.process(data)


class NexusManager():
    def __init__(self) -> None:
        self.pipelines = []

    def add_pipeline(self, pipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data):
        for pipeline in self.pipelines:
            pipeline.process(data)


def main():
    data1 = {"sensor": "temp", "value": 23.5, "unit": "C"}
    data2 = "user,action,timestamp"
    data3 = [20, 21, 22, 23, 20]
    print()
    pipe = ProcessingPipeline()
    print()
    stages = [InputStage, TransformStage, OutputStage]
    for stage in stages:
        pipe.add_stage(stage)
    nexus = NexusManager()
    nexus.add_pipeline(pipe)
    json_adapter = JSONAdapter(pipe)
    json_adapter.process(data1)


if __name__ == "__main__":
    main()
    