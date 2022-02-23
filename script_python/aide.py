import tkinter as root

menuBar = Menu(root)
root['menu'] = menuBar
sousMenu = Menu(menuBar)
menuBar.add_cascade(label='Aide', menu=sousMenu)
sousMenu.add_command(label='À propos', command=aproposGest)