from class_Label import Label

class Candidate():

    def __init__(self) -> None:
        self.list_of_labels = []
        self.conflicts = 0
        self.list_of_conflicts= []
        self.free_labels = 0

    def add_label(self, label: Label):
        self.list_of_labels.append(label)

    def search_label(self, id):
        for label in self.list_of_labels:
            if label.id == id:
                return label
        return None