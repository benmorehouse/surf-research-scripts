import matplotlib.pyplot as plt
import pandas as pd

# Data for women whose primary beach is Manhattan Beach / El Porto
data_women_manhattan = {
    'Factor': ['Personal schedule/work commitments', 'Weather conditions', 
               'Availability of transportation', 'Availability of friends to surf with', 
               'Perceived safety at the beach', 'Mood/mental health', 
               'Physical health', 'Crowdedness of the beach'],
    'Count': [6, 5, 4, 3, 2, 2, 2, 2]
}

# Data for women whose primary beach is Malibu
data_women_malibu = {
    'Factor': ['Personal schedule/work commitments', 'Crowdedness of the beach', 
               'Weather conditions', 'Availability of friends to surf with', 
               'Physical health', 'Availability of rental equipment', 
               'Perceived safety at the beach', 'Mood/mental health'],
    'Count': [14, 10, 10, 6, 2, 2, 1, 1]
}

# Data for men whose primary beach is Manhattan Beach / El Porto
data_men_manhattan = {
    'Factor': ['Personal schedule/work commitments', 'Weather conditions', 
               'Availability of friends to surf with', 'Mood/mental health', 
               'Physical health', 'Availability of transportation', 
               'Crowdedness of the beach', 'Perceived safety at the beach', 
               'Availability of rental equipment'],
    'Count': [12, 10, 10, 6, 6, 6, 4, 3, 2]
}

# Data for men whose primary beach is Malibu
data_men_malibu = {
    'Factor': ['Personal schedule/work commitments', 'Weather conditions', 
               'Availability of transportation'],
    'Count': [2, 1, 1]
}

# Creating dataframes
df_women_manhattan = pd.DataFrame(data_women_manhattan)
df_women_malibu = pd.DataFrame(data_women_malibu)
df_men_manhattan = pd.DataFrame(data_men_manhattan)
df_men_malibu = pd.DataFrame(data_men_malibu)

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].barh(df_women_manhattan['Factor'], df_women_manhattan['Count'], color='pink')
axs[0, 0].set_title('Women - Manhattan Beach / El Porto')
axs[0, 0].invert_yaxis()

axs[0, 1].barh(df_women_malibu['Factor'], df_women_malibu['Count'], color='pink')
axs[0, 1].set_title('Women - Malibu')
axs[0, 1].invert_yaxis()

axs[1, 0].barh(df_men_manhattan['Factor'], df_men_manhattan['Count'], color='blue')
axs[1, 0].set_title('Men - Manhattan Beach / El Porto')
axs[1, 0].invert_yaxis()

axs[1, 1].barh(df_men_malibu['Factor'], df_men_malibu['Count'], color='blue')
axs[1, 1].set_title('Men - Malibu')
axs[1, 1].invert_yaxis()

plt.tight_layout()
plt.show()
