from tkinter import ttk, constants

from ui.login import LoginView

class UI:
    def __init__(self, root):
        self.root = root
        self.view = None

    def start(self):
        self.show_login()

    def show_login(self):
        self.hide_view()
        self.view = LoginView(self.root)
        self.view.pack()

    def hide_view(self):
        if self.view:
            self.view.destroy()

        self.view = None