from tkinter import ttk, constants

class LoginView():
    def __init__(self, root):
        self.root = root
        self.username = None
        self.password = None
        self.newuser = None
        self.newpass = None

        self.initialize()

    def show_login(self):
        login_label = ttk.Label(master=self.frame, text="Login")
        username_label = ttk.Label(master=self.frame, text="Username")
        username_entry = ttk.Entry(master=self.frame)

        password_label = ttk.Label(master=self.frame, text="Password")
        password_entry = ttk.Entry(master=self.frame)

        loginbutton = ttk.Button(master=self.frame, text="Login", command=self.loginbutton_click(username_entry.get(), password_entry.get()))
        login_label.grid(row=1, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        loginbutton.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def show_register(self):
        register_label = ttk.Label(master=self.frame, text="Make a new user")

        newuser_label = ttk.Label(master=self.frame, text= "Choose a username")
        newuser_entry = ttk.Entry(master=self.frame)

        newpassword_label = ttk.Label(master=self.frame, text="Choose a password")
        newpassword_entry = ttk.Entry(master=self.frame)
        registerbutton = ttk.Button(master=self.frame, text="Register", command=self.registerbutton_click(newuser_entry.get(), newpassword_entry.get()))
        
        register_label.grid(row=5, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        newuser_label.grid(padx=5, pady=5)
        newuser_entry.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        newpassword_label.grid(padx=5, pady=5)
        newpassword_entry.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        registerbutton.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        welcome_label = ttk.Label(master=self.frame, text="Welcome to BudgetApp!")

        welcome_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.show_login()
        self.show_register()

        self.root.grid_columnconfigure(1, weight=1, minsize=300)

    def loginbutton_click(self, username_entry, password_entry):
        pass

    def registerbutton_click(self, newuser_entry, newpassword_entry):
        pass