genres = ['Jazz', "Rock", "Hip-hop", "Classical"]
for x in range(len(genres)): 
    print("Genre {}, {}".format(x+1, genres[x]))
    if genres[x] == "Jazz":
        print("The jazz light show is ready!")
    elif genres[x] == "Rock":
        print("The rock music light show is ready!")
    elif genres[x] == "Hip-hop":
        continue
    elif genres[x] == "Classical":
        print("The classical music light show is ready!")