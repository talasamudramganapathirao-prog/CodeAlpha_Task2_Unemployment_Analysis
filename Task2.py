import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Unemployment Data (India Regional Trend & Covid Impact)
data = {
    'Region': ['Andhra Pradesh', 'Andhra Pradesh', 'Andhra Pradesh', 'Telangana', 'Telangana', 'Telangana'],
    'Date': ['2019-12-31', '2020-04-30', '2020-08-31', '2019-12-31', '2020-04-30', '2020-08-31'],
    'Estimated Unemployment Rate (%)': [6.5, 20.5, 12.1, 5.2, 18.2, 10.4],
    'Area': ['Rural', 'Rural', 'Rural', 'Urban', 'Urban', 'Urban']
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Trend Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region', marker='o')
plt.title('Unemployment Rate Trend (COVID-19 Impact Analysis)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()
