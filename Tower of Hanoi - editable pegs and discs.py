# Sarai Ayon
# 5/7/2024
# CS 240 Data Structures and Algorithms
# Miterm Project - Tower of Hanoi - recursive editable pegs and discs 


def tower_of_hanoi_recursive(num_disks, source_rod, target_rod, auxiliary_rods, pegs):
    if num_disks == 0:
        return
    if num_disks == 1:
        print("Move disk 1 from", source_rod, "to", target_rod)
        pegs[target_rod].append(pegs[source_rod].pop())
        print_pegs(pegs)
        return
    
    # Find the auxiliary rods for this step
    available_rods = list(range(len(pegs)))
    available_rods.remove(source_rod)
    available_rods.remove(target_rod)
    auxiliary_rod = available_rods[0]
    
    # Move the top num_disks-1 disks from source to auxiliary
    tower_of_hanoi_recursive(num_disks-1, source_rod, auxiliary_rod, auxiliary_rods, pegs)
    
    # Move the bottom disk from source to target
    print("Move disk", num_disks, "from", source_rod, "to", target_rod)
    pegs[target_rod].append(pegs[source_rod].pop())
    print_pegs(pegs)
    
    # Move the num_disks-1 disks from auxiliary to target
    tower_of_hanoi_recursive(num_disks-1, auxiliary_rod, target_rod, auxiliary_rods, pegs)

def print_pegs(pegs):
    for i, peg in enumerate(pegs):
        print("Peg", i + 1, ":", peg)

def get_user_input():
    print("WELCOME!")
    print("The Tower of Hanoi is a mathematical game or puzzle that consists of three rods and a number of disks of different sizes which can slide onto any rod.")
    print("The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.")
    print("The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:")
    print()
    print("1. Only one disk can be moved at a time.")
    print("2. Each move consists of taking the top disk from one of the stacks and placing it on top of another stack.")
    print("3. No disk may be placed on top of a smaller disk.")
    print()
    print("Enter the number of disks and pegs for the Tower of Hanoi puzzle.")
    print("**The number of disks must be at least 1.")
    print("**The number of pegs must be at least 3.")
    
    num_disks = int(input("Enter the number of disks: "))
    while num_disks < 1:
        print("Invalid input. The number of disks must be at least 1.")
        num_disks = int(input("Enter the number of disks: "))
    
    num_pegs = int(input("Enter the number of pegs: "))
    while num_pegs < 3:
        print("Invalid input. The number of pegs must be at least 3.")
        num_pegs = int(input("Enter the number of pegs: "))
    
    return num_disks, num_pegs

num_disks, num_pegs = get_user_input()
source_rod = 0
target_rod = num_pegs - 1
auxiliary_rods = list(range(1, num_pegs - 1))

pegs = [[] for _ in range(num_pegs)]
pegs[source_rod] = list(reversed(range(1, num_disks + 1)))

tower_of_hanoi_recursive(num_disks, source_rod, target_rod, auxiliary_rods, pegs)

print("Thanks for using the Tower of Hanoi puzzle!")
