from tabnanny import check
from tkinter import *
root = Tk()
root.geometry("480x720")

#heading
Label(root, text = 'Python Form', font = "arial 20 bold").grid(row = 0, column = 3)

#field name
name = Label(root, text = "Name: ")
gender = Label(root, text = "Gender: ")
address = Label(root, text = "Address: ")
contact = Label(root, text = "Contact: ")

#packing fields
name.grid(row = 1, column = 2)
address.grid(row = 2, column = 2)
contact.grid(row = 3, column = 2)
gender.grid(row = 4, column = 2)

#variables for storing data
name_value = StringVar
address_value = StringVar
contact_value = IntVar
gender_value = StringVar
check_value = IntVar

#creating entry field
name_entry = Entry(root, textvariable = name_value)
gender_entry = Entry(root, textvariable = gender_value)
address_entry = Entry(root, textvariable = address_value)
contact_entry = Entry(root, textvariable = contact_value)

#packing entry fields
name_entry.grid(row = 1, column = 3)
gender_entry.grid(row = 2, column = 3)
address_entry.grid(row = 3, column = 3)
contact_entry.grid(row = 4, column = 3)

#creating checkbox
check_button = Checkbutton(text = "Rememeber me?",variable = check_value)
check_button.grid(row = 5, column = 3)

#Submit button
Button(text = "Submit").grid(row = 7, column = 3)


root.mainloop()

