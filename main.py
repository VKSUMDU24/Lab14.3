import json
import matplotlib.pyplot as plt

with open('data.json') as f:
    data = json.load(f)

male_count = 0
female_count = 0

for person in data:
    if person['gender'] == 'male':
        male_count += 1
    elif person['gender'] == 'female':
        female_count += 1

labels = ['Male', 'Female']
sizes = [male_count, female_count]
colors = ['blue', 'pink']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')

plt.title('Gender Distribution in the Class')

plt.show()
