from tkinter import *

"""
Position could be pack,place or grid
"""


def button_click():
    new_text = input_data.get()
    my_label.config(text=new_text)


window = Tk()
window.title("Nuevo título")
window.minsize(width=1000, height=800)

# Label
my_label = Label(text="Label", font=("Arial", 29, "bold"))
my_label.place(x=0, y=0)

my_label["text"] = "New Text"
my_label.config(text="New new Text")

######## BUTTON###########
my_button = Button(text="Click me", command=button_click)
my_button.pack()

########ENTRY###########
input_data = Entry(width=10)
input_data.pack()

######TEXT#######
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example")
print(text.get("1.0", END))
text.pack()


######SPINBOX#######
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


######SCALE#######
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


######CHECKBUTTON#######
def checked_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checked_used)
checked_state.get()
checkbutton.pack()


######RADIOBUTTON#######
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


######LISTBOX#######
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Pear", "Lemon"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
