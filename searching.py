#PACMAN_position_x , PACMAN_position_y
#FOOD_position_x , FOOD_position_y
#cell_list format: [ [ x , y ] : [ color /white/black/green/red/ , turn /None/number/ ] ]
'''dont forget:
        calcute all cell checked
        set dictionary format for if
        when you want call bfs first you should append position to queue
'''
def RUN(food_x_entry ,food_y_entry,pacman_x_entry,pacman_y_entry,algorithm_name):
    global FOOD_position_x,FOOD_position_y,cell_list,turn,checked,q
    FOOD_position_x = food_x_entry 
    FOOD_position_y = food_y_entry 
    cell_list = []
    turn = 0
    checked = 0
    #BFS queue 
    q = [[pacman_x_entry,pacman_y_entry]]
    if algorithm_name == "DFS":
        DFS(pacman_x_entry,pacman_y_entry)
    elif algorithm_name == "BFS":
        BFS(pacman_x_entry,pacman_y_entry)
    elif algorithm_name == "A":
        A(pacman_x_entry,pacman_y_entry)

def DFS(PACMAN_position_x , PACMAN_position_y):
    #check final 
    if PACMAN_position_x == FOOD_position_x  and PACMAN_position_y  == FOOD_position_y :
        raise 'Food found!'
    
    #check up
    checked = checked + 1
    if cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y] = ['green' , turn]
        DFS(PACMAN_position_x  , PACMAN_position_y + 1 )

    elif (cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['black', None] or 
          cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['red', None]):
        cell_list[PACMAN_position_x , PACMAN_position_y + 1] = ['red' , None]


    #check right
    checked = checked + 1
    if cell_list[PACMAN_position_x + 1 , PACMAN_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y] = ['green' , turn]
        DFS(PACMAN_position_x + 1  , PACMAN_position_y )

    elif (cell_list[PACMAN_position_x + 1, PACMAN_position_y] == ['black', None] or 
          cell_list[PACMAN_position_x + 1, PACMAN_position_y] == ['red', None]):
        cell_list[PACMAN_position_x + 1 , PACMAN_position_y] = ['red' , None]

    #check down
    checked = checked + 1
    if cell_list[PACMAN_position_x , PACMAN_position_y- 1] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y] = ['green' , turn]
        DFS(PACMAN_position_x  , PACMAN_position_y - 1 )

    elif (cell_list[PACMAN_position_x , PACMAN_position_y- 1] == ['black', None] or 
          cell_list[PACMAN_position_x , PACMAN_position_y- 1] == ['red', None]):
        cell_list[PACMAN_position_x , PACMAN_position_y - 1] = ['red' , None]

    #check left
    checked = checked + 1
    if cell_list[PACMAN_position_x-1 , PACMAN_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y] = ['green' , turn]
        DFS(PACMAN_position_x - 1  , PACMAN_position_y )

    elif (cell_list[PACMAN_position_x - 1 , PACMAN_position_y] == ['black', None] or 
          cell_list[PACMAN_position_x - 1 , PACMAN_position_y] == ['red', None]):
        cell_list[PACMAN_position_x - 1, PACMAN_position_y] = ['red' , None]  

    #no way
    raise 'there is no way to food'

def BFS(PACMAN_position_x , PACMAN_position_y):

    if checked > 0 and not q:
        raise 'there is no way to food'
    if PACMAN_position_x == FOOD_position_x  and PACMAN_position_y  == FOOD_position_y :
        raise 'Food found!'
    
    #check up
    checked = checked + 1
    if cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y + 1 ] = ['green' , turn]
        q.append([PACMAN_position_x,PACMAN_position_y  + 1])
    elif (cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['black', None] or 
          cell_list[PACMAN_position_x , PACMAN_position_y + 1] == ['red', None]):
        cell_list[PACMAN_position_x , PACMAN_position_y + 1] = ['red' , None]

    #check right
    checked = checked + 1
    if cell_list[PACMAN_position_x + 1 , PACMAN_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x + 1 , PACMAN_position_y] = ['green' , turn]
        q.append([PACMAN_position_x + 1,PACMAN_position_y])
    elif (cell_list[PACMAN_position_x + 1 , PACMAN_position_y] == ['black', None] or 
          cell_list[PACMAN_position_x + 1 , PACMAN_position_y] == ['red', None]):
        cell_list[PACMAN_position_x + 1 , PACMAN_position_y] = ['red' , None]

    #check up
    checked = checked + 1
    if cell_list[PACMAN_position_x , PACMAN_position_y - 1] == ['white', None]:
        turn = turn + 1
        cell_list[PACMAN_position_x , PACMAN_position_y - 1 ] = ['green' , turn]
        q.append([PACMAN_position_x,PACMAN_position_y  - 1])
    elif (cell_list[PACMAN_position_x , PACMAN_position_y - 1] == ['black', None] or 
          cell_list[PACMAN_position_x , PACMAN_position_y - 1] == ['red', None]):
        cell_list[PACMAN_position_x , PACMAN_position_y - 1] = ['red' , None]

    #check left
    checked = checked + 1
    if cell_list[PACMAN_position_x - 1 , PACMAN_position_y] == ['white', None]:
        turn = turn - 1
        cell_list[PACMAN_position_x  - 1 , PACMAN_position_y] = ['green' , turn]
        q.append([PACMAN_position_x,PACMAN_position_y])
    elif (cell_list[PACMAN_position_x - 1 , PACMAN_position_y] == ['black', None] or 
          cell_list[PACMAN_position_x - 1 , PACMAN_position_y] == ['red', None]):
        cell_list[PACMAN_position_x - 1 , PACMAN_position_y] = ['red' , None]

    BFS(q.popleft()[0],q.popleft()[1])
    
    return
    
def A():
    return
    

