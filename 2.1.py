weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
emotions = ['Happy', 'Sad', 'Energetic', 'Calm']
time = ['Morning', 'Afternoon', 'Evening']
import random
for i in range(len(weekdays)):
    for j in range(len(time)):
        e_w = random.choice(emotions)
        print("On " + weekdays[i], time[j], " I was ", e_w)