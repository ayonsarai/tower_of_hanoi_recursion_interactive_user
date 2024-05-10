Hanoi's Tower- Recursion ** for extra credit there is user input
The tower_of_hanoi_recursive function is the main function that solves the puzzle. It takes five parameters: the number of disks, the source rod, the target rod, the auxiliary rods, and the current state of the pegs.

If there are no disks left to move (i.e., num_disks == 0), the function returns and does nothing.

If there is only one disk left to move(i.e.num_disks == 1), the function prints a message indicating that it's moving the disk from the source rod to the target rod. 
It then moves the disk by popping it from the source peg to the target peg, and prints the current state of the pegs.

If there are more than one disks to move, the function first identifies the auxiliary rod for this step. It does this by creating a list of all rods, 
removing the source and target rods from the list, and selecting the first rod in the remaining list.

The function then recursively moves the top num_disks - 1 disks from the source rod to the auxiliary rod.

After that, it moves the bottom disk from the source rod to the target rod, and prints the current state of the pegs.

Finally, it recursively moves the num_disks - 1 disks from the auxiliary rod to the target rod.

The print_pegs function is a helper function that prints the current state of the pegs. It iterates over each peg and prints its number and the disks on it.

The get_user_input function (START) is another helper function that prints a welcome message and some information about the Tower of Hanoi puzzle, and prompts the user to enter the number of disks and pegs for the puzzle.


Time Complexity: 
The time complexity of tower_of_hanoi_recursive is O(2^n), because with each recursive call, the number of calls doubles (there are two recursive calls inside it). This is an exponential time complexity. 
The time complexity of print_pegs is O(n), as it has to print each peg's content once. The time complexity of get_user_input is constant because it just involves simple I/O operations.

Space Complexity:
The space complexity of tower_of_hanoi_recursive is O(n), as it uses space proportional to the number of disks for the call stack. The space complexity of print_pegs is O(n), because it creates an output string that grows with the number of disks.
The space complexity of get_user_input is also constant, as it does not use any additional space that scales with input size.

Advantages:
Recursive solutions often lead to cleaner, more readable code, especially for problems that can be naturally broken down into smaller, similar subproblems.
Recursion can provide elegant solutions for problems like tree traversal, searching, and sorting.It's particularly useful when dealing with data structures like trees and graphs.

Disadvantages:
Recursive solutions can be less efficient in terms of both time and space complexity due to the overhead of function calls and maintaining the call stack.(slows down)
Deep recursive calls can lead to stack overflow errors, especially for languages with limited stack space.
