import tkinter as tk


def RUN_button(PACMAN_position_x, PACMAN_position_y, FOOD_position_x, FOOD_position_y):
	print(PACMAN_position_x.get() )
def radio_func():
	print('hi')
	
#basic info of plot	
root = tk.Tk()
root.geometry('800x600')
root.title('Pacman looking for food')
root.resizable(0, 0)
root.iconbitmap('assets/pacman.ico')

radio_string = tk.StringVar()
exercise_radio1 = tk.Radiobutton(
	root, 
	text = 'Radio A', 
	value = 'A', 
	command = radio_func, 
	variable = radio_string)
exercise_radio2 = tk.Radiobutton(
	root, 
	text = 'Radio B', 
	value = 'B', 
	command = radio_func, 
	variable = radio_string)
exercise_radio1.pack()
exercise_radio2.pack()

#PACMAN_position_x entry
PACMAN_position_x = tk.StringVar(value = 'PACMAN x')
entry = tk.Entry(root, textvariable = PACMAN_position_x)
entry.pack()
#PACMAN_position_y entry
PACMAN_position_y = tk.StringVar(value = 'PACMAN y')
entry = tk.Entry(root, textvariable = PACMAN_position_y)
entry.pack()

#FOOD_position_x entry
FOOD_position_x = tk.StringVar(value = 'FOOD x')
entry = tk.Entry(root, textvariable = FOOD_position_x)
entry.pack()
#FOOD_position_y entry
FOOD_position_y = tk.StringVar(value = 'FOOD y')
entry = tk.Entry(root, textvariable = FOOD_position_y)
entry.pack()


button = tk.Button(root , text = 'RUN', command = lambda:RUN_button(PACMAN_position_x, PACMAN_position_y, FOOD_position_x, FOOD_position_y) , width = 10 )
button.pack()


root.mainloop()
