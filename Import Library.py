# Mengimpor pustaka untuk analisis data dan visualisasi

# Install SciPy jika belum terpasang
!pip install scipy

# Mengimpor pustaka yang dibutuhkan
import pandas as pd                          # Digunakan untuk manipulasi dan analisis data
import numpy as np                           # Digunakan untuk operasi numerik dan manipulasi array
import matplotlib.pyplot as plt              # Digunakan untuk membuat visualisasi statis (grafik, plot)
import seaborn as sns                        # Digunakan untuk membuat visualisasi statistik
import plotly.express as px                  # Digunakan untuk membuat visualisasi interaktif
from sklearn.cluster import KMeans,DBSCAN    # Digunakan untuk algoritma clustering
import scipy.stats as stats                  # Digunakan untuk analisis statistik
from sklearn.metrics import silhouette_score # Mengimpor fungsi silhouette_score dari sklearn

# Mendefinisikan nama file yang akan dibaca
file_path = "ecommerce_sales_analysis.csv"

# Membaca file CSV ke dalam DataFrame
df = pd.read_csv(file_path)

# Menampilkan 5 baris pertama dari DataFrame
df.head()

# Menampilkan 5 baris terakhir dari DataFrame
df.tail()

# Menampilkan dimensi DataFrame (jumlah baris dan kolom)
df.shape

# Menampilkan informasi dasar dari DataFrame
# Termasuk jumlah baris dan kolom, tipe data setiap kolom, serta jumlah nilai non-null
df.info()  # Ringkasan dasar

