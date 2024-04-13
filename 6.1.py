genres = ['Jazz', "Rock", "Hip-hop", "Classical"]
sublist = genres[1:1] = ['Country', 'Disco', 'Electronic']
print(genres)
for x in range(len(genres)): 
    track = genres[x]
    print(track)

print("New genres added: ", sublist)