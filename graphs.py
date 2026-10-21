import matplotlib as plt
import tkinter as tk

#making the main window
mainWindow = tk.Tk()
mainWindow.title("Graph Program")
mainWindow.geometry("600x700")
mainWindow.configure(background = "ghost white")


#labels
titleLabel = tk.Label(mainWindow, text= "Welcome to the Python Graph Plotter!", bg="ghost white", fg="black", font=("Arial",20), justify="center")

welcomeLabel = tk.Label(mainWindow, text="Enter the values you wish to plot in each of the text entry\nbox below (Separate each value with one (1)\nsingle space).", bg="ghost white", fg="black", font=("Arial",15))

xLabel = tk.Label(mainWindow, text="X:",bg="ghost white",fg="black",font=("Arial",20))

yLabel = tk.Label(mainWindow, text="Y:",bg="ghost white",fg="black",font=("Arial",20))

#entry boxes
xEntryBox = tk.Entry(mainWindow, width=20, font=("Arial",20))

yEntryBox = tk.Entry(mainWindow, width=20, font=("Arial",20))

#placing elements
titleLabel.grid(row=0,column=1)
welcomeLabel.grid(row=1,column=1)
xEntryBox.grid(row=2,column=1)
yEntryBox.grid(row=3,column=1,pady=10)
xLabel.grid(row=2,column=0)
yLabel.grid(row=3,column=0,pady=10)

mainWindow.mainloop()