"""To-Do list program!"""

"""----Workflow of program----
1. Get string from wordbox(?)
2. Add it to list of TO-DO's with checkbox next to the string when pressed the button "Add"
3. Clear element from list when checkbox is checked
"""

from tkinter import *
from tkinter.messagebox import *
from const.const import *
from func.func import *

def blitScreen(TaskName):
    global finish
    if TaskName != "":
        taskList.append(TaskName)
        checkList.append(BooleanVar()); checkBoxList.append(Checkbutton(root, text=TaskName, variable=checkList[-1]))
        checkBoxList[-1].grid(sticky="W", column=0)
        finish = True
    else:
        showinfo("Error" , "Error. Please enter a task to complete!")

root = Tk()

putTask = Entry(root); putTask.grid(sticky="W", column=0)                                                               #* Text box to type what to do!
Button(root, command=lambda : blitScreen(putTask.get()), text="Add").grid(sticky="W", column=0)                         #* Button to add element to TO-DO list

while True:
    for ind, checkBox in enumerate(checkList):
        if checkBox.get() == True:                                                                                      #*Erase element from list
            checkList.remove(checkList[checkList.index(checkBox)])
            checkBoxList[ind].destroy()
            checkBoxList.remove(checkBoxList[ind])
    if len(checkList) == 0 and finish == True:
        #text = Text(root); text.config(font=("Courier", 44)); text.insert(INSERT, "You're all done!"); text.grid()
        text = Label(root); text.config(text="You're all done!"); text.grid()

        finish = False

    root.update()