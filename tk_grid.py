import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Tkinter Grid")
    root.geometry("400x300")
    root.resizable(False, False)

    # Root Grid 設定
    root.columnconfigure(0, weight=0)  # Left
    root.columnconfigure(1, weight=1)  # Center
    root.columnconfigure(2, weight=0)  # Right
    root.rowconfigure(0, weight=1)

    
    # Left Sidebar
    left = tk.Frame(root, bg="lightgreen", width=40)
    left.grid(row=0, column=0, sticky="ns")

    # Right Sidebar
    right = tk.Frame(root, bg="lightblue", width=40)
    right.grid(row=0, column=2, sticky="ns")

    # Center container
    center = tk.Frame(root)
    center.grid(row=0, column=1, sticky="nsew")

    center.columnconfigure(0, weight=1)
    center.rowconfigure(0, weight=0)  # Top
    center.rowconfigure(1, weight=1)  # Middle
    center.rowconfigure(2, weight=0)  # Bottom

    # Top (Red)
    top = tk.Frame(center, bg="red", height=60)
    top.grid(row=0, column=0, sticky="ew")
    top.grid_propagate(False)

    label_left = tk.Label(top, text="left", bg="white", fg="black")
    label_left.grid(row=0, column=0, sticky="n")

    label_center = tk.Label(top, text="center", bg="white", fg="black")
    label_center.grid(row=0, column=1, sticky="n")

    label_right = tk.Label(top, text="Right", bg="white", fg="black")
    label_right.grid(row=0, column=2, sticky="n")

    top.columnconfigure(0, weight=1)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=1)

    # Middle (Yellow)
    middle = tk.Frame(center, bg="yellow")
    middle.grid(row=1, column=0, sticky="nsew")

    # Bottom (Blue)
    bottom = tk.Frame(center, bg="blue", height=30)
    bottom.grid(row=2, column=0, sticky="ew")
    bottom.grid_propagate(False)

    root.mainloop()


if __name__ == "__main__":
    main()
