
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load CSV file
file_path = "data/trends_20260414.csv"  # change date if needed

try:
    df = pd.read_csv(file_path)
    print("CSV loaded for visualization")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# STEP 2: Stories per category (Bar Chart)
category_counts = df["category"].value_counts()

plt.figure()
category_counts.plot(kind="bar")
plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.savefig("data/category_chart.png")
plt.show()

# STEP 3: Score distribution (Histogram)
plt.figure()
df["score"].plot(kind="hist", bins=10)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("data/score_histogram.png")
plt.show()

# STEP 4: Comments vs Score (Scatter Plot)
plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.savefig("data/score_vs_comments.png")
plt.show()

print("Charts saved in data/ folder")
