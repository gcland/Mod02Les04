weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
emotions = ['Happy', 'Sad', 'Energetic', 'Calm']
import random
for i in range(len(weekdays)):
    e_w = random.choice(emotions)
    print("On " + weekdays[i] + " I was " + e_w)

