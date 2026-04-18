import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Create Dataset
# -----------------------------
data = {
    "Company": ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS Origin", "Amdocs"],
    "Recruitments": [120, 150, 200, 180, 140, 160, 100, 90]
}

df = pd.DataFrame(data)

# Save dataset (optional for submission)
df.to_csv("recruitment.csv", index=False)

# -----------------------------
# a) Bar Chart
# -----------------------------
plt.figure()
plt.bar(df["Company"], df["Recruitments"])
plt.title("New Recruitments in Companies")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# b) Pie Chart
# -----------------------------
plt.figure()
plt.pie(df["Recruitments"], labels=df["Company"])
plt.title("Recruitment Distribution")
plt.show()

# -----------------------------
# c) Customized Pie Chart
# -----------------------------
plt.figure()
plt.pie(
    df["Recruitments"],
    labels=df["Company"],
    autopct='%1.1f%%',
    explode=[0, 0, 0.1, 0, 0, 0, 0, 0]
)
plt.title("Customized Pie Chart")
plt.show()

# -----------------------------
# d) Doughnut Chart
# -----------------------------
plt.figure()
plt.pie(df["Recruitments"], labels=df["Company"], autopct='%1.1f%%')

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Doughnut Chart")
plt.show()

# -----------------------------
# e) IBM vs Amdocs Comparison
# -----------------------------
ibm = df[df["Company"] == "IBM"]["Recruitments"].values[0]
amdocs = df[df["Company"] == "Amdocs"]["Recruitments"].values[0]

plt.figure()
plt.bar(["IBM", "Amdocs"], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.ylabel("Recruitments")
plt.show()