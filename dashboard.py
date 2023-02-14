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
        self.window.configure(bg="lightgrey")


        # Menu Bar
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        # img = ImageTk.PhotoImage(Image.open("retail.ico"))


        # Create menu
        # File menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Print')
        file_menu.add_command(label='Export')
        file_menu.add_separator()

        sub_file_menu = Menu(file_menu, tearoff=0)
        file_menu.add_cascade(label='Layout', menu=sub_file_menu)
        sub_file_menu.add_command(label='Add or remove columns')
        sub_file_menu.add_command(label='Save')
        sub_file_menu.add_separator()
        sub_file_menu.add_command(label='Restore default layout')

        file_menu.add_separator()
        file_menu.add_command(label='Log Out')
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.window.destroy)

        # Show menu
        show_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Show', menu=show_menu)
        show_menu.add_command(label='Sales')
        show_menu.add_command(label='Quotation')
        show_menu.add_command(label='Customers')
        show_menu.add_command(label='Products')
        show_menu.add_command(label='Account Payable')
        show_menu.add_command(label='Register')
        show_menu.add_command(label='Users')
        show_menu.add_command(label='Statistics')
        show_menu.add_separator()
        show_menu.add_command(label='Hide Test')

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='1. Learn how to manage your POS')
        help_menu.add_separator()
        help_menu.add_command(label='2. Online Technical Suport')
        help_menu.add_separator()
        help_menu.add_command(label='3. Terms of service')
        help_menu.add_separator()
        help_menu.add_command(label='4. Update Techcified POS')
        help_menu.add_separator()
        help_menu.add_command(label='5. Renew your POS license')
        help_menu.add_separator()
        sub_help_menu = Menu(help_menu, tearoff=0)
        help_menu.add_cascade(label='6. Account', menu=sub_help_menu)
        sub_help_menu.add_command(label='Create a new account')

        Set_B = Button(window, text='Set up your application here', font=('roboto', 10, 'bold'), bd=0, fg='#D30E0E', bg='white', cursor='hand2')
        Set_B.place(relx=0.5, y=20, anchor=N, width=300)

        #frame
        MF = Frame(window, width=950, height=500, bg='#e5dcda')
        MF.place(relx=0.5, y=120, anchor=N)

        img1 = PhotoImage(file='./Images/admicon.png')
        img1.photo = img1
        ADP = Button(MF, text='Admission\nPortal', image=img1, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        ADP.place(x=45, y=30, width=200, height=200,)

        img2 = PhotoImage(file='./Images/sticon.png')
        img2.photo = img2
        SP = Button(MF, text='Student\nPortal', image=img2, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        SP.place(x=265, y=30, width=200, height=200,)

        img3 = PhotoImage(file='./Images/teachericon.png')
        img3.photo = img3
        TP = Button(MF, text='Teachers\nPortal', image=img3, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        TP.place(x=485, y=30, width=200, height=200,)

        img4 = PhotoImage(file='./Images/payicon.png')
        img4.photo = img4
        PP = Button(MF, text='Payment\nPortal', image=img4, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        PP.place(x=705, y=30, width=200, height=200,)

        img5 = PhotoImage(file='./Images/medicon.png')
        img5.photo = img5
        MR = Button(MF, text='Medical\nStatement', image=img5, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        MR.place(x=45, y=260, width=200, height=200,)

        img6 = PhotoImage(file='./Images/calicon.png')
        img6.photo = img6
        SC = Button(MF, text='School\nCalendar', image=img6, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        SC.place(x=265, y=260, width=200, height=200,)

        img7 = PhotoImage(file='./Images/repicon.png')
        img7.photo = img7
        RC = Button(MF, text='Report\nCard', image=img7, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        RC.place(x=485, y=260, width=200, height=200,)

        img8 = PhotoImage(file='./Images/exticon.png')
        img8.photo = img8
        EC = Button(MF, text='Extra\nCurriculum', image=img8, compound=TOP, font=('roboto', 15, 'bold'), bd=0, bg='white', fg='#D30E0E', cursor='hand2')
        EC.place(x=705, y=260, width=200, height=200,)
        

        


       

def dash():
    window = Tk()
    Dashboard(window)
    window.mainloop()


if __name__ == '__main__':
    dash()




