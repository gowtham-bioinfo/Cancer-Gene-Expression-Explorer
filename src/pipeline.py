import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def main():

    base_dir = os.path.dirname(os.path.dirname(__file__))
    outputs = os.path.join(base_dir, "outputs")
    os.makedirs(outputs, exist_ok=True)

    np.random.seed(42)
    X = np.random.rand(100, 50)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    plt.figure()
    sns.heatmap(X_scaled)
    plt.title("Heatmap")
    plt.savefig(os.path.join(outputs, "heatmap.png"))
    plt.close()

    plt.figure()
    plt.scatter(X_pca[:, 0], X_pca[:, 1])
    plt.title("PCA Plot")
    plt.savefig(os.path.join(outputs, "pca_plot.png"))
    plt.close()

    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()