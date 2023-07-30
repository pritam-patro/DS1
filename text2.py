import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
cities = pd.read_csv("california_cities.csv")
print(cities.head())
seaborn.set()
latitude, longitude = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

# now we will craete a legend, we will plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([latitude], [longitude], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of California Cities")
plt.show()