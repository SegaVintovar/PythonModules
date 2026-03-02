from abc import ABC, abstractmethod
from typing import Any


class Logs():
    def __init__(self, data: str, type: str):
        self.data = data
        self.type = type


class DataProcessor(ABC):
    def __init__(self):
        super().__init__()

    def format_output(data: Any) -> str:
        if type(data) is Logs:
            return LogProcessor.format_output(data)
        if type(data[0]) is int:
            return NumericProcessor.format_output(data)
        if type(data) is str:
            return TextProcessor.format_output(data)

    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        print("Initializing Numeric Processor...")

    def process(data: Any) -> str:
        # self.__data = data
        print("Processing data: ", data)
        return str(data)

    def validate(data: Any) -> bool:
        for i in data:
            try:
                if type(i) is int:
                    continue
                else:
                    raise TypeError
            except TypeError:
                print(i, " - is not valid")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_output(data: Any) -> str:
        i = 0
        total = 0
        for item in data:
            total += item
            i += 1
        avg = total / i
        result = f"Processed {i} numeric values, "
        result2 = f"sum={total}, avg={avg:.1f}"
        return result + result2


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(data: Any) -> str:
        print("Processing data: ", data)
        return str(data)

    def validate(data: Any) -> bool:
        try:
            if type(data) is not str:
                raise TypeError
        except TypeError:
            return False
        else:
            print("Validation: Text data verified")
            return True

    def format_output(data: Any) -> str:
        if data:
            words = 1
            old_char = " "
            characters = 0
            for char in data:
                if char == " " and old_char != " ":
                    words += 1
                old_char = char
                characters += 1
        result1 = f"Processed text: {characters} characters,"
        result2 = f" {words} words"
        return result1 + result2


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__(self)

    def process(data: Logs) -> str:
        print("Processing data: ", f"{data.type}: {data.data}")

    def validate(data: Logs) -> bool:
        if type(data) is Logs:
            print("Validation: Log entry verified")
            return True
        else:
            return False

    def format_output(data: Logs) -> str:
        output = None
        if data.type == "ERROR":
            output = "[ALERT]"
        if data.type == "INFO":
            output = "[INFO]"
        return f"{output} {data.type} level detected: {data.data}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    num_data = [1, 2, 3, 5, 5]
    NumericProcessor.process(num_data)
    if NumericProcessor.validate(num_data) is True:
        print("Output: ", NumericProcessor.format_output(num_data))
    print()
    txt_data = "Hello Nexus World"
    TextProcessor.process(txt_data)
    if TextProcessor.validate(txt_data) is True:
        print("Output: ", TextProcessor.format_output(txt_data))
    print()
    err_log = Logs("Connection timeout", "ERROR")
    info_log = Logs("System ready", "INFO")
    LogProcessor.process(err_log)
    if LogProcessor.validate(err_log) is True:
        print("Output: ", LogProcessor.format_output(err_log))
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    i = 1
    mydata = [[1, 2, 3], "hello world!", info_log]
    for data in mydata:
        print(f"Result {i}: ", DataProcessor.format_output(data))
        i += 1


if __name__ == "__main__":
    main()
