import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and read the dataset
data = pd.read_csv('/Matplotlib_Seaborn/shopping_trends.csv')

# Filter for sweaters
sweater_data = data[data['Item Purchased'] == 'Sweater']

# Group by Location and count the number of sweaters sold
location_sweater_sales = sweater_data.groupby('Location').size().reset_index(name='Sweaters Sold')

# Create a color palette
palette = sns.color_palette("hsv", len(location_sweater_sales))

# Plotting the bar graph with different colors for each location
plt.figure(figsize=(12, 6))
bars = plt.bar(location_sweater_sales['Location'], location_sweater_sales['Sweaters Sold'], color=palette)
plt.xlabel('Location')
plt.ylabel('Number of Sweaters Sold')
plt.title('Number of Sweaters Sold per Location')
plt.xticks(rotation=45, ha='right')  #  rotates x-axis labels to the right at 45 degrees angle
plt.tight_layout()

plt.show()
