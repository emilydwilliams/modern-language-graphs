import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

preps = pd.read_csv('preps.csv')
print(preps.head())

avg_preps = preps.groupby('Content').Preps.mean().reset_index()
print(avg_preps)
prep = avg_preps['Preps']

avg_plan = preps.groupby('Content')['Off Periods'].mean().reset_index()
print(avg_plan)
plan = avg_plan['Off Periods']

n = 1  # This is our first dataset (out of 2)
t = 2  # Number of datasets
d = 3  # Number of sets of bars
w = 0.8  # Width of each bar
preps_x = [t * element + w * n for element
           in range(d)]

fig = plt.figure()

plt.bar(preps_x, prep, color='tab:orange')

n = 2  # This is our first dataset (out of 2)
t = 2  # Number of datasets
d = 3  # Number of sets of bars
w = 0.8  # Width of each bar
plans_x = [t * element + w * n for element
           in range(d)]

plt.bar(plans_x, plan, color='tab:cyan')


plt.xticks(np.arange(6), ('', 'Core', '', 'Elective', '', 'Language', ''))
plt.legend(['Preps', 'Off Periods'])
plt.title('Preps and Off Periods for Teachers of Different Contexts\nBased on Master Schedule')
plt.ylabel('Average Number of Periods', fontweight='bold')
plt.xlabel('Teaching Context', fontweight='bold')
plt.show()

fig.savefig('prepsplans.png')
