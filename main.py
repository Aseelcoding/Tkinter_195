import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Aplikasi Prediksi Prodi Pilihan")
    root.geometry("600x680")
    root.minsize(500, 630)

    judul = ttk.Label(
        root,
        text="Aplikasi Prediksi Prodi Pilihan",
        font=("Arial", 16, "bold"),
    )
    judul.pack(pady=20)

    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(pady=10)

    mata_pelajaran = ttk.Label(input_frame, text="Nilai Mata Pelajaran 1:")
    mata_pelajaran.grid(row=0, column=0, sticky="w", pady=5, padx=10)
    entry = ttk.Entry(input_frame, width=20)
    entry.grid(row=0, column=1, pady=5)

    mata_pelajaran_2 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 2:")
    mata_pelajaran_2.grid(row=1, column=0, sticky="w", pady=5, padx=10)
    entry_2 = ttk.Entry(input_frame, width=20)
    entry_2.grid(row=1, column=1, pady=5)

    mata_pelajaran_3 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 3:")
    mata_pelajaran_3.grid(row=2, column=0, sticky="w", pady=5, padx=10)
    entry_3 = ttk.Entry(input_frame, width=20)
    entry_3.grid(row=2, column=1, pady=5)

    mata_pelajaran_4 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 4:")
    mata_pelajaran_4.grid(row=3, column=0, sticky="w", pady=5, padx=10)
    entry_4 = ttk.Entry(input_frame, width=20)
    entry_4.grid(row=3, column=1, pady=5)

    mata_pelajaran_5 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 5:")
    mata_pelajaran_5.grid(row=4, column=0, sticky="w", pady=5, padx=10)
    entry_5 = ttk.Entry(input_frame, width=20)
    entry_5.grid(row=4, column=1, pady=5)

    mata_pelajaran_6 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 6:")
    mata_pelajaran_6.grid(row=5, column=0, sticky="w", pady=5, padx=10)
    entry_6 = ttk.Entry(input_frame, width=20)
    entry_6.grid(row=5, column=1, pady=5)

    mata_pelajaran_7 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 7:")
    mata_pelajaran_7.grid(row=6, column=0, sticky="w", pady=5, padx=10)
    entry_7 = ttk.Entry(input_frame, width=20)
    entry_7.grid(row=6, column=1, pady=5)

    mata_pelajaran_8 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 8:")
    mata_pelajaran_8.grid(row=7, column=0, sticky="w", pady=5, padx=10)
    entry_8 = ttk.Entry(input_frame, width=20)
    entry_8.grid(row=7, column=1, pady=5)

    mata_pelajaran_9 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 9:")
    mata_pelajaran_9.grid(row=8, column=0, sticky="w", pady=5, padx=10)
    entry_9 = ttk.Entry(input_frame, width=20)
    entry_9.grid(row=8, column=1, pady=5)

    mata_pelajaran_10 = ttk.Label(input_frame, text="Nilai Mata Pelajaran 10:")
    mata_pelajaran_10.grid(row=9, column=0, sticky="w", pady=5, padx=10)
    entry_10 = ttk.Entry(input_frame, width=20)
    entry_10.grid(row=9, column=1, pady=5)

    prediction_button = ttk.Button(
        root,
        text="Prediction Results",
    )
    prediction_button.pack(pady=10)

    result_label = ttk.Label(
        root,
        text="Hasil prediksi akan ditampilkan di sini.",
        font=("Arial", 11, "bold"),
    )
    result_label.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
