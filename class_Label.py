
class Label():

    id = None
    x1 = None
    x2 = None
    y1 = None
    y2 = None

    def __init__(self, id, x1, x2, y1, y2):
        self.id = id
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_center(self):
        x = (self.x2 - self.x1)/2 
        x = self.x2 - x
        y = (self.y2 - self.y1)/2
        y = self.y2 - y
        return x, y

    def verify_colision(self, other_label):
        if (self.x1 < other_label.x2) and (other_label.x1 < self.x2) and (self.y1 < other_label.y2) and (other_label.y1 < self.y2):
            return True
        else:
            return False


