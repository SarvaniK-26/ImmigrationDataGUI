from tkinter import *
from tkinter import filedialog
root = Tk()

#Create title for the display (seen on the top left corner).
root.title("Data Input for Immigrant Students")

root.geometry("800x800")
root.config(bg = '#008080')


def submit_info():
    # Set variables to get the data from each entry widget.
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    curage_info = curage.get()
    agemove_info = agemove.get()
    dep_info = dep.get()
    parent_info = parent.get()
    status_info = status.get()
    agingout_info = agingout.get()
    zipcode_info = zipcode.get()
    district_info = district.get()
    
    # Format how the information will be printed onto the text file. 
    print(firstname_info, lastname_info, curage_info, agemove_info, dep_info, parent_info, status_info, agingout_info, zipcode_info, district_info)
    
    # Append data to the immigration.txt file that can be found in the source folder. 
    file = open("immigration.txt", "a")
    
    # Variables from previous line will get the information from entry widget and write to the file. 
    file.write("\n")
    file.write("Your First Name: " + firstname_info + "\n")
    file.write("Your Last Name: " + lastname_info + "\n" )
    file.write("Your Current Age: " + curage_info + "\n")
    file.write("Age you moved to the USA: " + agemove_info + "\n")
    file.write("Dependent Visa you are currently on: " + dep_info + "\n")
    file.write("The Parent Visa you are on: " + parent_info + "\n")
    file.write("Your Status: " + status_info + "\n")
    file.write("Aging Out (yes/no): " + agingout_info +  "\n")
    file.write("Your Zipcode: " + zipcode_info +"\n")
    file.write("Your Congressional District: "  + district_info + "\n")
    file.close()
   
# This allows users to delete info in the entry boxes.
def delete():
    firstname_entry.delete(0, 'end')
    lastname_entry.delete(0, 'end')
    curage_entry.delete(0, 'end')
    agemove_entry.delete(0, 'end')
    dep_entry.delete(0, 'end')
    parent_entry.delete(0, 'end')
    status_entry.delete(0, 'end')
    agingout_entry.delete(0, 'end')
    zipcode_entry.delete(0, 'end')
    district_entry.delete(0, 'end')
    
# Allows users to open text from file by printing
def openfile():
    file = filedialog.askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
    
    file.close()
# Create a list of all of the labels. 
labels = ['First Name ' , 'Last Name ', 'Current Age ', 'Age of Move ', 'Dependent Visa Type ', 'Parent Visa Type ', 'Current Status ', 'Aging out (Yes/No) ', 'Zip Code ', 'Congressional District ']

# For every i in range within the labels list go through and create a different label for each one. 
for i in range(len(labels)):
    labels_all = 'label' + str(i) 
    
    # Format labels to capture text from labels list and create a widget for each i in range 
    labels_all = Label(root, text = labels[i],  font = ('Times New Roman', 20 ,'bold' ), bg = '#008080') # shows the specific label on each one with the name from the list
    labels_all.grid(row=i+1, column=0) # adds to the display

# Set variables to StringVar(), entry spots get data as strings
firstname = StringVar()
lastname = StringVar()
curage = StringVar()
agemove = StringVar()
dep = StringVar()
parent = StringVar()
status = StringVar()
agingout = StringVar()
zipcode = StringVar()
district = StringVar()

# Set each entry box to the variables above so users can input information.
firstname_entry = Entry(textvariable = firstname, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3' )
lastname_entry = Entry(textvariable = lastname, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
curage_entry = Entry(textvariable = curage, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
agemove_entry = Entry(textvariable = agemove, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
dep_entry = Entry(textvariable = dep, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
parent_entry = Entry(textvariable = parent, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
status_entry = Entry(textvariable = status, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
agingout_entry = Entry(textvariable = agingout, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
zipcode_entry = Entry(textvariable = zipcode, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')
district_entry = Entry(textvariable = district, width = "30",  font = ('Times New Roman', 20 ,'bold' ), bg = '#d3d3d3')

# Place entry widget onto the grid. 
firstname_entry.grid(row = 1, column = 1)
lastname_entry.grid(row = 2, column = 1)
curage_entry.grid(row = 3, column = 1)
agemove_entry.grid(row = 4, column = 1)
dep_entry.grid(row = 5, column = 1)
parent_entry.grid(row =6, column = 1)
status_entry.grid(row = 7, column = 1)
agingout_entry.grid(row = 8, column = 1)
zipcode_entry.grid(row = 9, column = 1)
district_entry.grid(row = 10, column =1)


# This submit button allows users to add the data to a user.txt file (found in source folder).
button_submit = Button(root, text = "Submit Data", width = "20" , height = '2',command = submit_info, bg = '#ff7f50')
button_submit.grid(row =  11, column = 1)

# Button allows users to exit the program.
button_quit = Button(root, text = "Exit Program", width = "20" , height = '2',  command = root.quit, bg = '#ff7f50')
button_quit.grid(row = 12, column =1)

# Button allows users to delete text in entry files to reenter data. 
mybutton = Button(root, text = "Delete", command = delete, width = "20" , height = '2', bg = '#ff7f50')
mybutton.grid(row = 13, column = 1)

# Button lets users open the file data is saved to
openButton = Button(root, text = "Open Contents of File", width = "20" , height = '2',  command = openfile, bg = '#ff7f50')
openButton.grid(row = 14, column =1)



mainloop()