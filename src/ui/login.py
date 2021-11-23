from tkinter import ttk, constants
from repositories.user_repository import UserRepository

class LoginView():
    def __init__(self, root, budget_create, budget_view):
        self.root = root
        self.username = None
        self.password = None
        self.newuser = None
        self.newpass = None
        self.frame = None
        self.budget_create = budget_create
        self.budget_view = budget_view

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def show_login(self):
        login_label = ttk.Label(master=self.frame, text="Login")
        username_label = ttk.Label(master=self.frame, text="Username")
        self.username_entry = ttk.Entry(master=self.frame)

        password_label = ttk.Label(master=self.frame, text="Password")
        self.password_entry = ttk.Entry(master=self.frame)

        login_label.grid(row=1, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        self.username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        self.password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        loginbutton = ttk.Button(master=self.frame, text="Login", command=self.loginbutton_click)
        loginbutton.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


    def show_register(self):
        register_label = ttk.Label(master=self.frame, text="Make a new user")

        newuser_label = ttk.Label(master=self.frame, text= "Choose a username")
        self.newuser_entry = ttk.Entry(master=self.frame)

        newpassword_label = ttk.Label(master=self.frame, text="Choose a password")
        self.newpassword_entry = ttk.Entry(master=self.frame)
        
        register_label.grid(row=5, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        newuser_label.grid(padx=5, pady=5)
        self.newuser_entry.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        newpassword_label.grid(padx=5, pady=5)
        self.newpassword_entry.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        registerbutton = ttk.Button(master=self.frame, text="Register", command=self.registerbutton_click)
        registerbutton.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        welcome_label = ttk.Label(master=self.frame, text="Welcome to BudgetApp!")

        welcome_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.show_login()
        self.show_register()

        self.frame.grid_columnconfigure(1, weight=1, minsize=300)

    def loginbutton_click(self):
        user = UserRepository.find_user(self.username_entry.get(), self.password_entry.get())
        self.budget_view(user)

    def registerbutton_click(self):
        user = UserRepository.create_user(self.newuser_entry.get(), self.newpassword_entry.get())
        self.budget_create(user)
