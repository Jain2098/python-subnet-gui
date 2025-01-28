# main.py

import tkinter as tk

from calculate_subnet_gui import SubnetCalculatorGUI


def main():
    root = tk.Tk()
    SubnetCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
