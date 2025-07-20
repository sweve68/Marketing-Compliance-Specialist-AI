from abc import ABC, abstractmethod

class AbstractLLM(ABC):
    @abstractmethod
    def get_specific_text(self, url):
        pass

    @abstractmethod
    def check_for_compliance(self, target_str, template):
        pass