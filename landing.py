from tkinter import *
from PIL import ImageTk, Image




class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.wm_iconbitmap('Images/icon.ico')
        self.window.title('EducAPP-360')
        self.window.geometry('400x400')
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

        # Top Buttons Menus        
        B1 = Button(window, text='Why EducAPP-360?', font=('roboto', 10, 'bold'), bg='white', bd=0, cursor='hand2')
        B1.place(x=410, y=30)
        
        B2 = Button(window, text='Platforms', font=('roboto', 10, 'bold'), bg='white', bd=0, cursor='hand2')
        B2.place(x=590, y=30)

        B3 = Button(window, text='Usage & Rewards', font=('roboto', 10, 'bold'), bg='white', bd=0, cursor='hand2')
        B3.place(x=690, y=30)

        B4 = Button(window, text='License', font=('roboto', 10, 'bold'), bg='white', bd=0, cursor='hand2')
        B4.place(x=840, y=30)

        LB = Button(window, text='Log In', font=('roboto', 10, 'bold'), bg='black', fg='white', cursor='hand2')
        LB.place(x=1135, y=30, width=70)
        SB = Button(window, text='Sign Up', font=('roboto', 10, 'bold'), bg='#BC0404', fg='white', cursor='hand2')
        SB.place(x=1220, y=30, width=80)

        # Labels
        txt = 'School Management\nsolution\nthat works seamlessly'
        ML1 = Label(window, text=txt, font=('roboto', 23, 'bold'), bg='white', justify=LEFT)
        ML1.place(x=80, y=250)

        txt2 = 'Built for Small, medium, & large schools,\nand freelancers.No hidden fee, no hassle of any form'
        ML2 = Label(window, text=txt2, font=('roboto', 10, 'bold'), bg='white', justify=LEFT)
        ML2.place(x=80, y=400)

        ActionB = Button(window, text='Get EducAPP-360 For Free', font=('roboto', 10, 'bold'), bd=0, bg='#BC0404', fg='white', cursor='hand2')
        ActionB.place(x=80, y=500, width=200, height=50)
        
               


    
def dash():
    window = Tk()
    Dashboard(window)
    mainloop()


if __name__ == '__main__':
    dash()




