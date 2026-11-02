import pandas as pd

# Charger le jeu de données
df = pd.read_csv("data/raw/adult.csv")

# Afficher les premières observations
print(df.head())

# Afficher les dimensions du jeu de données
print(df.shape)

#les noms des colonne "variables"
print(df.columns)


#verifier le repartition du variable income
print(df["income"].value_counts())


print(df.info())


print(df.isna().sum())

print(df.duplicated().sum())

print((df["workclass"]=="?").sum())

print((df["occupation"]=="?").sum())