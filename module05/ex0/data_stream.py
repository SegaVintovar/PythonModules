from abc import ABC, abstractmethod
from typing import Any

class Logs():
    def __init__(self, data: str, type: str):
        self.data = data
        self.type = type

class DataProcessor(ABC):
    def format_optput(data: Any) -> str:
        if type(data[0]) == int:
            return NumericProcessor.format_optput(data)
        if type(data) == str:
            return TextProcessor.format_optput(data)
        if type(data) == Logs:
            return LogProcessor.format_optput(data)

    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__(self)
        print("Initializing Numeric Processor...")
        self.__data = None
    
    @abstractmethod
    def process(data: Any) -> list:
        # self.__data = data
        print("Processing data: ", data)
        return str(data)

    @abstractmethod
    def validate(data: Any) -> bool:
        for i in data:
            try:
                if type(i) == int:
                    continue
                else:
                    raise TypeError
            except TypeError:
                print(i, " - is not valid")
                return False
        print("Validation: Numeric data verified")
        return True

    def format_optput(data: Any) -> str:
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
        super().__init__(self)

    @abstractmethod
    def process(data: Any) -> str:
        print("Processing data: ", data)
        return str(data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        try:
            if type(data) != str:
                raise TypeError
        except TypeError:
            return False
        else:
            print("Validation: Text data verified")
            return True
    
    def format_optput(data: Any) -> str:
        if data:
            words = 1
            for char in data:
                new_char
                old_char
                if char == " ":
                    words += 1
                

class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__(self)

    @abstractmethod
    def process(data: Logs) -> str:
        ...

    @abstractmethod
    def validate(data: Logs) -> bool:
        ...

    def format_optput(data: Logs) -> str:
        ...

def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    num_data = [1, 2, 3, 5, 5]
    NumericProcessor.process(num_data)
    if NumericProcessor.validate(num_data) == True:
        NumericProcessor.format_optput(num_data)
    txt_data = "Hello Nexus World"
    TextProcessor.process(txt_data)

    print()
    print("Processing multiple data types through same interface...")
    print(DataProcessor.format_optput(num_data))
    

main()