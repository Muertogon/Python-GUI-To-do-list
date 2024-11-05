from tkinter import *
from tkinter import ttk

#create the window
main = Tk(className="To do list")
main.geometry("500x400")

#create frames in the window
frm = ttk.Frame(main, padding=2, width=300, height=300, borderwidth=2, relief="solid")
frm.pack(side="left", fill="both", expand=True)
frmTwo = ttk.Frame(main, padding=2, width=200, height=300, borderwidth=2, relief="solid")
frmTwo.pack(side="right", fill="both", expand=True)

#variables
comboValues = ['Critical','High','Medium','Low']
chooseText  = ['Please enter the task you want to add', 'Choose the priority', 'Add', 'Reset']
dynamic_buttons = []
entryValue  = StringVar()

def write_callback(var, index, mode):
  # checks if you can add the task
  val = entryValue.get()
  if not val or len(val) > 40:
    taskCheck.config(state='disabled')
  else:
    taskCheck.config(state='normal')

def taskAdd():
  print('creates label 1')
  label = ttk.Label(frmTwo, text=entryValue.get()).grid(padx=10, pady=10)
  print('creates label 2')
  labelTwo = ttk.Label(frmTwo, text=taskPriority.get()).grid(padx=10, pady=10)

def valueReset():
  #resets the fields
  taskPriority.set('')
  entryValue.set('')

#widgets

# entry text box
ttk.Label(frm, text=chooseText[0]).grid()
taskName = ttk.Entry(frm, width=30, textvariable=entryValue)
taskName.grid(padx=20, pady=20)
entryValue.trace_add("write", callback= write_callback)

# priority
ttk.Label(frm, text=chooseText[1]).grid()
taskPriority = ttk.Combobox(frm, justify='left', values=comboValues)
taskPriority.grid()


#add
taskCheck = ttk.Button(frm, text=chooseText[2], command = taskAdd(), state='disabled')
taskCheck.grid(padx=20, pady=20)

#reset
valueReset = ttk.Button(frm, text=chooseText[3], command = valueReset)
valueReset.grid(padx=20)

#Quit
ttk.Button(frm, text="Quit", command=main.destroy).grid()

main.mainloop()

'''
  Set grid seperately(lines 24,27), as when trying to return a value of an entry field, lets say,
  it tries to return the grid.
'''