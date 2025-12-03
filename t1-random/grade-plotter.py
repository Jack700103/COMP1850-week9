import matplotlib.pyplot as plt

df = pd.read_csv('processed_grades.csv')

plt.figure(figsize=(10,6))
plt.hist(df['score'], bins=20, color='skyblue', edgecolor='black', alpha=0.8)
plt.axvline(df['score'].mean(), color='red', linestyle='--', linewidth=2)

plt.text(df['score'].mean()+3, 12, f'average score: {df["score"].mean():.2f}', 
         color='red', fontsize=12)
plt.title('Histogram of student performance distribution', fontsize=14, fontweight='bold')
plt.xlabel('score', fontsize=12)
plt.ylabel('number of students', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('grade_histogram.png', dpi=300)
plt.show()