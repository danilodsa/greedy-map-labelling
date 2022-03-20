from random import random
from random import randrange
from class_Candidate import Candidate

def greedy(candidate: Candidate):
    label_list = candidate.list_of_labels
    init_label = randrange(len(label_list))
    feasible_solution = [init_label]

    for label in label_list:
        conflict = False
        if not(label.id in feasible_solution):
            for id in feasible_solution:
                if candidate.search_label(id).verify_colision(label):
                    conflict = True 
            
            if not(conflict):
                feasible_solution.append(label.id)

    return feasible_solution