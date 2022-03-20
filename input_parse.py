from entity.Label import Label
from entity.Candidate import Candidate

def read_input(path, candidate: Candidate):
    file = open(path, 'r')

    for line in file:
        if line[0] == 'L':
            label_data = line.split()
            id = int(label_data[1])
            x1 = int(label_data[2])
            x2 = int(label_data[3])
            y1 = int(label_data[4])
            y2 = int(label_data[5])
            label = Label(id, x1, x2, y1, y2)
            candidate.add_label(label)