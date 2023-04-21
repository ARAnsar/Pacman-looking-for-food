map = [1 , 1 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 ,
       1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 0 ,
       1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ,
       1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 ,
       1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 ,
      ]
cell_list = []
for i in range(0,len(map)+1):
      if i == 0:
            cell_list.append([i//10,i%10,'black'])   
      else:
            cell_list.append([i//10,i%10,'white']) 
      