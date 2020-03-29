import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from ipywidgets import widgets


df = pd.read_csv('IPIP-FFM-data-8Nov2018/data-final.csv', sep='\t')
scales = ['EXT', 'AGR', 'CSN', 'EST', 'OPN']
labels = ['Extraversion', 'Agreeableness', 'Conscientiousness', \
    'Emotional Stability', 'Intellect or Imagination']
for column in df.columns:
    df = df[~df[column].isna()]
df = df.loc[:5000, :]

for scale in scales:
    df[f'{scale}_sum'] = sum(df[scale + str(i)] for i in range(1, 11))

continious_dimensions = [i + '_sum' for i in scales]
df['Complete score'] = sum([df[i] for i in continious_dimensions])

fig = go.Figure(
    data=go.Parcoords(
        dimensions=[{
            'values': df[continious_dimensions[i]],
            'label': labels[i]} for i in range(5)],
        line={
            'color': df['Complete score'],
            'colorscale': px.colors.sequential.RdBu,
            'showscale': True,
            'reversescale': True
        }
    ))

fig.update_layout(
        title='Big five personality test scores',
        height=600,
        width=1000, 
        hovermode='closest')

fig.write_html('vis.html')
