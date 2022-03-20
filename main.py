from class_Candidate import Candidate
from greedy import greedy
from input_parse import read_input
from plot import plot_labels
import sys


def main(file):
    candidate = Candidate()
    read_input(str(file), candidate)
    solution = greedy(candidate)
    print(solution) 
    plot_labels(candidate.list_of_labels, solution)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('File path required')
    else:
        main(sys.argv[1])