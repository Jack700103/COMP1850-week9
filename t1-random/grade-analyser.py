import pandas as pd

df = pd.read_csv('student_grades.csv')
df = df.rename(columns={'Student_ID': 'student_id', 'Grade': 'score'})

average_score = df['score'].mean()
df['passed'] = df['score'] > 70
processed_df = df.sort_values('student_id')

print(f"\naverage score: {average_score:.2f}")
print("\nProcessed data (sorted by student_id):")
print(processed_df)

processed_df.to_csv('processed_grades.csv', index=False)