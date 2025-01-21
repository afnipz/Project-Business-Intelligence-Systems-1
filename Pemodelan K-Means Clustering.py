# Memilih hanya kolom numerik sebelum menghitung korelasi
numerical_df = df.select_dtypes(include=['number'])

# Menghitung korelasi dan membuat heatmap
plt.figure(figsize=(14, 7))
sns.heatmap(numerical_df.corr(), annot=True, cmap='YlOrBr')
plt.title('Heatmap Korelasi')
plt.show()

# Menghitung jumlah kemunculan setiap nilai dalam kolom 'price'
df["price"].value_counts()

# Menghitung jumlah kemunculan setiap nilai dalam kolom 'review_score'
df["review_score"].value_counts()

# Menghitung jumlah kemunculan setiap nilai dalam kolom 'review_count'
df["review_count"].value_counts()

# Menghitung total penjualan dari bulan 1 hingga bulan 12
df['total_sales'] = df[[f'sales_month_{i}' for i in range(1, 13)]].sum(axis=1)

# Menyimpan DataFrame ke dalam file CSV baru
df.to_csv('ecommerce_sales_analysis_updated.csv', index=False)

# Menghapus beberapa kolom dari DataFrame
columns_to_drop = [f'sales_month_{i}' for i in range(1, 13)]
df.drop(columns=columns_to_drop, axis=1, inplace=True)

# Menampilkan 5 baris pertama dari DataFrame
df.head()

# Menampilkan dimensi DataFrame (jumlah baris dan kolom)
df.shape

# Memilih hanya kolom numerik sebelum menghitung korelasi
numerical_df = df.select_dtypes(include=['number'])

# Menghitung korelasi dan membuat heatmap
plt.figure(figsize=(14, 7))
sns.heatmap(numerical_df.corr(), annot=True, cmap='YlOrBr')
plt.title('Heatmap Korelasi')
plt.show()

# Menghitung Within-Cluster Sum of Squares (WCSS) untuk berbagai jumlah klaster
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)

    # Fit model KMeans pada fitur numerik
    kmeans.fit(numerical_df)
    wcss.append(kmeans.inertia_)

# Plot hasil dengan Metode Elbow
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Inisialisasi variabel untuk menyimpan hasil Silhouette Score
silhouette_scores = []

# Loop untuk mencoba berbagai jumlah kluster (misal dari 2 hingga 10)
# Mulai loop dari 2, bukan 1
for n_clusters in range(2, 11):
    # Membuat model KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)

    # Fit data dan prediksi kluster
    cluster_labels = kmeans.fit_predict(numerical_df)

    # Menghitung Silhouette Score
    score = silhouette_score(numerical_df, cluster_labels)
    silhouette_scores.append(score)

    # print(f"Number of clusters: {n_clusters}, Silhouette Score: {score}")

# Visualisasi Silhouette Score untuk berbagai jumlah kluster
sns.lineplot(x=range(2, 11), y=silhouette_scores, marker='o', color='b')

# Memberikan judul dan label pada plot
plt.title('Silhouette Score vs Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.xticks(range(2, 11))  # Agar tick di sumbu x sesuai dengan jumlah kluster yang diuji
plt.grid(True)

# Menampilkan plot
plt.show()

# Membuat model KMeans dengan 3 klaster
kmeans_final = KMeans(n_clusters=3, init='k-means++', random_state=0)

# Fit model KMeans pada fitur numerik
classlabels = kmeans_final.fit_predict(numerical_df)

# Menambahkan label klaster ke DataFrame
df['clusters'] = classlabels

# Mengubah tipe data kolom 'clusters' menjadi string
df['clusters'] = df['clusters'].astype(str)

# Mengurutkan DataFrame berdasarkan kolom 'clusters'
df = df.sort_values('clusters')

# Menampilkan 5 baris pertama dari DataFrame
df.head()

# Menghitung jumlah kemunculan setiap nilai dalam kolom 'clusters'
df["clusters"].value_counts()

# Membuat figure dengan ukuran yang ditentukan
plt.figure(figsize=(14, 10))

# Membuat histogram untuk kolom 'clusters'
sns.histplot(df['clusters'])

# Menampilkan plot
plt.show()

# Menampilkan koordinat pusat klaster dari model KMeans
kmeans_final.cluster_centers_

# Menyimpan koordinat pusat klaster ke dalam variabel 'centroid'
centroid = kmeans_final.cluster_centers_

# Memilih hanya kolom numerik (misal, 'price', 'review_score')
numerical_cols = df.columns[2:-1]     # asumsi kolom 3 hingga 6 adalah numerik

# Fit KMeans menggunakan hanya kolom-kolom ini
kmeans_final = KMeans(n_clusters=3)   # sesuaikan n_clusters sesuai kebutuhan
kmeans_final.fit(df[numerical_cols])

# Mendapatkan pusat klaster untuk kolom numerik
centroid = kmeans_final.cluster_centers_

# Membuat DataFrame untuk pusat klaster
centroid_df = pd.DataFrame(centroid, columns=numerical_cols)
centroid_df

# Menampilkan statistik deskriptif dari DataFrame
df.describe()
