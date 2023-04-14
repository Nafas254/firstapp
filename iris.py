import streamlit as st
st.text('IRIS')
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

dataset_path='https://frenzy86.s3.eu-west-2.amazonaws.com/fav/iris.data'

df = pd.read_csv(dataset_path, header=None)
df.head()
df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
df
data_columns=['sepal length', 'sepal width','petal length','petal width']
df[data_columns].describe().T
import seaborn as sns
sns.heatmap(df[data_columns].corr(),annot=True)

fig, ax = plt.subplots(figsize=(7,5))
df[data_columns].boxplot()
df[data_columns].hist(figsize=(16,4),layout=(1,6))

