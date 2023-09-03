# -----------------------
# Import necessary libraries
# -----------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

# -----------------------
# Data Loading and Inspection
# -----------------------

# Load the dataset
data_path = 'train_40k.csv'
data = pd.read_csv(data_path)

# Handle missing values
data['Title'].fillna('Unknown', inplace=True)

# -----------------------
# Data Preprocessing
# -----------------------

# Select the numerical columns for clustering
numerical_columns = ['Score', 'Time']
numerical_data = data[numerical_columns]

# Normalize the data
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(numerical_data)

# -----------------------
# Hierarchical Clustering
# -----------------------

# Take a random sample for dendrogram creation (for computational efficiency)
sample_size = 1000
sample_data = normalized_data[np.random.choice(normalized_data.shape[0], sample_size, replace=False)]

# Generate the linkage matrix
Z = linkage(sample_data, method='ward')

# -----------------------
# Visualization: Dendrogram
# -----------------------

plt.figure(figsize=(12, 6))
dendrogram(Z, truncate_mode='level', p=10)
plt.title('Hierarchical Clustering Dendrogram (Truncated)')
plt.xlabel('Sample Index')
plt.ylabel('Euclidean Distance')
plt.show()

# -----------------------
# Forming Clusters
# -----------------------

# Cut the dendrogram to form clusters
cut_distance = 0.05
clusters = fcluster(Z, cut_distance, criterion='distance')

# -----------------------
# Cluster Analysis
# -----------------------

# Convert sampled data to DataFrame for analysis
sample_df = pd.DataFrame(sample_data, columns=numerical_columns)
sample_df['Cluster'] = clusters

# Calculate cluster characteristics
cluster_summary = sample_df.groupby('Cluster').agg(
    Score_Mean=('Score', 'mean'),
    Score_Std=('Score', 'std'),
    Time_Mean=('Time', 'mean'),
    Time_Std=('Time', 'std')
).reset_index()

# -----------------------
# Visualization: Cluster Scatter Plot
# -----------------------

plt.figure(figsize=(12, 8))
plt.scatter(sample_df['Score'], sample_df['Time'], c=sample_df['Cluster'], cmap='viridis', s=50, alpha=0.6, edgecolors='w', linewidth=0.5)
plt.colorbar().set_label('Cluster')
plt.title('Clusters based on Score and Time')
plt.xlabel('Score (Normalized)')
plt.ylabel('Time (Normalized)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

# -----------------------
# Output
# -----------------------

cluster_summary
