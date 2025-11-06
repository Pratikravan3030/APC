#show the contribution of different energy sources(Pie chart) python program
#compare rice production across diifernt regions(Bar chart) python program

import matplotlib.pyplot as plt

# Data
energy_sources = ['Coal', 'Natural Gas', 'Hydro', 'Nuclear', 'Renewable']
contribution = [40, 25, 15, 10, 10]

# Plot
plt.figure(figsize=(6,6))
plt.pie(contribution, labels=energy_sources, autopct='%1.1f%%', startangle=90)
plt.title('Contribution of Different Energy Sources')
plt.show()
