from abc import abstractmethod, ABC

class FileTreeEntry(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_size(self) -> float:
        ...
        
    @abstractmethod
    def print_tree(self, indent=0):
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
    
    def print_tree(self, indent=0):
        print(f"{" " * indent}> {self.name}")
        
        for entry in self.entries:
            entry.print_tree(indent + 2)
    
class File(FileTreeEntry):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_size(self):
        return self.size
    
    def print_tree(self, indent=0):
        print(f"{" " * indent}- {self.name}")
    

documents = Directory("Documents")
thesis = File("phd-thesis.pdf", 270)
report = File("report.pdf", 385)
private = Directory("Private")
porn = File("urlaub.mp4", 10627)
public = Directory("Public")
course_list = File("course_list.pdf", 3400)

documents.add_entry(thesis)
documents.add_entry(report)

private.add_entry(porn)
documents.add_entry(private)

public.add_entry(course_list)
documents.add_entry(public)

print(documents.get_size())
documents.print_tree()