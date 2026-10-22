import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Aplikasi Prediksi Prodi Pilihan")
    root.geometry("600x400")
    root.minsize(500, 350)

    judul = ttk.Label(
        root,
        text="Aplikasi Prediksi Prodi Pilihan",
        font=("Arial", 16, "bold"),
    )
    judul.pack(pady=20)

    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(pady=10)

    mata_pelajaran = ttk.Label(
        input_frame,
        text="Nilai Mata Pelajaran 1:",
    )
    mata_pelajaran.grid(row=0, column=0, sticky="w", pady=5, padx=10)

    entry = ttk.Entry(input_frame, width=20)
    entry.grid(row=0, column=1, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
