from tkinter import *
from tkcalendar import *

# createing object 
root = Tk()
root.title('LIC Calendar')
root.geometry("600x700")
root.configure(background="lightblue")

# heading
Label(root, text = 'Gregorian Calendar',bg='lightblue', font =('Harlow Solid Italic', 30)).pack( side = TOP, pady = 50,padx=15)

#Adding Calendar
calen = Calendar(root,select="day",date_pattern ='d/m/yy',
                 showweeknumbers = False,
                 showothermonthdays =False,
                 background="purple",
                 normalbackground ="lavender",
                 selectbackground = "lightgreen",
                 weekendbackground = "silver")
calen.pack(pady=25)


# selecting the date
def peek_date():
    label.config( text = "Selected Date "+ calen.get_date (),font =('Lucida Handwriting', 25),bg="lightblue",)
    label.pack(pady=15, expand = True,)

    
#Button section
calen_button = Button(calen, text = "Click me",command = peek_date,font =('Lucida Calligraphy', 15), bg="violet",bd="5" )
calen_button.pack(fill = BOTH, expand = True)


#After Clicking button
label = Label(root,text="Please Select Any Date",font =('Lucida Calligraphy', 15), bg="lightblue")
label.pack(pady=25)

root.mainloop()

