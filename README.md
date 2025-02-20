# Graph for Sweaters Sold in Different Location

![Image](https://github.com/rnx2024/Matplotlib_Seaborn/blob/main/graphforshoppingtrends.png)

This is a colorful graph using the pandas, matplotlib and seaborn libraries.  
To load, read, filter and group the dataset, pandas was used. 

```
pd.read_csv()</i>
data[data['Item Purchased'] == 'Sweater']</i>
data.groupby('Location').size().reset_index(name='Sweaters Sold')
```

The seaborn color_palette was used to assign individual colors to the different locations

```sns.color_palette("hsv", len(location_sweater_sales))```

The matplotlib functions used: 

```
plt.figure()
plt.bar()
plt.xlabel(), plt.ylabel(), plt.title()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
```
