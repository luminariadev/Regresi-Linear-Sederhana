#%%
# Import library dan package yang dibutuhkan
import numpy as np  # untuk perhitungan saintifik
import matplotlib.pyplot as plt  # untuk plotting
from sklearn.linear_model import LinearRegression  # import library LinearRegression dari scikit-learn

#%%
# Membuat data sembarang
penjualan = np.array([6, 5, 5, 4, 4, 3, 2, 2, 2, 1])
harga = np.array([16000, 18000, 27000, 34000, 50000, 68000, 65000, 81000, 85000, 90000])

# %%
# Print data sembarang
print("Data Penjualan :", penjualan)
print("Data Harga :", harga)

# %%
# Visualisasi data scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(penjualan, harga, color='blue', s=100, alpha=0.6, edgecolors='black')
plt.title("Grafik data penjualan dan harga", fontsize=16, fontweight='bold')
plt.xlabel("Penjualan", fontsize=12)
plt.ylabel("Harga", fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig('visualisasi_data_scatter.png', dpi=300, bbox_inches='tight')
plt.show()

#%%
# Membuat model regresi
penjualan_reshaped = penjualan.reshape(-1, 1)  # kita tukar baris dan kolom variabel ini
linreg = LinearRegression()
linreg.fit(penjualan_reshaped, harga)

# Print coefficients
print("\n=== Hasil Model Regresi ===")
print(f"Coefficients (Slope): {linreg.coef_[0]:.2f}")
print(f"Intercept: {linreg.intercept_:.2f}")
print(f"\nPersamaan Regresi: y = {linreg.coef_[0]:.2f}x + {linreg.intercept_:.2f}")

#%%
# Visualisasi plot hasil regresi
plt.figure(figsize=(10, 6))
plt.scatter(penjualan, harga, color='red', s=100, alpha=0.6, edgecolors='black', label='Data Aktual')
plt.plot(penjualan, linreg.predict(penjualan_reshaped), color='blue', linewidth=2, label='Garis Regresi')
plt.title("Visualisasi model regresi data penjualan dan harga", fontsize=16, fontweight='bold')
plt.xlabel("Penjualan", fontsize=12)
plt.ylabel("Harga", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('visualisasi_model_regresi.png', dpi=300, bbox_inches='tight')
plt.show()

# %%
# Prediksi untuk nilai penjualan baru
penjualan_baru = np.array([[3.5], [7]])
harga_prediksi = linreg.predict(penjualan_baru)
print("\n=== Prediksi Harga ===")
for i, p in enumerate(penjualan_baru):
    print(f"Penjualan: {p[0]}, Harga Prediksi: Rp {harga_prediksi[i]:,.0f}")