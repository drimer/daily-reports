import abc


class Report(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


class ReportRunner(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self) -> Report:
        ...

    
class ReportSender(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def send(self, report: Report) -> None:
        ...