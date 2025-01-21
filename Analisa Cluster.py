# Membuat salinan DataFrame
df2 = df.copy()

# Menampilkan 5 baris pertama dari salinan DataFrame
df2.head()

# Menampilkan statistik deskriptif untuk setiap klaster
clusters = df['clusters'].unique()  # Mendapatkan daftar unik klaster

# Loop untuk setiap klaster
for cluster in clusters:
    # Mencetak judul untuk statistik deskriptif klaster saat ini
    print(f"\nStatistik Deskriptif untuk Klaster {cluster}:")

    # Menampilkan statistik deskriptif dari baris-baris DataFrame yang termasuk dalam klaster saat ini
    print(df[df['clusters'] == cluster].describe())

# Menghitung jumlah data pada setiap klaster
cluster_counts = df['clusters'].value_counts()

# Mengatur ukuran figure
plt.figure(figsize=(8, 5))

# Membuat bar plot
bar_plot = sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette='coolwarm')

# Menambahkan label jumlah di atas setiap batang
for container in bar_plot.containers:
    bar_plot.bar_label(container)

# Menampilkan judul dan label sumbu
plt.title('Jumlah Data pada Setiap Klaster')
plt.xlabel('Klaster')
plt.ylabel('Jumlah Data')

# Menampilkan grafik
plt.show()

# Visualisasi Persentase Data pada Setiap Klaster (Pie Chart)

# Menghitung jumlah data pada setiap klaster
cluster_counts = df['clusters'].value_counts()

# Mengatur ukuran figure untuk plot
plt.figure(figsize=(8, 8))

# Membuat pie chart untuk persentase data pada setiap klaster
plt.pie(cluster_counts.values,
        labels=cluster_counts.index,
        autopct='%1.2f%%',                                          # Menampilkan persentase dengan satu desimal
        startangle=90,                                              # Memulai pie chart dari sudut 90 derajat
        colors=sns.color_palette('coolwarm', len(cluster_counts)))  # Mengatur palet warna

# Mendapatkan current figure
fig = plt.gcf()

# Menambahkan judul pada plot
plt.title('Persentase Data pada Setiap Klaster')

# Menampilkan plot
plt.show()

# Histogram Terpisah untuk Masing-masing Klaster

# Mendapatkan daftar unik klaster
clusters = df['clusters'].unique()

# Mengatur ukuran figure untuk plot
plt.figure(figsize=(12, 8))

# Loop untuk setiap klaster
for cluster in clusters:
    # Membuat subset data untuk klaster saat ini
    subset = df[df['clusters'] == cluster]

    # Membuat histogram untuk kolom 'price' dalam subset data
    sns.histplot(subset['price'], kde=True, label=f'Klaster {cluster}', bins=20)

# Menambahkan judul pada plot
plt.title('Sebaran Harga pada Setiap Klaster')

# Menambahkan label untuk sumbu x
plt.xlabel('Harga')

# Menambahkan label untuk sumbu y
plt.ylabel('Frekuensi')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()

# Histogram Terpisah untuk Masing-masing Klaster

# Mendapatkan daftar unik klaster
clusters = df['clusters'].unique()

# Mengatur ukuran figure untuk plot
plt.figure(figsize=(12, 8))

# Loop untuk setiap klaster
for cluster in clusters:
    # Membuat subset data untuk klaster saat ini
    subset = df[df['clusters'] == cluster]

    # Membuat histogram untuk kolom 'review_score' dalam subset data
    sns.histplot(subset['review_score'], kde=True, label=f'Klaster {cluster}', bins=20)

# Menambahkan judul pada plot
plt.title('Sebaran Nilai Ulasan pada Setiap Klaster')

# Menambahkan label untuk sumbu x
plt.xlabel('Nilai Ulasan')

# Menambahkan label untuk sumbu y
plt.ylabel('Frekuensi')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()

# Histogram Terpisah untuk Masing-masing Klaster

# Mendapatkan daftar unik klaster
clusters = df['clusters'].unique()

# Mengatur ukuran figure untuk plot
plt.figure(figsize=(12, 8))

# Loop untuk setiap klaster
for cluster in clusters:
    # Membuat subset data untuk klaster saat ini
    subset = df[df['clusters'] == cluster]

    # Membuat histogram untuk kolom 'total_sales' dalam subset data
    sns.histplot(subset['total_sales'], kde=True, label=f'Klaster {cluster}', bins=20)

# Menambahkan judul pada plot
plt.title('Sebaran Nilai Ulasan pada Setiap Klaster')

# Menambahkan label untuk sumbu x
plt.xlabel('Nilai Ulasan')

# Menambahkan label untuk sumbu y
plt.ylabel('Frekuensi')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()

# Histogram Terpisah untuk Masing-masing Klaster

# Mendapatkan daftar unik klaster
clusters = df['clusters'].unique()

# Mengatur ukuran figure untuk plot
plt.figure(figsize=(12, 8))

# Loop untuk setiap klaster
for cluster in clusters:
    # Membuat subset data untuk klaster saat ini
    subset = df[df['clusters'] == cluster]

    # Membuat histogram untuk kolom 'total_sales' dalam subset data
    sns.histplot(subset['total_sales'], kde=True, label=f'Klaster {cluster}', bins=20)

# Menambahkan judul pada plot
plt.title('Sebaran Total Penjualan pada Setiap Klaster')

# Menambahkan label untuk sumbu x
plt.xlabel('Total Penjualan')

# Menambahkan label untuk sumbu y
plt.ylabel('Frekuensi')

# Menambahkan legenda pada plot
plt.legend()

# Menampilkan plot
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the file path if needed)
file_path = 'ecommerce_sales_analysis.csv'
df = pd.read_csv(file_path)

# Create a mapping for the clusters based on all categories
category_cluster_map = {
    'Clothing': 0,
    'Sports': 0,
    'Home & Kitchen': 1,
    'Books': 1,
    'Toys': 2,
    'Electronics': 2,
    'Health': 2
}

# Assign clusters based on the new mapping
df['clusters'] = df['category'].map(category_cluster_map)

# Calculate the number of data points in each cluster for each category
cluster_category_counts = df.groupby(['clusters', 'category']).size().unstack(fill_value=0)

# Create grouped bar plot
ax = cluster_category_counts.plot(kind='bar', figsize=(10, 6), colormap='coolwarm')

# Add annotations to each bar
for container in ax.containers:
    ax.bar_label(container, label_type='edge')

# Customize the plot
plt.title('Sebaran Cluster Berdasarkan Kategori Produk')
plt.xlabel('Cluster')
plt.ylabel('Jumlah Data')
plt.xticks(rotation=0)
plt.legend(title='Kategori', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()

# Visualisasi Tren Harga per Cluster (Line Plot)
plt.figure(figsize=(10, 6))
for cluster in clusters:
    subset = df[df['clusters'] == cluster]
    sns.lineplot(x='total_sales', y='price', data=subset, label=f'Cluster {cluster}')

plt.title('Tren Harga Berdasarkan Cluster')
plt.xlabel('Total Sales')
plt.ylabel('Harga')
plt.xticks(rotation=45)
plt.legend()
plt.show()
