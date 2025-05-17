from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1.1 load
X, y = fetch_openml('Fashion-MNIST', version=1, return_X_y=True, as_frame=False)

# 1.2 normalise to [0,1]
X = X.astype("float32") / 255.0          # (70 000 × 784)

# 1.3 nothing is missing → OK

# 1.4 split 80 / 20
X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(int), test_size=0.20, stratify=y, random_state=42)
