################## ----------------🙃 Cool TextEditor 🙃----------------------##################

######### limitations : TODO
#
# 
# 
#
##########################################################################################################


import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

mainApplication = tk.Tk()
mainApplication.geometry("1200x800")
mainApplication.title("My Editor")


def action():
    pass

######################################     Main  Menu   ###################################################

###### Main menu :

mainMenu = tk.Menu()                            # mainMenu = tk.Menu(mainApplication)

###### submenu :

file = tk.Menu(mainMenu,tearoff=False) 
edit = tk.Menu(mainMenu,tearoff=False) 
view = tk.Menu(mainMenu,tearoff=False) 
ColourTheme = tk.Menu(mainMenu,tearoff=False) 

###### cascade :

### File :

# icons :

newIcon = tk.PhotoImage(file='icons2/new.png')
openIcon = tk.PhotoImage(file='icons2/open.png')
saveIcon = tk.PhotoImage(file='icons2/save.png')
save_asIcon = tk.PhotoImage(file='icons2/save_as.png')
exitIcon = tk.PhotoImage(file='icons2/exit.png')


mainMenu.add_cascade(label="File",menu=file)


### Edit :

# icons :

copyIcon = tk.PhotoImage(file='icons2/copy.png')
cutIcon = tk.PhotoImage(file='icons2/cut.png')
pasteIcon = tk.PhotoImage(file='icons2/paste.png')
clear_allIcon = tk.PhotoImage(file='icons2/clear_all.png')
findIcon = tk.PhotoImage(file='icons2/find.png')


mainMenu.add_cascade(label="Edit",menu=edit)



### View :

# icons :

toolBarIcon = tk.PhotoImage(file='icons2/tool_bar.png')
statusBarIcon = tk.PhotoImage(file='icons2/status_bar.png')


mainMenu.add_cascade(label="View",menu=view)



### Colour Theme :

# icons 

lightDefaultIcon = tk.PhotoImage(file='icons2/light_default.png')
lightPlusIcon = tk.PhotoImage(file='icons2/light_plus.png')
darkIcon = tk.PhotoImage(file='icons2/dark.png')
redIcon = tk.PhotoImage(file='icons2/red.png')
monokaiIcon = tk.PhotoImage(file='icons2/monokai.png')
nightBlueIcon = tk.PhotoImage(file='icons2/night_blue.png')

mainMenu.add_cascade(label="Colour Theme",menu=ColourTheme)

themeChosen = tk.StringVar()
colourIcons = (lightDefaultIcon,lightPlusIcon,darkIcon,redIcon,monokaiIcon,nightBlueIcon)

colourDict = {
    'Light Default' : ('#000000','#ffffff'),      # background and font
    'Light Plus' : ('#474747','#e0e0e0'), 
    'Dark' : ('#c4c4c4','#2d2d2d'), 
    'Red' : ('#2d2d2d','#ffe8e8'), 
    'Monokai' : ('#d3b774','#474747'), 
    'Night Blue' : ('#ededed','#6b9dc2')
}








mainApplication.config(menu = mainMenu)

##############----------------------  Ending  Main  Menu   ----------------------##########################
######################################     Toolbar     ###################################################


##############----------------------  Ending  Toolbar     ----------------------##########################
######################################     TEXT editor  ###################################################


##############----------------------  Ending  TEXT editor  ----------------------##########################
######################################     main status bar#################################################


##############----------------------  Ending  main status bar--------------------##########################
######################################     Main  Menu functionality #######################################


##############----------------------  Ending  Main  Menu functionality ----------##########################

# file commands :

file.add_command(label="New File",image=newIcon,compound=tk.LEFT,accelerator='Ctrl+N' ,command = action)
file.add_command(label="Open",image=openIcon,compound=tk.LEFT,accelerator='Ctrl+O' ,command = action)      
file.add_command(label="Save",image=saveIcon,compound=tk.LEFT,accelerator='Ctrl+O' ,command = action)
file.add_command(label="Save as",image=save_asIcon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command= action)
file.add_separator()   
file.add_command(label="Exit",image=exitIcon,compound=tk.LEFT,accelerator='Ctrl+E' ,command = action)

# Edit commands :

edit.add_command(label="Copy",image=copyIcon,compound=tk.LEFT,accelerator='Ctrl+C' ,command = action)
edit.add_command(label="Cut",image=cutIcon,compound=tk.LEFT,accelerator='Ctrl+X' ,command = action)      
edit.add_command(label="Paste",image=pasteIcon,compound=tk.LEFT,accelerator='Ctrl+V' ,command = action)
edit.add_command(label="Clear all",image=clear_allIcon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command= action)
edit.add_command(label="Find",image=findIcon,compound=tk.LEFT,accelerator='Ctrl+F' ,command = action)

# View commands :

view.add_checkbutton(label="Tool Bar",image=toolBarIcon,compound=tk.LEFT ,command = action)
view.add_checkbutton(label="Status Bar",image=statusBarIcon,compound=tk.LEFT ,command = action)      

# Colour Theme commands :

count =0 

for i in colourDict:
    ColourTheme.add_radiobutton(label=i,image=colourIcons[count],variable=themeChosen,compound = tk.LEFT)
    count+=1




###########################################################################################################





###########################################################################################################


mainApplication.mainloop()



###########################################################################################################

########################### NOTE :
#
#   ICONS => https://www.flaticon.com/
# 
# 
#
#
# 
# 
#
###########################################################################################################