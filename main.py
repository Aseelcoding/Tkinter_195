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

    subjects_frame = tk.Frame(root, padx=20, pady=10)
    subjects_frame.pack()

    for index in range(10):
        row = index % 5
        column = (index // 5) * 2

        subject_label = tk.Label(
            subjects_frame,
            text=f"Subject {index + 1}:",
            font=("Arial", 11),
            anchor="w",
            width=12,
        )
        subject_label.grid(row=row, column=column, padx=8, pady=8, sticky="w")

        subject_entry = tk.Entry(subjects_frame, width=18, font=("Arial", 11))
        subject_entry.grid(row=row, column=column + 1, padx=8, pady=8)

    prediction_button = tk.Button(
        root,
        text="Prediction Results",
        font=("Arial", 12, "bold"),
        padx=16,
        pady=8,
    )
    prediction_button.pack(pady=(12, 8))

    result_label = tk.Label(
        root,
        text="Prediction result will appear here.",
        font=("Arial", 12),
        fg="darkblue",
        pady=10,
    )
    result_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
