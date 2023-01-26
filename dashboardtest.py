import random
import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc
from dash import html

# Generate some sample data
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [random.randint(1, 10) for _ in range(5)]}
df = pd.DataFrame(data)

# Create a bar chart
bar_chart = dcc.Graph(
    figure={
        'data': [
            {'x': df['Category'], 'y': df['Value'], 'type': 'bar'}
        ],
        'layout': {
            'title': 'Sample Bar Chart'
        }
    }
)

# Create a pie chart
pie_chart = dcc.Graph(
    figure={
        'data': [
            {'values': df['Value'], 'labels': df['Category'], 'type': 'pie'}
        ],
        'layout': {
            'title': 'Sample Pie Chart'
        }
    }
)

# Assemble the dashboard
app = dash.Dash()
app.layout = html.Div([bar_chart, pie_chart])

# Run the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)