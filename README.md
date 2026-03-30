# Simple Linear Regression - Machine Learning

Repository ini berisi implementasi Simple Linear Regression menggunakan Python untuk memprediksi nilai berdasarkan hubungan linear antara variabel independen dan dependen.

## 📋 Deskripsi Project

Project ini mengimplementasikan dua modul pembelajaran Simple Linear Regression:

1. **Modul 1**: Menggunakan data sembarang untuk memahami konsep dasar regresi linear
2. **Modul 2**: Menggunakan dataset real (Fuel Consumption CO2) untuk analisis yang lebih mendalam

## 🎯 Tujuan Pembelajaran

- Memahami konsep Supervised Learning
- Memahami dan mengimplementasikan Simple Linear Regression
- Melakukan visualisasi data dan hasil prediksi
- Evaluasi performa model menggunakan metrik yang sesuai

## 📚 Materi

### Supervised Learning

Supervised learning adalah pendekatan dalam machine learning yang menggunakan kumpulan data berlabel untuk melatih algoritma dalam mengklasifikasikan data atau memprediksi hasil secara akurat.

### Regresi Linear

Regresi adalah teknik machine learning untuk memprediksi nilai numerik yang bersifat kontinu. Berbeda dengan klasifikasi yang memprediksi kategori, regresi memprediksi nilai seperti harga, suhu, atau emisi CO2.

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **NumPy** - Perhitungan numerik
- **Matplotlib** - Visualisasi data
- **Pandas** - Manipulasi data
- **Scikit-learn** - Machine learning library

## 📦 Instalasi

1. Clone repository ini:

```bash
git clone https://github.com/username/simple-linear-regression.git
cd simple-linear-regression
```

2. Install dependencies yang diperlukan:

```bash
pip install numpy
pip install matplotlib
pip install scikit-learn
pip install pandas
```

Atau install semua sekaligus:

```bash
pip install -r requirements.txt
```

## 📂 Struktur Project

```
simple-linear-regression/
│
├── modul1_data_sembarang.py          # Implementasi regresi dengan data sembarang
├── modul2_dataset_fuel_consumption.py # Implementasi regresi dengan dataset fuel consumption
├── FuelConsumptionCo2.csv            # Dataset (download terpisah)
├── requirements.txt                   # Dependencies
├── README.md                          # Dokumentasi project
│
└── visualizations/                    # Folder untuk menyimpan hasil visualisasi
    ├── visualisasi_data_scatter.png
    ├── visualisasi_model_regresi.png
    ├── fuel_vs_emission.png
    ├── engine_vs_emission.png
    ├── training_engine_vs_emission.png
    ├── model_regresi_linear.png
    └── prediksi_vs_aktual.png
```

## 🚀 Cara Menggunakan

### Modul 1: Data Sembarang

```bash
python modul1_data_sembarang.py
```

Script ini akan:

- Membuat data penjualan dan harga secara manual
- Memvisualisasikan scatter plot data
- Membuat model regresi linear
- Menampilkan persamaan regresi
- Membuat prediksi untuk nilai baru

### Modul 2: Dataset Fuel Consumption

1. Download dataset dari:

```
https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv
```

2. Letakkan file `FuelConsumptionCo2.csv` di folder yang sama dengan script

3. Jalankan script:

```bash
python modul2_dataset_fuel_consumption.py
```

Script ini akan:

- Membaca dan menganalisis dataset
- Memvisualisasikan hubungan antar variabel
- Membagi data menjadi training dan testing
- Membuat model regresi linear
- Evaluasi model dengan metrik MAE, MSE, dan R²
- Membuat prediksi untuk nilai engine size baru

## 📊 Hasil dan Visualisasi

### Modul 1: Data Sembarang

- Grafik scatter plot: Menampilkan hubungan antara penjualan dan harga
- Model regresi: Garis regresi yang menunjukkan trend linear
- Persamaan regresi: y = mx + c

### Modul 2: Fuel Consumption Dataset

- Analisis korelasi antara Engine Size dan CO2 Emissions
- Perbandingan data aktual vs prediksi
- Metrik evaluasi model (MAE, MSE, R²)

## 📈 Contoh Output

```
=== Hasil Model Regresi ===
Coefficients (Slope): -14777.78
Intercept: 103333.33

Persamaan Regresi: y = -14777.78x + 103333.33

=== Prediksi Harga ===
Penjualan: 3.5, Harga Prediksi: Rp 51,611
Penjualan: 7.0, Harga Prediksi: Rp -893
```

## 🔍 Penjelasan Kode

### Reshape Data

```python
penjualan_reshaped = penjualan.reshape(-1, 1)
```

Reshape diperlukan karena scikit-learn mengharapkan input dalam bentuk 2D array (matrix).

### Fitting Model

```python
linreg = LinearRegression()
linreg.fit(penjualan_reshaped, harga)
```

Proses ini melatih model untuk menemukan garis yang paling sesuai dengan data.

### Coefficients

- **Slope (Koefisien)**: Menunjukkan seberapa besar perubahan Y untuk setiap perubahan 1 unit X
- **Intercept**: Nilai Y ketika X = 0

## 📝 Evaluasi Model

Model dievaluasi menggunakan:

- **MAE (Mean Absolute Error)**: Rata-rata error absolut
- **MSE (Mean Squared Error)**: Rata-rata kuadrat error
- **R² Score**: Koefisien determinasi (0-1, semakin mendekati 1 semakin baik)

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📖 Referensi

- [Scikit-learn Linear Regression Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [IBM Machine Learning Course](https://github.com/Ilham-Fauzi02/Regresi-Linier-Sederhana-ID-)
- [Supervised Learning - IBM](https://www.ibm.com/topics/supervised-learning)

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lebih lanjut.

## 👤 Author

**Nama Anda**

- GitHub: [@username](https://github.luminariadev)

## 🙏 Acknowledgments

- Terima kasih kepada IBM untuk dataset Fuel Consumption
- Terima kasih kepada komunitas scikit-learn
- Materi pembelajaran dari mata kuliah Machine Learning

---

⭐ Jika repository ini bermanfaat, jangan lupa berikan star!

```

## **File 4: requirements.txt**
```

numpy>=1.21.0
matplotlib>=3.4.0
scikit-learn>=1.0.0
pandas>=1.3.0

```

## **File 5: .gitignore**
```

# Python

**pycache**/
_.py[cod]
_$py.class
_.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
_.egg-info/
.installed.cfg
\*.egg

# Jupyter Notebook

.ipynb_checkpoints

# IDEs

.vscode/
.idea/
_.swp
_.swo
\*~

# OS

.DS_Store
Thumbs.db

# Data files

_.csv
_.xlsx
\*.xls

# Images (optional, uncomment if you don't want to track generated images)

# \*.png

# \*.jpg

# \*.jpeg
