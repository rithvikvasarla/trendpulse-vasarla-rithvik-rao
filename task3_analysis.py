
# Import libraries
import pandas as pd
import numpy as np
# STEP 1: Load cleaned CSV file

file_path = "data/trends_20260414.csv"  # change date if needed

try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully")
except Exception as e:
    print("Error loading CSV:", e)
    exit()

# STEP 2: Basic information
print("
Total number of stories:", len(df))

# STEP 3: Average score calculation
avg_score = np.mean(df["score"])
print("Average score of stories:", avg_score)

# STEP 4: Average comments
avg_comments = np.mean(df["num_comments"])
print("Average number of comments:", avg_comments)

# STEP 5: Category-wise analysis
print("
Stories per category:")
category_counts = df["category"].value_counts()
print(category_counts)

# STEP 6: Highest scoring story
top_story = df.loc[df["score"].idxmax()]
print("
Top scoring story:")
print("Title:", top_story["title"])
print("Score:", top_story["score"])

# STEP 7: Most active author
top_author = df["author"].value_counts().idxmax()
print("
Most active author:", top_author)

# STEP 8: Save analysis results
with open("data/analysis_summary.txt", "w") as f:
    f.write(f"Total stories: {len(df)}
")
    f.write(f"Average score: {avg_score}
")
    f.write(f"Average comments: {avg_comments}
")
    f.write("
Stories per category:
")
    f.write(str(category_counts))

print("
Analysis summary saved to data/analysis_summary.txt")
