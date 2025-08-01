from ultralytics import YOLO

# Arahkan ke file best.pt hasil training Anda
model = YOLO("best.pt")

# Jalankan proses ekspor
results = model.export(format="onnx")

print("Model berhasil diekspor ke format ONNX.")