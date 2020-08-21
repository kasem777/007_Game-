print("Welcome to my Game007!")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old.")

health = 10



if age >= 18:
    print("You are old enough to play!")

    weapon = input("pick a weapon (sword/baton/taser):")

    if weapon == sword:
        health = 15


    wants_to_play = input("Do you want to play? ")
    if wants_to_play == "yes":
        print("Let's play!")
        print("You are stating with", health, "health")

        left_or_right = input("First choice... left or right (left.right)?" )
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reach the other side of the lake")

            elif ans == "across":
                print("You manage to get across, but were bit by a fish and lost 5 health")
                health -= 5

            ans = input("You notice a house and a river, which do you go to (ricver/House)? ")

            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lost 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You are survived... You win! ")
            else:
                print("You feel in to the river and lost")
            

        else:
            print("You fell down and lost...")


    else:
        print("Cya...")

else:
    print("You are not old enough to play...")
	


















