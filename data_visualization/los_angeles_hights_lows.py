from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


path = Path('weather_data/los angeles_weather_2023.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取最高,最低温度和日期
dates, hights, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[8])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        hights.append(high)
        lows.append(low)

# 根据最高和最低温度绘图
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, hights, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, hights, lows, facecolor='blue', alpha=0.1)

# 设置绘图的格式
ax.set_title('Daily high and low temperatures, 2023\nLos angeles, CA', fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
