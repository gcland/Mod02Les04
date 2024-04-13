genres = ['Jazz', "Rock", "Hip-hop", "Classical"]
import random
for x in range (0, 10): #10 is length of playlist
    track = random.choice(genres)
    if track == "Jazz":
        print(track + ". Track #", str(x+1) + "! The smooth sounds of brass instruments.")
    elif track == "Rock":
        print(track + ". Track #", str(x+1) + "! The best of rock and roll.")
    elif track == "Hip-hop":
        print(track + ". Track #", str(x+1) + "! The beats of hip-hop.")
    else:
        print(track + ". Track #", str(x+1) + "! The comtemporary sounds of the soul.")