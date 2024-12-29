This is a colorful graph using the pandas, matplotlib and seaborn libraries.  
To load, read, filter and group the dataset, pandas was used. 

<i>pd.read_csv()</i>
<i>data[data['Item Purchased'] == 'Sweater']</i>
<i>data.groupby('Location').size().reset_index(name='Sweaters Sold')</i>

The seaborn color_palette was used to assign individual colors to the different locations
<i>sns.color_palette("hsv", len(location_sweater_sales))</i>

The matplotlib functions used: 
<i>plt.figure()</i>
<i>plt.bar()</i>
<i>plt.xlabel(), plt.ylabel(), plt.title()</i>
<i>plt.xticks(rotation=45, ha='right')</i>
<i>plt.tight_layout()</i>
<i>plt.show()</i>
