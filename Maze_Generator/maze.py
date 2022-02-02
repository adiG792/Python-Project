from colorama import init, Fore

cell = "c"
wall = "w"


def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append("u")
        maze.append(line)
    return maze


init()  # to initialize colorama

def