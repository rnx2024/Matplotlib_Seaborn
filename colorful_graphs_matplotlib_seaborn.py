import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('C:\\Users\\acer\\Documents\\Work Stuff\\Online Courses Notes\\Python\\env\\shopping_trends.csv')

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
plt.xticks(rotation=45, ha='right')  #  x-axis labels
plt.tight_layout()

# Adding the legend with space between the graph and the label
#for bar, loc in zip(bars, location_sweater_sales['Location']):
    #bar.set_label(loc)
#plt.legend(loc='upper right', bbox_to_anchor=(1.2, 0.5))

plt.show()
