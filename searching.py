#starting_position_x , starting_position_y
#final_position_x , final_position_y
#cell_list format: [ [ x , y ] : [ color /white/black/green/red/ , turn /None/number/ ] ]
'''dont forget:
        calcute all cell checked
        set dictionary format for if
        when you want call bfs first you should append position to queue
'''
final_position_x = 0 
final_position_y = 0
cell_list = []
turn = 0
checked = 0
#BFS queue 
starting_position_x = 0
starting_position_y = 0
q = [[starting_position_x , starting_position_y]]

def DFS(starting_position_x , starting_position_y):
    #check final 
    if starting_position_x == final_position_x  and starting_position_y  == final_position_y :
        raise 'Food found!'
    
    #check up
    checked = checked + 1
    if cell_list[starting_position_x , starting_position_y + 1] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y] = ['green' , turn]
        DFS(starting_position_x  , starting_position_y + 1 )

    elif (cell_list[starting_position_x , starting_position_y + 1] == ['black', None] or 
          cell_list[starting_position_x , starting_position_y + 1] == ['red', None]):
        cell_list[starting_position_x , starting_position_y + 1] = ['red' , None]


    #check right
    checked = checked + 1
    if cell_list[starting_position_x + 1 , starting_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y] = ['green' , turn]
        DFS(starting_position_x + 1  , starting_position_y )

    elif (cell_list[starting_position_x + 1, starting_position_y] == ['black', None] or 
          cell_list[starting_position_x + 1, starting_position_y] == ['red', None]):
        cell_list[starting_position_x + 1 , starting_position_y] = ['red' , None]

    #check down
    checked = checked + 1
    if cell_list[starting_position_x , starting_position_y- 1] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y] = ['green' , turn]
        DFS(starting_position_x  , starting_position_y - 1 )

    elif (cell_list[starting_position_x , starting_position_y- 1] == ['black', None] or 
          cell_list[starting_position_x , starting_position_y- 1] == ['red', None]):
        cell_list[starting_position_x , starting_position_y - 1] = ['red' , None]

    #check left
    checked = checked + 1
    if cell_list[starting_position_x-1 , starting_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y] = ['green' , turn]
        DFS(starting_position_x - 1  , starting_position_y )

    elif (cell_list[starting_position_x - 1 , starting_position_y] == ['black', None] or 
          cell_list[starting_position_x - 1 , starting_position_y] == ['red', None]):
        cell_list[starting_position_x - 1, starting_position_y] = ['red' , None]  

    #no way
    raise 'there is no way to food'

def BFS(starting_position_x , starting_position_y):

    if checked > 0 and not q:
        raise 'there is no way to food'
    if starting_position_x == final_position_x  and starting_position_y  == final_position_y :
        raise 'Food found!'
    
    #check up
    checked = checked + 1
    if cell_list[starting_position_x , starting_position_y + 1] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y + 1 ] = ['green' , turn]
        q.append([starting_position_x,starting_position_y  + 1])
    elif (cell_list[starting_position_x , starting_position_y + 1] == ['black', None] or 
          cell_list[starting_position_x , starting_position_y + 1] == ['red', None]):
        cell_list[starting_position_x , starting_position_y + 1] = ['red' , None]

    #check right
    checked = checked + 1
    if cell_list[starting_position_x + 1 , starting_position_y] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x + 1 , starting_position_y] = ['green' , turn]
        q.append([starting_position_x + 1,starting_position_y])
    elif (cell_list[starting_position_x + 1 , starting_position_y] == ['black', None] or 
          cell_list[starting_position_x + 1 , starting_position_y] == ['red', None]):
        cell_list[starting_position_x + 1 , starting_position_y] = ['red' , None]

    #check up
    checked = checked + 1
    if cell_list[starting_position_x , starting_position_y - 1] == ['white', None]:
        turn = turn + 1
        cell_list[starting_position_x , starting_position_y - 1 ] = ['green' , turn]
        q.append([starting_position_x,starting_position_y  - 1])
    elif (cell_list[starting_position_x , starting_position_y - 1] == ['black', None] or 
          cell_list[starting_position_x , starting_position_y - 1] == ['red', None]):
        cell_list[starting_position_x , starting_position_y - 1] = ['red' , None]

    #check left
    checked = checked + 1
    if cell_list[starting_position_x - 1 , starting_position_y] == ['white', None]:
        turn = turn - 1
        cell_list[starting_position_x  - 1 , starting_position_y] = ['green' , turn]
        q.append([starting_position_x,starting_position_y])
    elif (cell_list[starting_position_x - 1 , starting_position_y] == ['black', None] or 
          cell_list[starting_position_x - 1 , starting_position_y] == ['red', None]):
        cell_list[starting_position_x - 1 , starting_position_y] = ['red' , None]

    BFS(q.popleft()[0],q.popleft()[1])
    
    return
    

    

