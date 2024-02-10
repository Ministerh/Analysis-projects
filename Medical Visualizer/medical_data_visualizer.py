import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('Medical Visualizer\medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight']/ (df['height']/100) ** 2).apply(lambda a: 1 if a > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda a: 0 if a == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda a: 0 if a == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat =  pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat)


    # Get the figure for the output
    fig =plt.gcf()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat =  df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025))
              & (df['height'] <= df['height'].quantile(0.975)) & 
              (df['weight'] >= df['weight'].quantile(0.025)) & 
              (df['weight'] <= df['weight'].quantile(0.975))]
    # use this
    # df_heat=df.query('ap_lo <= ap_hi & height >= height.quantile(0.025) & height <= height.quantile(0.975) & weight >= weight.quantile(0.025) & weight <= weight.quantile(0.975)')

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f',
    center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
