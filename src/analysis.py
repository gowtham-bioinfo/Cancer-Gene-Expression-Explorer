import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import os

os.makedirs("Outputs", exist_ok=True)

np.random.seed(42)

gene_data = pd.DataFrame(
    np.random.rand(100, 10),
    columns=[f"Gene_{i}" for i in range(10)]
)

labels = pd.DataFrame({
    "sample": [f"S{i}" for i in range(100)],
    "group": ["Cancer"] * 50 + ["Normal"] * 50
})

# PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(gene_data)

pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
pca_df["group"] = labels["group"]

plt.figure()
sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="group")
plt.title("PCA: Cancer vs Normal")
plt.savefig("Outputs/pca_plot.png")
plt.show()

# Heatmap
plt.figure()
sns.heatmap(gene_data.corr())
plt.title("Gene Correlation Heatmap")
plt.savefig("Outputs/heatmap.png")
plt.show()

# Distribution
plt.figure()
gene_data.boxplot()
plt.title("Gene Expression Distribution")
plt.savefig("Outputs/gene_distribution.png")
plt.show()

# Top genes
top_genes = gene_data.var().sort_values(ascending=False).head(10)
print(top_genes)