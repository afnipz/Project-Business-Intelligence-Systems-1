# Menghapus kolom "product_id" dari DataFrame
df.drop("product_id", axis=1, inplace=True)

# Menampilkan statistik deskriptif dari DataFrame
df.describe()

# Menampilkan nama-nama kolom dari DataFrame
df.columns

# Menghitung jumlah baris duplikat dalam DataFrame
df.duplicated().sum()

# Menghitung jumlah nilai yang hilang (NULL Value) dalam setiap kolom di DataFrame
df.isna().sum()

# Memilih kolom numerik yang akan dicek outlier-nya
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Memvisualisasikan outlier menggunakan boxplot
sns.boxplot(data=df[numerical_columns], orient='h')
plt.title("Boxplot untuk Mendeteksi Outlier")
plt.show()

# Fungsi untuk mendeteksi outlier menggunakan metode IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)  # Kuartil pertama (25%)
    Q3 = df[column].quantile(0.75)  # Kuartil ketiga (75%)
    IQR = Q3 - Q1  # Menghitung rentang interkuartil (IQR)

    # Menentukan batas bawah dan batas atas untuk outlier
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Mendapatkan data yang berada di luar rentang IQR (outlier)
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    # Menampilkan jumlah outlier
    print(f"Kolom {column}: {len(outliers)} outliers berdasarkan IQR")

    return outliers

# Fungsi untuk mendeteksi outlier menggunakan Z-Score
def detect_outliers_zscore(df, column):
    z_scores = np.abs(stats.zscore(df[column]))   # Menghitung Z-Score
    outliers_zscore = df[z_scores > 3]            # Outlier dengan Z-Score lebih dari 3

    print(f"Kolom {column}: {len(outliers_zscore)} outliers berdasarkan Z-Score")

    return outliers_zscore

# Menghitung outlier pada setiap kolom numerik dalam dataset
for column in numerical_columns:
    print(f"\n--- {column} ---")
    detect_outliers_iqr(df, column)     # Menghitung outlier dengan IQR
    detect_outliers_zscore(df, column)  # Menghitung outlier dengan Z-Score
