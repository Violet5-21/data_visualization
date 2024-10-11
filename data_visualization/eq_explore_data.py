from pathlib import Path
import json
import plotly.express as px
import pandas as pd


# 将数据作为字符串读取并转换为python对象
path = Path('eq_data/1.0_month.geojson')
contents = path.read_text(encoding='utf-8')  # 明确使用utf-8进行编码读取文件
all_eq_data = json.loads(contents)

# 查看数据中的所有地震
all_eq_dicts = all_eq_data['features']
magnitudes, titles, longitudes, latitudes = [], [], [], []
for eq_dict in all_eq_dicts:
    magnitude = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    longitude = eq_dict['geometry']['coordinates'][0]
    latitude = eq_dict['geometry']['coordinates'][1]
    magnitudes.append(magnitude)
    titles.append(title)
    longitudes.append(longitude)
    latitudes.append(latitude)

# 将数据文件转换为更易阅读的版本
path = Path('eq_data/readable_eq_data.json')
readable_contents = json.dumps(all_eq_data, indent=4, ensure_ascii=False)  # 添加ensure_ascii=False以保持非ASCII字符的可读性
path.write_text(readable_contents, encoding='utf-8')  # 写入时也指定编码

# 自定义渐变颜色
custom_colorscale = [(0, 'white'), (0.2, 'blue'), (0.4, 'blue'), (0.6, 'purple'), (0.8, 'red'), (1, 'orange')]

data = pd.DataFrame(
    data=zip(longitudes, latitudes, titles, magnitudes), columns=['longitude', 'latitude', 'title', 'magnitude']
)
data.head()
fig = px.scatter(
    data,
    x='longitude',
    y='latitude',
    range_x=[-180, 180],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='Global Earthquake Scatter Diagram',
    size='magnitude',
    size_max=10,
    color='magnitude',
    color_continuous_scale=custom_colorscale,
    hover_name='title'
)
fig.write_html('global_earthquakes_scatter_diagram.html')
fig.show()
