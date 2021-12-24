from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title('BudgetApp')

    ui_window = UI(window)
    ui_window.start()

    window.mainloop()


if __name__ == '__main__':
    main()
