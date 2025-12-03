import pandas as pd
import matplotlib.pyplot as plt

try:
    processed_df = pd.read_csv('processed_grades.csv')
    print("File verification:processed_grades.csv exist")
except FileNotFoundError:
    print("Execute task B first to generate processed_grades.csv")
    exit(1)

plt.figure(figsize=(10,6))
plt.hist(processed_df['score'], bins=20, color='skyblue', edgecolor='black', alpha=0.8)
plt.axvline(processed_df['score'].mean(), color='red', linestyle='--', linewidth=2)

plt.text(processed_df['score'].mean()+3, 12, f"average score: {processed_df['score'].mean():.2f}", 
         color='red', fontsize=12)
plt.title('Histogram of student performance distribution', fontsize=14, fontweight='bold')
plt.xlabel('fraction', fontsize=12)
plt.ylabel('number of students', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('grade_histogram.png', dpi=300)
print("Generated grade_histogram.png")
plt.show()