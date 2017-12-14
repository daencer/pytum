from pahtum_class import PahTum
import tkinter as tk


def main():
    root = tk.Tk()
    root.config(bg="red")

    btn = PahTum(root)
    root.mainloop()


if __name__ == '__main__':
    main()
