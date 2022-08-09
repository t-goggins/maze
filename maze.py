import csv

def load_map(filename):
    """Load map from external csv file into a variable, then return that 
    variable"""

    # Create a map variable to load the map into - then return
    this_map = []

    # Open the external map file
    with open(filename, mode="r") as file:
        mapfile = csv.reader(file)
        # Append each line of the csv as a list into the this_map list
        for line in mapfile:
            this_map.append(line)

    return this_map

class Maze_Map():
    """Map Class"""

    def __init__(self, filename):
        """Creates a maze map object"""
        # Load map from external file
        self.squares = load_map(filename)

    def print_map(self):
        """Prints map"""
        for row in self.squares:
            for col in row:
                print(col, end="")
            print()

class Player():
    pass
    # def __init__(self, x, y):
    #     self.x = x 
    #     self.y = y



def main():

    # Create a map
    my_map = Maze_Map('map.csv')

    # Print map
    my_map.print_map()


if __name__ == '__main__':
    main()
