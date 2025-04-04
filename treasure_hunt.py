name =input("type your name")
print ("welcome", name, "to this Treasure Hunt!")

answer = input(" choose 1 door between the red door and the blue door. so which door are we picking? ")

if answer == "red door":
    answer = input("You open and see a small box full of gold rings and by the side there are keys to a onther door. Whats are you going to pick? If small box full of gold rings type small box and if keys type keys: ").lower()

    if answer == "small box":
        print("Because you picked the small box, you triggered a trap which locks all the doors living you without oxgen. ")
        print("GAME OVER")
    
    elif answer == "keys":
        answer = input("You open the door and see yourself in a desert and it's extremely hot. There is a bottle of water so you can walk if you think you can make it 85km on foot before nightand if you don't make it before night the desert turns in to quicksand or open a door to the unknow as shotcut. Type walk if you are walking, type door if you are opening: ").lower()

        if answer == "walk":
            print("So you decided to take the bottle of water and walk 85 km but little did you know that it was a long distance you could not make it before night time and in the night the sand turns in to quicksand.So you started to sinking slowly and slowly until your head was buried inside the sand and there was no oxygen. ")
            print("GAME OVER")
              
        elif answer == "door":
            answer = input("When you opened the door they gave you only two options either you cross the river which is full of alligators so you can get the treasure or you decide to leave the game so you can go home without any harm. Type cross to cross or type leave to leave the game: ").lower()
                   
            if answer == "cross":
                print("You agreed of wealth got you cute because there was no way you could cross the river without any help.")
                print("GAME OVER")

            elif answer == "leave":
                print("So you decided to go home and not to put your life on risk")
                print("GAME OVER")

                         
if answer == "blue door":
    answer = input("When you opened the blue door you see yourself in your room full of forbidden treasure  and on the other side there is a door which is flaming with fire. type touch if you want to get the treasure or type door: ").lower()

    if answer == "touch":
        print("With the way the treasure looked you decided to take some but not knowing touching the forbidden treasure would turn you into a gold")
        print("GAME OVER")

    elif answer == "door":
        answer = input("You open the door and see yourself at the beach looking at everyone having fun and at the other side there are people digging in the mini.Type beach if you want to have fun or type mini if you want too: ").lower()

        if answer == "beach":
            print("you end up lossing trick of time and you get stuck in the game for ever.")
            print("GAME OVER")

        elif answer == "mini":
            answer = input("You started to digging in the mini and as you go you got lost and could not find your way out so you kept going find yourself in a cave. In this cave there are 2 doors red and blue,1 door takes you straight to the treasure and the other 1 makes you a miner for ever until you die of old age. Type red or blue to open the door: ").lower()

            if answer == "blue":
                print("because you chose the wrong door your life was done for, you will die in that cave because there is no way out of this game now.")
                print("GAME")

            elif answer == "red":
                print("When you opened the door your eyes could not believe what you were looking at, there was so much treasure no man or King has ever owned that much treasure and you were the first one to get such a reward.")
                print("YOU WIN")


            
    

            