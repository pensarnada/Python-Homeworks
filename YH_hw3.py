"""

Expectation and explanation of the homework :

You are expected to write a Python program for a single player game: Ball Crush.
There is a 5 × 5 game board. At the beginning of the game, 3 balls are inserted to the board at
random. The aim is to crush all but one ball on the board, and inform the player about how
much time he/she spends.
The rules of the game are specified below:
● At each step, the board and positions of the balls are displayed.
● The player first chooses one of the balls by typing its x and y positions. Then, the
valid directions for the selected ball are displayed, and the program asks the player for
a move.
● A direction (“w”, “a”, “s”, and “d”) is valid if there is no wall in that direction.
● After the player types a direction, the ball is moved to the entered direction. If there is
already a ball at the destination position, the moving ball is crushed (and deleted from
the board).
● The board and positions of the balls are updated.
● When only one ball is left, the game ends, “Game Over!” and the elapsed time are
printed.
Functions:
The required functions’ names and tasks are given. You will fill these functions, and will not
implement additional functions.
display_board(board): The board is printed.
display_ball_positions(ball_positions): The positions of the balls are printed.
choose_ball(board): A ball is chosen from the given board by entering its x and y positions.
get_valid_moves(pos, len_board): The valid moves are returned according to the position of
the selected ball and length of the board.
make_move(board, pos, valid_moves, ball_positions): The direction is taken from the
player, the board and ball_positions are updated by taking into account a collision situation.
delete_ball(board, pos, ball_positions): The ball is deleted from the board and
ball_positions.
check_collision(board, pos): It checks whether there is a collision or not.
main(): This part is already implemented! (See HW3_base.py)
Important Notes:
● Be careful about invalid inputs! Ask each question again until a valid input is entered.
● Do not modify the given code . Insert your code to the indicated section.


"""

# Yusuf HAYIRLI

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Ball Crush

from random import randint
import time

# INSERT YOUR CODE HERE ...

def check_collision(board, ball_positions):
    x=False
    if len(ball_positions) != len(set(ball_positions)):
        x=True #If list != unique list
    return x
def delete_ball(board, ball_pos, ball_positions):
    ball_positions.remove(ball_positions[ball_positions.index(ball_pos)])
    for pos in ball_positions:
        board[pos[0]][pos[1]] = 1
    return ball_positions
def display_ball_positions(ball_positions):
    temp_positions=[] # Temporary list for indexes + 1 
    for i in range(len(ball_positions)):
        temp_positions.append((ball_positions[i][0]+1,ball_positions[i][1]+1))
    print(temp_positions)
def display_board(board):
    for i in board: # Displays board as matrix order
        print(i)
def choose_ball(board): 
    index_list=[] # Temporary list for ball_positions from board
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==1:
                index_list.append((row+1,col+1))
    while True: # For valid input
        x=input("Which ball? ")
        if len(x)==3:
            if x[0].isnumeric() and x[2].isnumeric():
                x=(int(x[0]),int(x[2]))
                if x not in index_list:
                    print("It is not a ball position.")
                    continue
        else:
            print("It is not a ball position.")
            continue
        return x
def get_valid_moves(ball_pos, len_board):
    valid_move_list=["w","a","s","d"] # default list for non max or min values.
    max_len=len_board
    min_len=1
    if ball_pos[0]==min_len:
        valid_move_list.remove("w")
    if ball_pos[0]==max_len:
        valid_move_list.remove("s")
    if ball_pos[1]==min_len:
        valid_move_list.remove("a")
    if ball_pos[1]==max_len:
        valid_move_list.remove("d")
    return valid_move_list

def make_move(board, ball_pos, valid_moves, ball_positions):
    while True: # For valid input
        x=input("Your move? ")
        if x not in valid_moves:
            print("Enter a valid direction!")
            continue
        else:
            break
    temp_positions=[] # Temporary list for indexes + 1 
    for i in range(len(ball_positions)):
        temp_positions.append((ball_positions[i][0]+1,ball_positions[i][1]+1))
    if x=="w":
        temp_pos=(ball_pos[0]-1,ball_pos[1]) # ball moves up if "w"
    elif x=="a":
        temp_pos=(ball_pos[0],ball_pos[1]-1) # ball moves left if "a"
    elif x=="s":
        temp_pos=(ball_pos[0]+1,ball_pos[1]) # ball moves down if "s"
    elif x=="d":
        temp_pos=(ball_pos[0],ball_pos[1]+1) # ball moves right if "d"
    temp_positions[temp_positions.index(ball_pos)]=(temp_pos[0],temp_pos[1])
    for i in range(len(ball_positions)):
        ball_positions[i]=((temp_positions[i][0]-1,temp_positions[i][1]-1)) 
    board[ball_pos[0]-1][ball_pos[1]-1]=0 # remove the previous position
    for pos in ball_positions: # fill the board again with ball_positions' indexes
        board[pos[0]][pos[1]] = 1
    if check_collision(board, ball_positions)==True:
        board[ball_pos[0]-1][ball_pos[1]-1]=0
        ball_positions=delete_ball(board, pos, ball_positions)
"""
The part until here is coded by me.

The part below here is not coded by me, this is given part in the homework, you can see it in explanation.
"""
def main():
    len_board = 5
    board = [[0 for col in range(len_board)] for row in range(len_board)]  
 
    while True:
        ball_positions = [(randint(0, len_board-1), randint(0, len_board-1)) for i in range(3)]
        if len(ball_positions) == len(set(ball_positions)):
            break
    
    for pos in ball_positions:
        board[pos[0]][pos[1]] = 1

    start_time = time.time()
    
    while True:
        display_ball_positions(ball_positions)
        display_board(board)
        
        if len(ball_positions) == 1:
            break
        
        ball_pos = choose_ball(board)
        
        valid_moves = get_valid_moves(ball_pos, len(board))
        print("Valid moves:", valid_moves)
        
        make_move(board, ball_pos, valid_moves, ball_positions)
        
    end_time = time.time()

    minutes, seconds = divmod(end_time-start_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Game Over!")
    print("Passed time= {:02d}:{:02d}:{:02d}".format(int(hours), int(minutes),int(seconds)))
    
main()

