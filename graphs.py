import matplotlib as plt
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Graph Program")
mainWindow.geometry("700x700")
mainWindow.configure(background = "ghost white")

titleLabel = tk.Label(mainWindow, text= "Welcome to the Python Graph Plotter!", bg="ghost white", fg="black", font=("Arial",20))
welcomeLabel = tk.Label(mainWindow, text="Enter the values you wish to plot in the text entry box below (x values\nthen y values next to them. Separate each value with one (1)\nsingle space).", bg="ghost white", fg="black", font=("Arial",15))

#placing elements
titleLabel.pack()
welcomeLabel.pack()

mainWindow.mainloop()