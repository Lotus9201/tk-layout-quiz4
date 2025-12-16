import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Tkinter Place")
    root.geometry("400x300")
    root.resizable(False, False)

    # Left Sidebar
    tk.Frame(root, bg="lightgreen").place(
        relx=0, rely=0, relwidth=0.1, relheight=1
    )

    # Right Sidebar
    tk.Frame(root, bg="lightblue").place(
        relx=0.9, rely=0, relwidth=0.1, relheight=1
    )

    # Top
    top = tk.Frame(root, bg="red")
    top.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.2)

    tk.Label(top, text="left", bg="white").place(relx=0.05, rely=0.05)
    tk.Label(top, text="center", bg="white").place(relx=0.45, rely=0.05)
    tk.Label(top, text="Right", bg="white").place(relx=0.8, rely=0.05)

    # Middle
    tk.Frame(root, bg="yellow").place(
        relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7
    )

    # Bottom
    tk.Frame(root, bg="blue").place(
        relx=0.1, rely=0.9, relwidth=0.8, relheight=0.1
    )

    root.mainloop()


if __name__ == "__main__":
    main()
