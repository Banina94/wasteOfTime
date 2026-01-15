import geopandas as gpd

import matplotlib.pyplot as plt

# Load world map data
url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
world = gpd.read_file(url)

# Filter for North Korea
north_korea = world[world['NAME'] == 'North Korea']

# Create figure and plot
fig, ax = plt.subplots(figsize=(10, 8))
north_korea.plot(ax=ax, color='blue', edgecolor='black')

# Customize the plot
ax.set_title('North Korea', fontsize=16, fontweight='bold')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()