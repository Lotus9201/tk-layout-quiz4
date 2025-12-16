import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Tkinter Pack")
    root.geometry("400x300")
    root.resizable(False, False)

    # Left Sidebar
    left = tk.Frame(root, bg="lightgreen", width=40)
    left.pack(side="left", fill="y")

    # Right Sidebar
    right = tk.Frame(root, bg="lightblue", width=40)
    right.pack(side="right", fill="y")

    # Center container
    center = tk.Frame(root)
    center.pack(fill="both", expand=True)

    # Top (Red)
    top = tk.Frame(center, bg="red", height=60)
    top.pack(fill="x")
    top.pack_propagate(False)

    label_left = tk.Label(top, text="left", bg="white", fg="black")
    label_left.pack(side="left", expand=True, anchor="n")

    label_center = tk.Label(top, text="center", bg="white", fg="black")
    label_center.pack(side="left", expand=True, anchor="n")

    label_right = tk.Label(top, text="Right", bg="white", fg="black")
    label_right.pack(side="left", expand=True, anchor="n")

    # Bottom (Blue)
    bottom = tk.Frame(center, bg="blue", height=30)
    bottom.pack(side="bottom", fill="x")
    bottom.pack_propagate(False)

    # Middle (Yellow)
    middle = tk.Frame(center, bg="yellow")
    middle.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
