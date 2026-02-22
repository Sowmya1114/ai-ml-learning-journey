import pandas as pd
# Series
s = pd.Series([10, 20, 30, 40])
print(s)
# DataFrame
data = {
    "Name": ["Sowmya", "Ravi", "Anu"],
    "Marks": [85, 72, 90],
    "Age": [22, 23, 21]
}
df = pd.DataFrame(data)
print(df)

# Read CSV
df = pd.read_csv("students.csv")
print(df.head())
# Write CSV
df.to_csv("students_copy.csv", index=False)


df = pd.read_csv("students.csv")
# column
print(df["Marks"])
# condition
print(df[df["Marks"] > 80])
# multiple condition
print(df[(df["Marks"] > 80) & (df["Age"] < 23)])


df = pd.read_csv("students.csv")
print("Average marks:", df["Marks"].mean())
print("Max marks:", df["Marks"].max())
print("Min marks:", df["Marks"].min())
print("Count:", df["Marks"].count())
