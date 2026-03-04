from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union, Dict


class ProcessingPipeline(ABC):
    def process(self, data: Any) -> Any