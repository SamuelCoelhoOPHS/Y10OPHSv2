
isitraining = ""
windy = "yes"


isitraining = input("Is it raining outside?")

if isitraining == "no":
    print("")
    print("Enjoy your day")
    
    
elif isitraining == "yes": 
    input("Is it windy?")
    
    if windy == "yes":
        print("it is too windy for an umbrella")

    else:
        if windy == "no":
            print ("Take an umbrella")
