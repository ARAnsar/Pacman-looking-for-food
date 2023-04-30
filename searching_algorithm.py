import map_generator
import time as t
#cell_list format: [ [ x , y ] : [ color /white/black/green/red/ , turn /''/number/ ] ]

def runb(food_x_entry ,food_y_entry,pacman_x_entry,pacman_y_entry,algorithm_name):
    global FOOD_position_x,FOOD_position_y,cell_list,turn,checked,q,start
    start = t.time()
    FOOD_position_x = food_x_entry 
    FOOD_position_y = food_y_entry 
    cell_list = map_generator.cell_list()
    turn = 0
    checked = 0
    #BFS queue 
    q = []
    if algorithm_name == "DFS":
        DFS(pacman_x_entry,pacman_y_entry)
        end = t.time()
        #no way
        raise 'there is no way to food'
    elif algorithm_name == "BFS":
        BFS(pacman_x_entry,pacman_y_entry)
        end = t.time()
        #no way
        raise 'there is no way to food'

def DFS(PACMAN_position_x , PACMAN_position_y):
    global FOOD_position_x,FOOD_position_y,cell_list,turn,checked,q,end
    #check final 
    if PACMAN_position_x == FOOD_position_x  and PACMAN_position_y  == FOOD_position_y :
        raise 'Food found!'
    
    #check right
    checked = checked + 1
    if cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y)] = ['green' , turn]
        DFS(PACMAN_position_x  , PACMAN_position_y + 1 )

    elif (cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['black', ''] or 
          cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['red', '']):
        cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] = ['red' , '']

    #check down
    checked = checked + 1
    if cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y)] = ['green' , turn]
        DFS(PACMAN_position_x + 1  , PACMAN_position_y )

    elif (cell_list[(PACMAN_position_x + 1, PACMAN_position_y)] == ['black', ''] or 
          cell_list[(PACMAN_position_x + 1, PACMAN_position_y)] == ['red', '']):
        cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] = ['red' , '']
    
    #check left
    checked = checked + 1
    if cell_list[(PACMAN_position_x , PACMAN_position_y- 1)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y)] = ['green' , turn]
        DFS(PACMAN_position_x  , PACMAN_position_y - 1 )

    elif (cell_list[(PACMAN_position_x , PACMAN_position_y- 1)] == ['black', ''] or 
          cell_list[(PACMAN_position_x , PACMAN_position_y- 1)] == ['red', '']):
        cell_list[(PACMAN_position_x , PACMAN_position_y - 1)] = ['red' , '']
    
    #check up
    checked = checked + 1
    if cell_list[(PACMAN_position_x-1 , PACMAN_position_y)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y)] = ['green' , turn]
        DFS(PACMAN_position_x - 1  , PACMAN_position_y )

    elif (cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] == ['black', ''] or 
          cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] == ['red', '']):
        cell_list[(PACMAN_position_x - 1, PACMAN_position_y)] = ['red' , '']

    if cell_list[(PACMAN_position_x , PACMAN_position_y)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y)] = ['green' , turn]
    return
    

def BFS(PACMAN_position_x , PACMAN_position_y):
    global FOOD_position_x,FOOD_position_y,cell_list,turn,checked,q,end

    if PACMAN_position_x == FOOD_position_x  and PACMAN_position_y  == FOOD_position_y :
        end = t.time()
        raise 'Food found!'
    
    #check right
    checked = checked + 1
    if cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y + 1) ] = ['green' , turn]
        q.append([PACMAN_position_x,PACMAN_position_y  + 1])
    elif (cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['black', ''] or 
          cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] == ['red', '']):
        cell_list[(PACMAN_position_x , PACMAN_position_y + 1)] = ['red' , '']

    #check down
    checked = checked + 1
    if cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] = ['green' , turn]
        q.append([PACMAN_position_x + 1,PACMAN_position_y])
    elif (cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] == ['black', ''] or 
          cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] == ['red', '']):
        cell_list[(PACMAN_position_x + 1 , PACMAN_position_y)] = ['red' , '']

    #check left
    checked = checked + 1
    if cell_list[(PACMAN_position_x , PACMAN_position_y - 1)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x , PACMAN_position_y - 1) ] = ['green' , turn]
        q.append([PACMAN_position_x,PACMAN_position_y  - 1])
    elif (cell_list[(PACMAN_position_x , PACMAN_position_y - 1)] == ['black', ''] or 
          cell_list[(PACMAN_position_x , PACMAN_position_y - 1)] == ['red', '']):
        cell_list[(PACMAN_position_x , PACMAN_position_y - 1)] = ['red' , '']

    #check up
    checked = checked + 1
    if cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] == ['white', '']:
        turn = turn + 1
        cell_list[(PACMAN_position_x  - 1 , PACMAN_position_y)] = ['green' , turn]
        q.append([PACMAN_position_x - 1,PACMAN_position_y])
    elif (cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] == ['black', ''] or 
          cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] == ['red', '']):
        cell_list[(PACMAN_position_x - 1 , PACMAN_position_y)] = ['red' , '']
    firsoflist = q.pop()
    BFS(firsoflist[0],firsoflist[1])
    
    return
    
