#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')
print(df.head())

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(x=df['mpg'],
                   y=df['horsepower'],
                   mode='markers',
                   text=df['name'],
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

# create a layout with a title and axis labels
layout = go.Layout(title='mpg versus horsepower',
                   xaxis={'title':'mpg'},
                   yaxis=dict(title='horsepower'),
                   hovermode='closest')


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
