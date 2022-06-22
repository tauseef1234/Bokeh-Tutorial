# Bokeh-Tutorial
<center><img src = 'https://static.bokeh.org/branding/logos/bokeh-logo.svg' width = 200>
 
Bokeh is a library for creating interactive data visualizations in a web browser. It offers a concise, human-readable syntax, which allows for rapidly presenting data in an aesthetically pleasing manner

## Bokeh Basics
This notebook is a basic tutorial on how to build your first bokeh plot. 
 
Note: The `.ipynb` file in github does not display the plots (refer to this [link](https://stackoverflow.com/questions/32518342/why-my-bokeh-plots-doesnt-work-on-github) for further details). The html version can be found [here](https://tauseef1234.github.io/Bokeh_Basics.html) which show all the bokeh plots.

## Bokeh Part2
This notebook shares steps on how to stack multiple plots in vertical, horizontal or a mix of both alignment. Next, the noteball also shares examples on how to create different type of widgets using bokeh.

Note: The `.ipynb` file in github does not display the plots (refer to this [link](https://stackoverflow.com/questions/32518342/why-my-bokeh-plots-doesnt-work-on-github) for further details). The html version can be found [here](https://tauseef1234.github.io/Bokeh_Part2.html) which show all the bokeh plots.
    
## Bokeh App

Bokeh server makes it easy to create interactive web applications that connect front-end UI events to running Python code. Bokeh creates high-level Python models, such as plots, ranges, axes, and glyphs, and then converts these objects to JSON to pass them to its client library, BokehJS.
    
The `bokeh_app.py` is a sample code which uses:
    
    -  the plots generated in the *Bokeh Basics* notebook 
    -  then uses the concepts of stacking of plots from the *Bokeh Part2* notebook
    -  and shows how to host these plots on a local bokeh server
 
References:
1. https://docs.bokeh.org/en/latest/
2. https://programminghistorian.org/en/lessons/visualizing-with-bokeh
