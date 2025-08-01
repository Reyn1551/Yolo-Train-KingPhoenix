# Proyek Deteksi Objek 'Target' dengan YOLOv8

Repositori ini berisi model YOLOv8 yang telah dilatih untuk mendeteksi objek "target" secara spesifik. Model ini menunjukkan performa sangat tinggi dengan **mAP@0.5 sebesar 0.995** pada dataset validasi, menjadikannya akurat dan andal untuk berbagai aplikasi.

## ⚙️ Persyaratan

Pastikan Anda memiliki **Python** dan **pip** terinstal. Untuk menjalankan model, Anda perlu menginstal pustaka berikut:

- [ultralytics](https://github.com/ultralytics/ultralytics) (YOLOv8)
- [opencv-python](https://pypi.org/project/opencv-python/) (untuk manipulasi gambar/video)

## 🛠️ Instalasi

1. **Clone Repositori Ini**

    ```bash
    git clone https://github.com/reynboo/YOLO-KINGPHOENIX.git
    cd YOLO-KINGPHOENIX
    ```

2. **Instal Pustaka yang Dibutuhkan**

    ```bash
    pip install ultralytics opencv-python
    ```

## 🚀 Cara Penggunaan

Pastikan file model `best.pt` berada di direktori utama proyek Anda.

### 🖼️ Deteksi pada Gambar

Untuk mendeteksi objek dalam gambar, gunakan perintah berikut di terminal. Ganti `path/to/your/image.jpg` dengan lokasi gambar Anda.

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source="path/to/your/image.jpg" show=True
```

- `model=best.pt`: File model hasil training.
- `conf=0.5`: Threshold confidence (bisa diubah sesuai kebutuhan).
- `source`: Lokasi file gambar.
- `show=True`: Menampilkan hasil deteksi.

### 📹 Deteksi pada Video

Untuk mendeteksi objek dalam video, gunakan:

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source="path/to/your/video.mp4" show=True
```

### 💻 Deteksi Menggunakan Kamera Live

Deteksi real-time menggunakan webcam (biasanya `source=0` untuk webcam utama):

```bash
yolo task=detect mode=predict model=best.pt conf=0.5 source=0 show=True
```

Tekan tombol `q` untuk menutup jendela kamera.

## 🐍 Contoh Penggunaan dalam Skrip Python

Integrasikan model ke aplikasi Python Anda dengan mudah. Berikut contoh skrip untuk deteksi gambar dan webcam.

### Deteksi pada Gambar

```python
from ultralytics import YOLO

# Muat model best.pt
model = YOLO('best.pt')

# Lokasi gambar sumber
sumber_gambar = "path/to/your/image.jpg"

# Prediksi pada gambar
hasil = model.predict(source=sumber_gambar, conf=0.5, show=True)

print("Deteksi selesai.")
```

### Deteksi via Webcam

```python
from ultralytics import YOLO

# Muat model best.pt
model = YOLO('best.pt')

# Prediksi menggunakan webcam (source=0)
hasil = model.predict(source=0, show=True, stream=True)

# Loop untuk setiap frame (opsional)
for r in hasil:
    # Tambahkan logika tambahan di sini jika diperlukan
    pass

print("Stream kamera dihentikan.")
```

## 📁 Struktur Direktori

```
YOLO-KINGPHOENIX/
├── best.pt
├── README.md
├── run_detection.py
├── dataset/
│   ├── images/
│   └── labels/
└── ...
```

## ❓ FAQ

- **Bagaimana cara mengganti model?**  
  Ganti argumen `model=best.pt` dengan nama file model Anda.

- **Bagaimana cara mengubah threshold confidence?**  
  Ubah nilai pada `conf=0.5` sesuai kebutuhan.

- **Bagaimana cara menyimpan hasil deteksi?**  
  Tambahkan argumen `save=True` pada perintah YOLO.

## 📝 Lisensi

Proyek ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan Anda.

---

Selamat mencoba dan semoga sukses