from math import pow

class Item():
    """Class containing information about an item to be ranked"""
    def __init__(self,
            data: dict):
        self.name: str = data["name"]
        self.info: dir = {k: v for k, v in data.items() if k != "name"}
        self.elo : int = 0.5

class Matchup():
    """Matchup created between two items"""
    def __init__(self, left, right):

        self.left = left
        self.right = right

    def score(self, left_win: bool = True):
        if left_win:
            delta = pow(self.left, 2)
            self.left.elo = round(self.left.elo - delta, 5)
            self.right.elo = round(self.right.elo + delta, 5)

        else:
            delta = pow(self.right, 2)
            self.left.elo = round(self.left.elo + delta, 5)
            self.right.elo = round(self.right.elo - delta, 5)


def main():
    d1 = { "name" : "meow", "post" : "cat", "glow" : "stick" }
    d2 = { "name" : "wof", "bread" : "no" }
    i1 = Item(d1)
    i2 = Item(d2)
    i1.elo = 0.5
    i2.elo = 0.5
    m = Matchup(i1, i2)
    print(m.lower.name, i1.elo)
    print(m.higher.name, i2.elo)

if __name__ == "__main__":
    main()