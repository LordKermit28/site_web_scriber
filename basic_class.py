from abc import ABC, abstractmethod


class BasicClass(ABC):
    @abstractmethod
    def get_request(self, keywords, count):
        pass