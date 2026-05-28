import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_employee_dataset.csv")

# Show data
print(df.head())

# Info
print(df.info())

# Summary
print(df.describe())

# Department count
dept_count = df["Department"].value_counts()
print(dept_count)

# Plot
dept_count.plot(kind="bar")
plt.title("Employees by Department")
plt.show()