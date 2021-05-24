tvprog = ["Valorant masters 2, iceland", "twitch.tv/tenz", "twitch.tv/acue", "twitch.tv/WARDELL"]
print(tvprog[0])
print(tvprog[1])
print(tvprog[2])
print(tvprog[3])


Newprog = str(input("Enter a new program >>"))
position = int(input("Enter a position between 0 and 4 >>"))

tvprog.insert(position, Newprog)
print(tvprog)
