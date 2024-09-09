#8 puzzle problem using A* Seach

board = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
hn = {
    '1': {'goal_pos': (0, 0)},
    '2': {'goal_pos': (0, 1)},
    '3': {'goal_pos': (0, 2)},
    '4': {'goal_pos': (2, 2)},
    '5': {'goal_pos': (1, 0)},
    '6': {'goal_pos': (1, 2)},
    '7': {'goal_pos': (2, 1)},
    '8': {'goal_pos': (1, 1)},
    '0': {'goal_pos': (2, 0)}
}
def difference(goal, cur):
    return abs(goal[0]- cur[0]) + abs(goal[1] - cur[1])

def puzzle():
    queue=[]
    x_blank,y_blank=return_current_position(0)
    for key in hn:
        if key=='0':
            continue
        x, y = return_current_position(int(key))
        if hn[key]['goal_pos'] != (x, y):
           sp_dist=difference((x_blank,y_blank),(x,y))
           queue.append((key,sp_dist))
    if len(queue)!=0:
         queue.sort(key=lambda x: x[1])
         sorting_puzzle(queue) 
    else:
        print('Puzzle Solved')
        for row in board:
            for col in row:
                print(col,end=" ")
            print()    

def sorting_puzzle(queue):
    while queue:
        state,d=queue.pop(0)
        x_blank,y_blank=return_current_position(0)
        x,y=return_current_position(int(state))
        if difference((x,y),(x_blank,y_blank))==1:
            temp=board[x][y]
            board[x][y]=board[x_blank][y_blank]
            board[x_blank][y_blank]=temp
    puzzle()

def return_current_position(state):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == state:
                return i, j
# --------------------------------------------------------------------------------------------
print("PUZZLE")
for row in board:
    for col in row:
        print(col,end=" ")
    print() 
puzzle()
