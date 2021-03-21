from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Würfel erzeugen. Standard 6 Seiten
die = Die()

# Rollen und Ergebnisse in 'results' speichern

results = []
for roll_num in range(6000):
    result = die.roll()
    results.append(result)

# Häufigkeiten untersuchen
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Darstellen als .html
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axix_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 6000 times',
                   xaxis=x_axis_config, yaxis=y_axix_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')