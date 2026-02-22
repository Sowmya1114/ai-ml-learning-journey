import pandas as pd
df = pd.read_csv("students.csv")
passed = df[df["Marks"] >= 40]
failed = df[df["Marks"] < 40]
print("Passed students:")
print(passed)
print("\nFailed students:")
print(failed)
print("\nPass percentage:",
      (len(passed) / len(df)) * 100)
