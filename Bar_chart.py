import matplotlib.pyplot as plt

# Data
regions = ['North', 'South', 'East', 'West', 'Central']
production = [120, 150, 90, 110, 130]  # in tonnes (example data)

# Plot
plt.figure(figsize=(8,5))
plt.bar(regions, production, color='skyblue', edgecolor='black')
plt.title('Rice Production Across Different Regions')
plt.xlabel('Regions')
plt.ylabel('Production (in tonnes)')
plt.show()
