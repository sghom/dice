from plotly.graph_objs import Bar, Layout
from plotly import offline
from die_2 import Die   

die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)

results = []
for value in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3,max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3,max_results+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}

my_layout = Layout(title='Results of rolling three D6 Dice 1000 times.',xaxis=x_axis_config,yaxis=y_axis_config)

offline.plot({'data':data,'layout':my_layout}, filename='d6_d6_d6.html')