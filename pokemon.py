
inicialpoke = input("Who choose to fight with? (Squirtle, Bulbasaur or Charmander): ")

vida_pikachu = 100
vida_enemigo = 0

if inicialpoke == "Squirtle":
    vida_enemigo = 90
    namepoke = "Squirtle"
    pokeattack = 8

elif inicialpoke == "Bulbasaur":
    vida_enemigo = 80
    namepoke = "Squirtle"
    pokeattack = 7

elif inicialpoke == "Charmander":
    vida_enemigo = 100
    namepoke = "Squirtle"
    pokeattack = 10

while vida_pikachu > 0 and vida_enemigo > 0 :
    ataque_pikachu = input("Which attack do you want to do? (Thunderbolt or Thunder Shock): ")
    
    if ataque_pikachu == "Thunderbolt":
        print("You made 10 ps of damage to the enemy")
        vida_enemigo -= 10
    elif ataque_pikachu == "Thunder Shock":
        print("You made 12 ps of damage to the enemy")
        vida_enemigo -= 12

    print("The ps bar of the enemy is of {}".format(vida_enemigo))

    print("{} made you {} ps of damage".format(namepoke, pokeattack))
    vida_pikachu -= pokeattack

    print("Your ps bar is of {}".format(vida_pikachu))

if vida_enemigo < vida_pikachu:
    print("{} it has weakened, you win".format(namepoke))
elif vida_pikachu < vida_enemigo:
    print("Pikachu it has weakened, you lose")
