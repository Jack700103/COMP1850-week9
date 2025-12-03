import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

file_id = "leeds-centre-air-quality"
df = pd.read_csv(f"{file_id}.csv")

columns = [' pm25', ' pm10', ' o3', ' no2']
df = df.rename(columns={
    ' date': 'date',
    ' pm25': 'pm25',
    ' pm10': 'pm10',
    ' o3': 'o3',
    ' no2': 'no2'
}).drop(columns=['Unnamed: 0']) 

df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df = df.sort_values('date')

df['avg_pollution'] = df[columns].mean(axis=1)

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['avg_pollution'], 
         marker='o', linestyle='-', color='#1f77b4', 
         markersize=4, linewidth=1.5)

plt.title('Leeds Central Air Quality - Created by [GuanJie Chen]', fontsize=14, pad=20)
plt.xlabel('Date', fontsize=12, labelpad=10)
plt.ylabel('Average Pollution Index', fontsize=12, labelpad=10)
plt.grid(True, linestyle='--', alpha=0.7)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45, ha='right')

for x,y in zip(df['date'], df['avg_pollution']):
    plt.text(x, y+1, f'{y:.1f}', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig('air_quality_plot.png', dpi=300, bbox_inches='tight')
print('The chart has been saved as air_quality_plot.png')

plt.show()