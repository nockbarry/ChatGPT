# Import necessary libraries
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, CategoricalColorMapper, HoverTool

# Load data into a ColumnDataSource
data = {'fruits': ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries'],
        '2015': [2, 1, 4, 3, 2, 4],
        '2016': [5, 3, 3, 2, 4, 6],
        '2017': [3, 2, 4, 4, 5, 3]}
source = ColumnDataSource(data=data)
fruits = data['fruits']
# Create a figure and plot
plot = figure(x_range=fruits, height=250, title="Fruit Counts by Year",
              toolbar_location=None, tools="")

# Use the CategoricalColorMapper to color the bars based on the fruit type
color_mapper = CategoricalColorMapper(factors=fruits, palette=['#2b83ba', '#abdda4', '#ffffbf',
                                                                '#fdae61', '#d7191c'])
plot.vbar(x='fruits', top='2015', width=0.9, color=dict(field='fruits', transform=color_mapper), legend_label="2015", source=source)
plot.vbar(x='fruits', top='2016', width=0.9, color=dict(field='fruits', transform=color_mapper), legend_label="2016", source=source)
plot.vbar(x='fruits', top='2017', width=0.9, color=dict(field='fruits', transform=color_mapper), legend_label="2017", source=source)

# Add a hover tool to display data when hovering over the bars
hover = HoverTool(tooltips=[('Fruit', '@fruits'),
                            ('2015', '@2015'),
                            ('2016', '@2016'),
                            ('2017', '@2017')])
plot.add_tools(hover)

# Show the plot
show(plot)

