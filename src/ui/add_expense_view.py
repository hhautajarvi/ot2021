from tkinter import Radiobutton, ttk, constants, IntVar
from services.user_service import user_service

class AddExpenseView:
    def __init__(self, root, show_budget_view):
        self.root = root
        self.frame = None
        self.show_budget_view = show_budget_view

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def enter_amount(self):
        amount_label = ttk.Label(master=self.frame, text="Enter expense amount:")
        self.amount_sum = ttk.Entry(master=self.frame)
        amount_label.grid(padx=5, pady=5)
        self.amount_sum.grid(row=1, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)  

    def choose_category(self):
        category_label = ttk.Label(master=self.frame, text="Choose category")
        self.category = IntVar()
        food_button = Radiobutton(master=self.frame, text="Food", variable=self.category, value=1)
        transit_button = Radiobutton(master=self.frame, text="Transit", variable=self.category, value=2)
        entertainment_button = Radiobutton(master=self.frame, text="Entertainment", variable=self.category, value=3)
        living_button = Radiobutton(master=self.frame, text="Living", variable=self.category, value=4)
        utilities_button = Radiobutton(master=self.frame, text="Utilities", variable=self.category, value=5)
        insurance_button = Radiobutton(master=self.frame, text="Insurance", variable=self.category, value=6)
        category_label.grid(padx=5, pady=5)
        food_button.grid(padx=5, pady=5)
        transit_button.grid(padx=5, pady=5)
        entertainment_button.grid(padx=5, pady=5)
        living_button.grid(padx=5, pady=5)
        utilities_button.grid(padx=5, pady=5)
        insurance_button.grid(padx=5, pady=5)

    def write_comment(self):
        comment_label = ttk.Label(master=self.frame, text="Write a comment of the expense:")
        self.comment = ttk.Entry(master=self.frame)
        comment_label.grid(padx=5, pady=5)
        self.comment.grid(row=8, column=2, sticky=(constants.E, constants.W), padx=5, pady=5)  

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        budget_label = ttk.Label(master=self.frame, text="Enter a new expense")
        budget_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.enter_amount()
        self.choose_category()
        self.write_comment()
        add_button = ttk.Button(master=self.frame, text="Add", command=self.addbutton_click)
        add_button.grid(padx=5, pady=5)


    def addbutton_click(self):
        amount = int(self.amount_sum.get())
        comment = self.comment.get()
        category = self.category.get()
        user_service.create_expense(amount, category, comment)
        self.show_budget_view()