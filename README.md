Tentu, ini draf lengkap untuk file `README.md` di proyek GitHub Anda, yang menjelaskan cara menggunakan model `best.pt` yang telah Anda latih.

Anda tinggal salin dan tempel (copy-paste) teks di bawah ini ke dalam file `README.md` di repositori GitHub Anda.

-----

# Proyek Deteksi Objek 'Target' dengan YOLOv8

Repositori ini berisi model YOLOv8 yang telah dilatih untuk mendeteksi objek "target" secara spesifik. Model ini menunjukkan performa yang sangat tinggi dengan **mAP@0.5 sebesar 0.995** pada dataset validasi, menjadikannya sangat akurat dan andal.

 \#\# ⚙️ Persyaratan

Pastikan Anda memiliki Python dan `pip` terinstal. Untuk menjalankan model, Anda perlu menginstal pustaka `ultralytics` dan `opencv`.

1.  **Clone Repositori Ini**

    ```bash
    git clone [URL_REPOSITORI_ANDA]
    cd [NAMA_FOLDER_REPOSITORI]
    ```

2.  **Instal Pustaka yang Dibutuhkan**

    ```bash
    pip install ultralytics opencv-python
    ```

-----

## 🚀 Cara Penggunaan

Pastikan file model `best.pt` berada di direktori utama proyek Anda. Berikut adalah sintaks dasar untuk melakukan deteksi menggunakan terminal/command prompt.

### 🖼️ Deteksi pada Gambar

Untuk mendeteksi objek dalam sebuah gambar, gunakan perintah berikut. Ganti `path/to/your/image.jpg` dengan lokasi gambar Anda.

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source="path/to/your/image.jpg" show=True
```

  - `model=best.pt`: Menggunakan file model Anda.
  - `conf=0.5`: Hanya menampilkan deteksi dengan tingkat keyakinan di atas 50%. Anda bisa mengubah nilai ini.
  - `source`: Lokasi file gambar Anda.
  - `show=True`: Menampilkan jendela hasil deteksi secara langsung.

### 📹 Deteksi pada Video

Untuk mendeteksi objek dalam sebuah file video, sintaksnya sangat mirip. Ganti `path/to/your/video.mp4` dengan lokasi video Anda.

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source="path/to/your/video.mp4" show=True
```

### 💻 Deteksi Menggunakan Kamera Live

Anda juga bisa melakukan deteksi secara real-time menggunakan webcam. `source=0` biasanya merujuk pada webcam utama laptop/PC.

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source=0 show=True
```

Tekan tombol `q` untuk menutup jendela kamera.

-----

## 🐍 Contoh Penggunaan dalam Skrip Python

Jika Anda ingin mengintegrasikan model ini ke dalam aplikasi Python, caranya sangat mudah. Buat sebuah file Python (misal: `run_detection.py`) dan gunakan kode di bawah ini.

**Contoh skrip untuk deteksi gambar:**

```python
from ultralytics import YOLO

# Muat model best.pt yang sudah dilatih
model = YOLO('best.pt')

# Tentukan lokasi gambar sumber
sumber_gambar = "path/to/your/image.jpg"

# Lakukan prediksi pada gambar
hasil = model.predict(source=sumber_gambar, conf=0.5, show=True)

# Loop akan berhenti setelah jendela gambar ditutup
print("Deteksi selesai.")

```

**Contoh skrip untuk deteksi via webcam:**

```python
from ultralytics import YOLO

# Muat model best.pt
model = YOLO('best.pt')

# Lakukan prediksi menggunakan webcam (source=0)
# Stream=True direkomendasikan untuk video/stream agar lebih efisien
hasil = model.predict(source=0, show=True, stream=True)

# Karena ini adalah stream, kita perlu loop untuk memprosesnya
# Namun, untuk penggunaan sederhana, show=True sudah cukup
# Kode akan berhenti saat Anda menekan 'q' di jendela webcam
for r in hasil:
    # Anda bisa menambahkan logika tambahan di sini untuk setiap frame
    pass

print("Stream kamera dihentikan.")
```

Selamat mencoba dan mengembangkan proyek ini lebih lanjut\!