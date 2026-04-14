
    import pandas as pd
# Loading JSON file 
file_path = "data/trends_20260414.json"

df = pd.read_json(file_path)

print("Original records:", len(df))

# Checking if at least 100 stories
if len(df) < 100:
    print("Not enough stories, rerun Task 1")

# Removing duplicate stories
df = df.drop_duplicates()

# Handles missing values
df["title"] = df["title"].fillna("No Title")
df["author"] = df["author"].fillna("Unknown")
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Clean text
df["category"] = df["category"].str.lower()
df["title"] = df["title"].str.strip()

# Convert types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Saving CSV
csv_file = file_path.replace(".json", ".csv")
df.to_csv(csv_file, index=False)

print("CSV saved:", csv_file)
print("Final records:", len(df))
