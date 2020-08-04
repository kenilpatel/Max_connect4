# Max_connect4

Artificial intelligence based two player interactive game 

There are total two modes in the game one is interactive and the other one is one move mode 

Interactive Mode

In the interactive mode, the game should run from the command line with
the following arguments (assuming a Java implementation, with obvious
changes for C++ or other implementations):

python maxconnect4.py interactive [input_file] [computer-next/human-next]

Argument interactive specifies that the program runs in interactive mode.
  
Argument [input_file] specifies an input file that contains an initial board state. This way we can start the program from a non-empty board state. If the input file does not exist, the program should just create an empty board state and start again from there.

Argument [computer-first/human-first] specifies whether the computer should make the next move or the human.  

Argument [depth] specifies the number of moves in advance that the computer should consider while searching for its next move. In other words, this argument specifies the depth of the search tree.Essentially, this argument will control the time takes for the computer to make a move.

After reading the input file, the program gets into the following loop:


  1) If computer-next, goto 2, else goto 5.
  2) Print the current board state and score. If the board is full, exit.
  3) Choose and make the next move.
  4) Save the current board state in a file called computer.txt(in same format as input file).
  5) Print the current board state and score. If the board is full, exit.
  6) Ask the human user to make a move (make sure that the move is valid, otherwise repeat request to the user).
  7) Save the current board state in a file called human.txt (in same format as input file).</li>
  8) Goto 2.
  
One-Move Mode
  
The purpose of the one-move mode is to make it easy for programs to compete against each other, and communicate their moves to each other using text files. The one-move mode is invoked as follows:

python maxconnect4.py one-move [input_file] [output_file] [depth]

In this case, the program simply makes a single move and terminates. In particular, the program should:

  1) Read the input file and initialize the board state and current score, as in interactive mode.
  2) Print the current board state and score. If the board is full, exit.
  3) Choose and make the next move.
  4) Print the current board state and score.
  5) Save the current board state to the output file IN EXACTLY THE SAME FORMAT THAT IS USED FOR INPUT FILES.
  6) Exit
  
0 stands for an empty spot, a 1 stands for a piece played by the first player, and a 2 stands for a piece played by the second player. The last number in the input file indicates which player plays NEXT (and NOT which player played last).
