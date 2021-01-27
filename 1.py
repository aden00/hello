from tkinter import *

window = Tk()
window.title('aden')
window.geometry('500x500')

label =Label(window, text='your name: ')
myname= Label(text='this is adens tool')
txtentry = Entry(window)
okbutton = Button(window, text='Press' )
cancelbutton = Button(window, text='Cancel')

myname.pack(anchor=N)
label.pack(side='left')
txtentry.pack(side='left',fill='x',expand=1,padx=5)
okbutton.pack(side='right',padx =5,sticky='we')
cancelbutton.pack(side='right',sticky='we')





window.mainloop()