from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Image
import map_generator
import searching_algorithm
import time as t

window = Tk()
window.geometry("1100x420")
window.configure(bg = "#FFFFFF")
canvas = Canvas(window,bg = "#FFFFFF",height = 420,width = 1100,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#mission complete
def change_color():
    #change color
    colors = list(searching_algorithm.cell_list.values())
    for i in range(0,98):
        canvas.itemconfig(cell_list_c[i] , fill = colors[i][0])
        canvas.itemconfig(cell_list_n[i] , text = str(colors[i][1]))
    canvas.itemconfig(cell_list_c[int(food_x_entry.get())*14+int(food_y_entry.get())] , fill = 'blue')
    canvas.itemconfig(cell_list_c[int(pacman_x_entry.get())*14+int(pacman_y_entry.get())] , fill = 'yellow')
    #calcute time and chek node
    canvas.itemconfig(nodes, text =str(searching_algorithm.checked))
    canvas.itemconfig(time, text =str(1000*(searching_algorithm.end - searching_algorithm.start)))
    return

#generate map
cell_list_c = []
cell_list_n = []
for i in range(0,98):
    if map_generator.map[i] == 0:
        cell_list_c.append(canvas.create_rectangle(10+(i%14)*60, 
                                                10+(i//14)*60,
                                                50+(i%14)*60,
                                                50+(i//14)*60,fill="black",outline=""))
    else:
        cell_list_c.append(canvas.create_rectangle(10+(i%14)*60, 
                                                10+(i//14)*60,
                                                50+(i%14)*60,
                                                50+(i//14)*60,fill="white",outline=""))
    cell_list_n.append(canvas.create_text(40+(i%14)*60, 
                        40+(i//14)*60,                           
                        text='',fill="#000000",font=("Inter", 14 * -1)))
    
#algorithm selection
button_image_BFS = PhotoImage(file="build/assets/frame0/BFS.png")
button_BFS = Button(image=button_image_BFS,borderwidth=0,highlightthickness=0,
                    command=lambda: searching_algorithm.runb(int(food_x_entry.get()),
                                                             int(food_y_entry.get()),
                                                             int(pacman_x_entry.get()),
                                                             int(pacman_y_entry.get()),
                                                             'BFS'),
                    relief="flat")
button_BFS.place(x=800 + 75,y=147 + 50,width=60.0,height=36.0)

button_image_DFS = PhotoImage(file="build/assets/frame0/DFS.png")
button_DFS = Button(image=button_image_DFS,borderwidth=0,highlightthickness=0,
                    command=lambda: searching_algorithm.runb(int(food_x_entry.get()),
                                                             int(food_y_entry.get()),
                                                             int(pacman_x_entry.get()),
                                                             int(pacman_y_entry.get()),
                                                             'DFS'),
                    relief="flat")
button_DFS.place(x=800 + 75,y=193.0 + 50,width=60.0,height=36.0)

button_image_A = PhotoImage(file="build/assets/frame0/A.png")
button_A = Button(image=button_image_A,borderwidth=0,highlightthickness=0,
                  command=lambda: searching_algorithm.runb(3,3,1,1,'A'),
                  relief="flat")
button_A.place(x=800 + 75 ,y=239 + 50,width=60.0,height=36.0)

#run button
button_image_RUN = PhotoImage(file="build/assets/frame0/RUN.png")
button_RUN= Button(image=button_image_RUN,
                   borderwidth=0,
                   highlightthickness=0,
                   command=lambda: change_color()
                   ,relief="flat")
button_RUN.place(x=867.0 + 75,y=239.0 + 50,width=122.0,height=36.0)

#ENTER POSITION OF FOOD AND PACMAN 
canvas.create_text(896 + 75,26 + 50,anchor="nw",text="X",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(948 + 75,26 + 50,anchor="nw",text="Y",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(827 + 75,106 + 50,anchor="nw",text="FOOD:",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(805 + 75,59 + 50,anchor="nw",text="PACMAN:",fill="#000000",font=("Inter", 14 * -1))

food_x_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
food_x_entry.place(x=889 + 75,y=95.0  + 50,width=30,height=30)
food_y_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
food_y_entry.place(x=941 + 75,y=95.0  + 50,width=30,height=30)

pacman_x_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
pacman_x_entry.place(x=889 + 75,y=49.0 + 50,width=30,height=30)
pacman_y_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
pacman_y_entry.place(x=941 + 75,y=49.0 + 50,width=30,height=30)

#result
canvas.create_text(872 + 75,157 + 50,anchor="nw",text="Time ",fill="#000000",font=("Inter", 14 * -1))
time = canvas.create_text(931 + 75,157 + 50,anchor="nw",text="",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(870 + 75,203 + 50,anchor="nw",text="Nodes",fill="#000000",font=("Inter", 14 * -1))
nodes = canvas.create_text(951 + 75,202 + 50,anchor="nw",text="",fill="#000000",font=("Inter", 14 * -1))

window.resizable(False, False)
window.mainloop()