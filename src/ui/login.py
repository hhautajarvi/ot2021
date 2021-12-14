from tkinter import ttk, constants
from services.user_service import user_service

class LoginView():
    def __init__(self, root, budget_create, budget_view): 
        self._root = root
        self._frame = None
        self._budget_create = budget_create
        self._budget_view = budget_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_login(self):
        login_label = ttk.Label(master=self._frame, text="Login")
        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password_entry = ttk.Entry(master=self._frame)

        login_label.grid(row=1, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        loginbutton = ttk.Button(master=self._frame, text="Login", command=self.loginbutton_click)
        loginbutton.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)


    def _show_register(self):
        register_label = ttk.Label(master=self._frame, text="Make a new user")

        newuser_label = ttk.Label(master=self._frame, text= "Choose a username")
        self._newuser_entry = ttk.Entry(master=self._frame)

        newpassword_label = ttk.Label(master=self._frame, text="Choose a password")
        self._newpassword_entry = ttk.Entry(master=self._frame)
        
        register_label.grid(row=5, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        newuser_label.grid(padx=5, pady=5)
        self._newuser_entry.grid(row=6, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        newpassword_label.grid(padx=5, pady=5)
        self._newpassword_entry.grid(row=7, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        registerbutton = ttk.Button(master=self._frame, text="Register", command=self._registerbutton_click)
        registerbutton.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        welcome_label = ttk.Label(master=self._frame, text="Welcome to BudgetApp!")
        welcome_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self._show_login()
        self._show_register()

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def loginbutton_click(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        user_service.login(username, password)
        self._budget_view()

    def _registerbutton_click(self):
        username = self._newuser_entry.get()
        password = self._newpassword_entry.get()
        user_service.create_new_user(username, password)
        self._budget_create()
