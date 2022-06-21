import pandas as pd
import os
from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.palettes import Spectral3
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import row, column
from bokeh.io.doc import curdoc

# Read the THOR dataset
df = pd.read_csv('https://query.data.world/s/mp3rupjnvdzmyq4nfbsojbqn354phd',nrows = 50000)

#### First Plot #####

sample = df.sample(50)
# pass the data to columndatasource constructor
source1 = ColumnDataSource(sample)

# define the figure object
p1 = figure()
# add the plot
p1.circle(x='TOTAL_TONS', y='AC_ATTACKING',
         source=source1,
         size=10, color='green')
# decorate the plot
p1.title.text = 'Attacking Aircraft and Munitions Dropped'
p1.xaxis.axis_label = 'Tons of Munitions Dropped'
p1.yaxis.axis_label = 'Number of Attacking Aircraft'

#### Second Plot #####
# manipulate the data to feed into the plot
grouped = df.groupby('COUNTRY_FLYING_MISSION')[['TOTAL_TONS', 'TONS_OF_HE', 'TONS_OF_IC', 'TONS_OF_FRAG']].sum()
grouped = grouped / 1000

# pass the data to columndatasource constructor
source2 = ColumnDataSource(grouped)
# list of y-aixs variables
countries = source2.data['COUNTRY_FLYING_MISSION'].tolist()

# define the figure object
p2 = figure(x_range=countries)

# add the plot
p2.vbar_stack(stackers=['TONS_OF_HE', 'TONS_OF_FRAG', 'TONS_OF_IC'],
             x='COUNTRY_FLYING_MISSION', source=source2,
             legend_label = ['High Explosive', 'Fragmentation', 'Incendiary'],
             width=0.5, color=Spectral3)

# decorate the plot
p2.title.text ='Types of Munitions Dropped by Allied Country'
p2.legend.location = 'top_left'

p2.xaxis.axis_label = 'Country'
p2.xgrid.grid_line_color = None  #remove the x grid lines
p2.y_range.start = 0

p2.yaxis.axis_label = 'Kilotons of Munitions'


sample = df.sample(50)
source = ColumnDataSource(sample)

# Layout the components with the plot in row postion (0) and the other components in a column in row position (1)
layout = row(p1,p2)


                             
# Add the layout to the current document
curdoc().add_root(layout)
curdoc().theme='dark_minimal'                                  