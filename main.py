from sorting import *
from shortest_path import *

def main():
    chosen = False
    while not chosen:
        algorithm = input("Which algorithm would you like to use? (help): ")
        
        if algorithm == "help":
            print("Enter 1 to run Djikstra's Algorithm.")
            print("Enter 2 to run Insertion Sort.")
            print("Enter help to get this message.")
        elif algorithm == "1":
            run_djikstra()
            chosen = True
        elif algorithm == "2":
            run_insertion_sort()
            chosen = True


if __name__ == "__main__":
    main()