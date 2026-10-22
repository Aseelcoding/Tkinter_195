import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Study Program Prediction")
    root.geometry("700x500")
    root.minsize(600, 450)

    title_label = tk.Label(
        root,
        text="Study Program Prediction",
        font=("Arial", 20, "bold"),
        pady=20,
    )
    title_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
