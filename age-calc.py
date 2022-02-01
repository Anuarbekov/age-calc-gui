import datetime
from tkinter import *
from tkinter import messagebox
now = datetime.datetime.now()

def clearAll() :
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)
 
def checkError() :
    if (dayField.get() == "" or monthField.get() == ""
        or yearField.get() == ""):
        messagebox.showerror("Input Error")
        clearAll()
        return -1
def calculateAge() :
    global now
    value = checkError()
 
    if value ==  -1 :
        return
     
    else :
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())
 
        given_day = now.day
        given_month = now.month
        given_year = now.year
        
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]
                     
                     
        # if birth month exceeds given month, then
        # donot count this year and add 12 to the
        # month so that we can subtract and find out
        # the difference
        if (birth_month > given_month):
            given_year = given_year - 1
            given_month = given_month + 12
                     
        # calculate day, month, year
        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;
 
        # calculated day, month, year write back
        # to the respective entry boxes
 
        # insert method inserting the 
        # value in the text entry box.
         
        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
     
 
# Driver Code
if __name__ == "__main__" :
 
    # Create a GUI window
    gui = Tk()
 
    # Set the background colour of GUI window 
    gui.configure(background = "light green")
 
    # set the name of tkinter GUI window
    gui.title("Age Calculator")
 
     # Set the configuration of GUI window
    gui.geometry("210x260")
 
    # Create a Date Of Birth : label
    dob = Label(gui, text = "Date Of Birth", bg = "blue")
 
    # Create a Day : label
    day = Label(gui, text = "Day", bg = "light green")
 
    # Create a Month : label
    month = Label(gui, text = "Month", bg = "light green")
 
    # Create a Year : label
    year = Label(gui, text = "Year", bg = "light green")
 
    # Create a Years : label
    rsltYear = Label(gui, text = "Years", bg = "light green")
 
    # Create a Months : label
    rsltMonth = Label(gui, text = "Months", bg = "light green")
 
    # Create a Days : label
    rsltDay = Label(gui, text = "Days", bg = "light green")
 
    
    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge)
 
    
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)
 
    dayField = Entry(gui)
    monthField = Entry(gui)
    yearField = Entry(gui)
    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)
    dob.grid(row = 0, column = 3)
    day.grid(row = 1, column = 2)
    dayField.grid(row = 1, column = 3)
    month.grid(row = 2, column = 2)
    monthField.grid(row = 2, column = 3)
    year.grid(row = 3, column = 2)
    yearField.grid(row = 3, column = 3)
    resultantAge.grid(row = 4, column = 3)
    rsltYear.grid(row = 5, column = 3)
    rsltYearField.grid(row = 6, column = 3)    
    rsltMonth.grid(row = 7, column = 3)
    rsltMonthField.grid(row = 8, column = 3)
    rsltDay.grid(row = 9, column = 3)
    rsltDayField.grid(row = 10, column = 3)
    clearAllEntry.grid(row = 12, column = 3)
 
    gui.mainloop()   