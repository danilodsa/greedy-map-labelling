import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_labels(labels, feasible_solution):

    fig, ax = plt.subplots()
    # ax.plot([0,20],[0,20])
    ax_max = 0
    
    for label in labels:
        width = label.x2 - label.x1
        height = label.y2 - label.y1
        
        if max([label.x2, label.y2]) > ax_max:
            ax_max = max([label.x2, label.y2])


        if label.id in feasible_solution:
            ax.add_patch(Rectangle((label.x1, label.y1), width, height, fill=False, edgecolor='red', lw=2))
        else:
            ax.add_patch(Rectangle((label.x1, label.y1), width, height, fill=False))

    lims = (0,(ax_max+1))
    plt.ylim(lims)
    plt.xlim(lims)
    plt.show()