genres = ['Jazz', "Rock", "Hip-hop", "Classical"]
import random
x = 0
while x < 10:  #10 is length of playlist
    track = random.choice(genres)
    if track == "Jazz":
        print(track + ". Track #", str(x+1) + "! The smooth sounds of brass instruments.")
        x += 1
    elif track == "Rock":
        print(track + ". Track #", str(x+1) + "! The best of rock and roll.")
        x += 1
    elif track == "Hip-hop":
        print(track + ". Track #", str(x+1) + "! The beats of hip-hop.")
        break
    else:
        print(track + ". Track #", str(x+1) + "! The comtemporary sounds of the soul.")
        x += 1