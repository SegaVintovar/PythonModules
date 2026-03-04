from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: Any) -> Any:
        ...
