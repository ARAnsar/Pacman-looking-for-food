from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Image

window = Tk()
window.geometry("1000x300")
window.configure(bg = "#FFFFFF")
canvas = Canvas(window,bg = "#FFFFFF",height = 300,width = 1000,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

#algorithm selection
button_image_BFS = PhotoImage(file="assets/frame0/BFS.png")
button_BFS = Button(image=button_image_BFS,borderwidth=0,highlightthickness=0,command=lambda: print("BFS"),relief="flat")
button_BFS.place(x=800.0,y=147.0,width=60.0,height=36.0)

button_image_DFS = PhotoImage(file="assets/frame0/DFS.png")
button_DFS = Button(image=button_image_DFS,borderwidth=0,highlightthickness=0,command=lambda: print("button_2 clicked"),relief="flat")
button_DFS.place(x=800.0,y=193.0,width=60.0,height=36.0)

button_image_A = PhotoImage(file="assets/frame0/A.png")
button_A = Button(image=button_image_A,borderwidth=0,highlightthickness=0,command=lambda: print("button_3 clicked"),relief="flat")
button_A.place(x=800.0,y=239.0,width=60.0,height=36.0)

#run button
button_image_RUN = PhotoImage(file="assets/frame0/RUN.png")
button_RUN= Button(image=button_image_RUN,borderwidth=0,highlightthickness=0,command=lambda: print("button_4 clicked"),relief="flat")
button_RUN.place(x=867.0,y=239.0,width=122.0,height=36.0)

#ENTER POSITION OF FOOD AND PACMAN 
canvas.create_text(896.0,26.0,anchor="nw",text="X",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(948.0,26.0,anchor="nw",text="Y",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(827.0,105.0,anchor="nw",text="FOOD:",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(805.0,59.0,anchor="nw",text="PACMAN:",fill="#000000",font=("Inter", 14 * -1))

food_x_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
food_x_entry.place(x=889.0,y=95.0,width=30,height=30)
food_y_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
food_y_entry.place(x=941.0,y=95.0,width=30,height=30)

pacman_x_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
pacman_x_entry.place(x=889.0,y=49.0,width=30,height=30)
pacman_y_entry = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
pacman_y_entry.place(x=941.0,y=49.0,width=30,height=30)

#result
canvas.create_text(872.0,157.0,anchor="nw",text="Time ",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(931.0,157.0,anchor="nw",text="33ms",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(870.0,203.0,anchor="nw",text="Nodes",fill="#000000",font=("Inter", 14 * -1))
canvas.create_text(951.0,202.0,anchor="nw",text="50",fill="#000000",font=("Inter", 14 * -1))

window.resizable(False, False)
window.mainloop()