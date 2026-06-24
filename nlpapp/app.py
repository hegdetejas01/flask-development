from tkinter import *
from mydb import Database
from tkinter import messagebox
import myApi

class NLPApp:

    def __init__(self):

        self.dbo = Database() # creating a database object


        # gui for the app
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap('nlpapp/resources/favicon.ico') # adding our own icon
        self.root.geometry('450x650') # setting the dimensions of the gui window
        self.root.configure(bg="#ACDDEC")

        self.login_gui()

        self.root.mainloop() # keep the window open

    def loadHeading(self):
        heading = Label(self.root, text="NLP App", bg = "#ACDDEC", fg="black")
        # Geometric manager - Pack, Grid
        heading.pack(pady=(20,10)) # 20 gap from top, 10 gap in bottom
        heading.configure(font=('verdana', 25, 'bold'))

    def loadEmail(self):
        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady = (10,10))
        self.email_input = Entry(self.root, width=50) # width increases the width of the text box
        self.email_input.pack(pady=(5,10), ipady=4) #ipady means internal padding for y axix for the email text box. Basically it increases the height

    def loadPassword(self):
        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady = (10,10))
        self.password_input = Entry(self.root, width=50, show="*")
        self.password_input.pack(pady=(5,10), ipady=4)

    def login_gui(self):
        self.clear_gui()

        self.loadHeading()
        self.loadEmail()
        self.loadPassword()

        login_button = Button(self.root, text="Login", width=15, height=1, command=self.performLogin)
        login_button.pack(pady=(10,10))
        login_button.configure(font=("", 15, 'bold'))

        label3 = Label(self.root, text="Not a member ?")
        label3.pack(pady = (20,10))
        
        redirect_button = Button(self.root, text="Register Now", bg='#ACDDEC', fg = "black", font=("",8,"bold"), command=self.register_gui) # when the button is clicked, call register_gui function
        redirect_button.pack(pady=(0,10))

        print(self.email_input, self.password_input)

    def clear_gui(self):
        # clear existing gui
        for i in self.root.pack_slaves(): # this function brings all elements - all labels and all buttons from above
            i.destroy()

    def register_gui(self):
        self.clear_gui()

        self.loadHeading()

        label0 = Label(self.root, text="Enter Name")
        label0.pack(pady = (10,10))
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5,10), ipady=4)

        self.loadEmail()
        self.loadPassword()

        register_button = Button(self.root, text="Register", width=15, height=1, command=self.performRegistration)
        register_button.pack(pady=(10,10))
        register_button.configure(font=("", 15, 'bold'))

        label3 = Label(self.root, text="Already a member ? ")
        label3.pack(pady = (20,10))
        
        redirect_button = Button(self.root, text="Login Now", bg='#ACDDEC', fg = "black", font=("",8,"bold"), command=self.login_gui)
        redirect_button.pack(pady=(0,10))

    def performRegistration(self):

        # fetch data from Entry Box
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.addData(name, email, password)
        if response == 1:
            print("Registration Successful")
            messagebox.showinfo("Success","Registration Successfull. Proceeding to Login.")
        else: 
            print("Email Exists")
            messagebox.showerror("Failed", "Email Already Exists. Proceeding to Login")

        self.login_gui()

    def performLogin(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.userLogin(email, password)
        if response == 1:
            messagebox.showinfo("success", "Login Successfull")
            self.home_gui()
        
        else:
            if response == -1:
                messagebox.showerror("failed", "Incorrect password. Try again :)")
                self.login_gui()
            elif response == 0:
                messagebox.showerror("failed", "User doesn't exist. Proceeding to Register.")
                self.register_gui()

    def createButton(self, text, function = None):
        if function == "senti":
            Button(self.root, text=text, width=25, height=4, command=self.sentiment_gui, font=("", 15, "bold")).pack(pady=(20,20))
        elif function == "ner":
            Button(self.root, text=text, width=25, height=4, command=self.nre_gui, font=("", 15, "bold")).pack(pady=(20,20))
        elif function == "emo":
            Button(self.root, text=text, width=25, height=4, command=self.emotion_gui, font=("", 15, "bold")).pack(pady=(20,20))
    
    def nre_gui():
        pass
    def emotion_gui():
        pass

    def home_gui(self):
        print("I am home GUI - i am called")
        self.clear_gui()

        self.loadHeading()

        sentiment_button = self.createButton("Sentiment Analysis", function="senti")
        ner_button = self.createButton("Named Entity Recognition", function="ner")
        emotion_button = self.createButton("Emotion Prediction", function="emo")

        logout_button = Button(self.root, text="Logout", bg='#ACDDEC',width="15", fg = "black", font=("",8,"bold"), command=self.login_gui)
        logout_button.pack(pady=(0,10))

    def sentiment_gui(self):
        self.clear_gui()
        self.loadHeading()

        heading = Label(self.root, text="Sentiment Analysis", bg="#ACDDEC", fg = "black")
        heading.pack(pady=(20,10))
        heading.configure(font=('verdana', 25, 'bold'))

        label1 = Label(self.root, text="Enter the text", font=("", 12, "bold"))
        self.sentiment_input = Entry(self.root, width=60)
        label1.pack(pady=(10, 10))
        self.sentiment_input.pack(pady=(5,10), ipady=4)
        
        self.sentiment_result = Label(self.root, text="", bg="#ACDDEC", fg = "black")
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        sentiment_button = Button(self.root, text="Analyse Sentiment", width=20, height=2, command=self.do_sentiment_analysis)
        sentiment_button.pack(pady=(10,10))
        sentiment_button.configure(font=("", 15))

        goback_button = Button(self.root, text="Go Back", width=15, height=1, command=self.home_gui)
        goback_button.pack(pady=(10,10))
        goback_button.configure(font=("", 15, 'bold'))

    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = myApi.API().sentimentAnalysis(text)
        print(result)
        
nlp = NLPApp()
