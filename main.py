import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Aplikasi Prediksi Prodi Pilihan")
    root.geometry("850x520")
    root.minsize(750, 470)

    def prediksi_prodi():
        result_label.config(text="Program Studi: Information Technology")

    def hapus_input():
        for entry in entries:
            entry.delete(0, tk.END)
        result_label.config(text="Hasil prediksi akan ditampilkan di sini.")

    judul = ttk.Label(
        root,
        text="Aplikasi Prediksi Prodi Pilihan",
        font=("Arial", 16, "bold"),
    )
    judul.pack(pady=(20, 5))

    petunjuk = ttk.Label(
        root,
        text="Masukkan nilai untuk 10 mata pelajaran, lalu klik Prediction Results.",
    )
    petunjuk.pack(pady=5)

    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack(pady=10)

    entries = []

    for nomor in range(1, 11):
        kolom_grup = 0 if nomor <= 5 else 2
        baris = (nomor - 1) % 5

        mata_pelajaran = ttk.Label(
            input_frame,
            text=f"Nilai Mata Pelajaran {nomor}:",
        )
        mata_pelajaran.grid(
            row=baris,
            column=kolom_grup,
            sticky="w",
            pady=7,
            padx=10,
        )

        entry = ttk.Entry(input_frame, width=15)
        entry.grid(
            row=baris,
            column=kolom_grup + 1,
            pady=7,
            padx=(0, 15),
        )
        entries.append(entry)

    button_frame = ttk.Frame(root)
    button_frame.pack(pady=5)

    prediction_button = ttk.Button(
        button_frame,
        text="Prediction Results",
        command=prediksi_prodi,
    )
    prediction_button.grid(row=0, column=0, padx=5)

    clear_button = ttk.Button(
        button_frame,
        text="Clear Inputs",
        command=hapus_input,
    )
    clear_button.grid(row=0, column=1, padx=5)

    result_label = ttk.Label(
        root,
        text="Hasil prediksi akan ditampilkan di sini.",
        font=("Arial", 11, "bold"),
    )
    result_label.pack(pady=10)

    footer = ttk.Label(
        root,
        text="Prediksi ini hanya menampilkan program studi Teknologi Informasi.",
        font=("Arial", 9),
    )
    footer.pack(pady=(0, 10))

    root.mainloop()


if __name__ == "__main__":
    main()
