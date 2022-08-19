import numpy as np
import pandas as pd
whisky = pd.read_csv("whiskies")
whisky["region"] = pd.read_csv("regions")
whisky.head(5)
whisky.iloc[0:10]
whisky.iloc[5:10, 0:5]
whisky.columns
flavors = whisky.iloc[:, 2:14]
flavors

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

import matplotlib.pyplot as plt
plt.Figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose())
corr_whisky
flavors

import matplotlib.pyplot as plt
plt.Figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()
plt.savefig("corr_whisky.pdf")

from sklearn.cluster import SpectralCoclustering
SpectralCoclustering(n_clusters=6, random_state=0)
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
model.rows_
np.sum(model.rows_, axis=1)
np.sum(model.rows_, axis=0)
model.row_labels_


whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose()) 
correlations = np.array(correlations)


plt.Figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")







































