from abc import abstractmethod, ABC

class FileTreeEntry(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self) -> float:
        ...

class Directory(FileTreeEntry):
    def __init__(self, name):
        super().__init__(name)
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_size(self):
        total_size = 0

        for entry in self.entries:
            total_size += entry.get_size()

        return total_size
    
class File(FileTreeEntry):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size
    

documents = Directory("Documents")
thesis = File("phd-thesis.pdf", 270)
report = File("report.pdf", 385)
private = Directory("Private")
porn = File("porn.mp4", 10627)

documents.add_entry(thesis)
documents.add_entry(report)

private.add_entry(porn)
documents.add_entry(private)

print(documents.get_size())