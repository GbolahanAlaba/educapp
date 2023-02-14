from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from PIL import ImageTk, Image



class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('EducAPP-360 | Signi Up')
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()
        self.window.geometry(f'{sw}x{sh}')
        # self.window.resizable(0,0)
        self.window.state('zoomed')
        self.window.configure(bg="white")


        #  Logo
        img = PhotoImage(file='./Images/logo.png')
        Logo = Label(window, image = img)
        Logo.photo = img
        Logo.place(x=45, y=10)
        Logo_Label = Label(window, text='EducAPP-360', font=('roboto', 15, 'bold'), bg='white', fg='#BC0404')
        Logo_Label.place(x=140, y=30)

        # Welcome Text
        Welc = Label(window, text='Welcome, We are glad you join us!', font=('Arial', 20, 'bold'), fg='black',bg='white')
        Welc.place(x=60, y=120)


        
        
        Login_Text = Label(window, text="Internet access is mind-free, we'll keep you safe.", font=('roboto', 11), bg='white')
        Login_Text.place(x=60, y=170)
        
        
        FN_Label = Label(window, text='First Name', font=('Arial', 13), bg='white')
        FN_Label.place(x=60, y=240)
        FN_Entry = Entry(window, font=('Arial', 13), bd=2, bg='white', relief='groove')
        FN_Entry.place(x=60, y=270, width=250, height=33)

        LN_Label = Label(window, text='Last Name', font=('Arial', 13), bg='white')
        LN_Label.place(x=380, y=240)
        LN_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        LN_Entry.place(x=380, y=270, width=250, height=33)

        U_Label = Label(window, text='Username', font=('Arial', 13), bg='white')
        U_Label.place(x=60, y=320)
        U_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        U_Entry.place(x=60, y=350, width=250, height=33)

        CU_Label = Label(window, text='Confirm Username', font=('Arial', 13), bg='white')
        CU_Label.place(x=380, y=320)
        CU_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        CU_Entry.place(x=380, y=350, width=250, height=33)

        P_Label = Label(window, text='Password', font=('Arial', 13), bg='white')
        P_Label.place(x=60, y=400)
        P_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        P_Entry.place(x=60, y=430, width=250, height=33)

        CP_Label = Label(window, text='Confirm Password', font=('Arial', 13), bg='white')
        CP_Label.place(x=380, y=400)
        CP_Entry = Entry(window, font=('roboto', 13), bd=2, bg='white', relief='groove')
        CP_Entry.place(x=380, y=430, width=250, height=33)


        # # Buttons
        SignupButton = Button(window, text='Sign up', font=('roboto', 10, 'bold'), bd=0, bg='#D30E0E', fg='white', cursor='hand2')
        SignupButton.place(x=60, y=540, width=310, height=33)

        NA_Label = Label(window, text="You have an account?", font=('roboto', 10, 'bold'), bg='white')
        NA_Label.place(x=60, y=500)

        NA_Button = Button(window, text='Click here', font=('roboto', 10, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        NA_Button.place(x=215, y=500)

        


       

def dash():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    dash()




