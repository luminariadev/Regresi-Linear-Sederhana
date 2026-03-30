#%%
# Import library dan package yang dibutuhkan
import pandas as pd  # untuk dataframe
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression  # import library LinearRegression dari scikit-learn

#%%
# Membaca data CSV
df = pd.read_csv("FuelConsumptionCo2.csv")  # membaca data
# melihat 5 baris pertama data
print("=== 5 Baris Pertama Dataset ===")
print(df.head())

#%%
# Informasi dataset
print("\n=== Informasi Dataset ===")
print(df.info())
print("\n=== Statistik Deskriptif ===")
print(df.describe())

#%%
# Kita ambil kolom mana saja yang akan kita analisis
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']]
print("\n=== Data yang Dipilih ===")
print(cdf.head(9))

# %%
# Kita plot hubungannya - Fuel Consumption vs Emission
plt.figure(figsize=(10, 6))
plt.scatter(cdf.FUELCONSUMPTION_CITY, cdf.CO2EMISSIONS, color='blue', alpha=0.5)
plt.xlabel("FUELCONSUMPTION_CITY", fontsize=12)
plt.ylabel("Emission (CO2)", fontsize=12)
plt.title("Hubungan Fuel Consumption City vs CO2 Emissions", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('fuel_vs_emission.png', dpi=300, bbox_inches='tight')
plt.show()

#%%
# Kita plot hubungannya - Engine Size vs Emission
plt.figure(figsize=(10, 6))
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue', alpha=0.5)
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("Emission (CO2)", fontsize=12)
plt.title("Hubungan Engine Size vs CO2 Emissions", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('engine_vs_emission.png', dpi=300, bbox_inches='tight')
plt.show()

# %%
# Membagi data menjadi training dan testing
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

print(f"\n=== Data Splitting ===")
print(f"Total data: {len(cdf)}")
print(f"Data training: {len(train)}")
print(f"Data testing: {len(test)}")

#%%
# Visualisasi data training - Engine Size vs Emission
plt.figure(figsize=(10, 6))
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue', alpha=0.5)
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("Emission (CO2)", fontsize=12)
plt.title("Data Training: Engine Size vs CO2 Emissions", fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig('training_engine_vs_emission.png', dpi=300, bbox_inches='tight')
plt.show()

#%%
# Membuat model regresi
regr = LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x, train_y)

# Koefisien model
print('\n=== Koefisien Model Regresi ===')
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)
print(f'\nPersamaan Regresi: CO2 = {regr.coef_[0][0]:.2f} * EngineSize + {regr.intercept_[0]:.2f}')

# %%
# Plot hasil regresi
plt.figure(figsize=(12, 6))
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue', alpha=0.5, label='Data Training')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r', linewidth=2, label='Garis Regresi')
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("Emission (CO2)", fontsize=12)
plt.title("Model Regresi Linear: Engine Size vs CO2 Emissions", fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('model_regresi_linear.png', dpi=300, bbox_inches='tight')
plt.show()

#%%
# Evaluasi model dengan data testing
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_pred = regr.predict(test_x)

print("\n=== Evaluasi Model ===")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(test_y, test_y_pred):.2f}")
print(f"Mean Squared Error (MSE): {mean_squared_error(test_y, test_y_pred):.2f}")
print(f"R² Score: {r2_score(test_y, test_y_pred):.4f}")

#%%
# Visualisasi prediksi vs aktual
plt.figure(figsize=(12, 6))
plt.scatter(test.ENGINESIZE, test.CO2EMISSIONS, color='blue', alpha=0.5, label='Data Testing (Aktual)')
plt.scatter(test.ENGINESIZE, test_y_pred, color='red', alpha=0.5, label='Prediksi')
plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-g', linewidth=2, label='Garis Regresi')
plt.xlabel("Engine Size", fontsize=12)
plt.ylabel("Emission (CO2)", fontsize=12)
plt.title("Perbandingan Prediksi vs Data Aktual", fontsize=14, fontweight='bold')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.savefig('prediksi_vs_aktual.png', dpi=300, bbox_inches='tight')
plt.show()

# %%
# Prediksi untuk engine size tertentu
engine_sizes_baru = np.array([[2.0], [3.5], [5.0]])
co2_prediksi = regr.predict(engine_sizes_baru)
print("\n=== Prediksi CO2 Emissions untuk Engine Size Baru ===")
for i, size in enumerate(engine_sizes_baru):
    print(f"Engine Size: {size[0]}, CO2 Emissions Prediksi: {co2_prediksi[i][0]:.2f}")