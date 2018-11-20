import csv
import numpy as np
import matplotlib.pyplot as plt

categories = [] # strip out the first row of text
installs = [] # push the installs data here
ratings = [] #push the ratings data here

#open the cvs file and parse it 
with open ("data/googeplaystore.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0: # strip the header out
            print('pushing text row to categories array')
            categories.append(row)
            line_count += 1
    else:
        #print("collect the rest of the data")
        ratingsData = (row[2])
        ratingsData = ratingsData.replace("NaN", "0")
        ratings.append(float(ratingsData))

        #print('collect the rest of the data') 
        installData = row[5]
        installData = installData.replace(",", "")
        installData = installData.replace("Free", "0")
        installs.append(int(np.char.strip(installData, "+")))
        line_count += 1

print('processed', line_count, "rows of data")
print('first line', ratings[0])
print('last line', ratings[-1])
#print('first line', installs[0])
#print('last line', installs [-1])

np_ratings = np.array(ratings)

popular_apps = np_ratings > 4
pop_pct = int(len(np_ratings[popular_apps]) / len(np_ratings) * 100)
print(pop_pct)

unpopular_apps = np_ratings < 2
not_pop_pct = int(len(np_ratings[unpopular_apps]) / len(np_ratings) * 100)
print(not_pop_pct)

mid_apps = 100 - (pop_pct + not_pop_pct)

#now we can plot stuff!

labels = "sucks, meh, love it!"
sizes = [not_pop_pct, mid_apps, pop_pct]
colors = ['yellowgreen', 'lightcoral', 'lightskyblue']
explode= (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("do we love our apps?")
plt.xlabel("User Ratings - Google Play Store Installs")
plt.show()

