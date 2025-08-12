## This is a relaxing fishing adventure... 🐟 Project for kasetsart University

### Initialize the project : 

1. install python

2. ```git clone https://github.com/Hugodesv/ADVENTURING_GAME```

3. run the script and enjoy

### Change form the original game :

- From an intense adventuring game to a relaxing fishing  game
- Use of the random module for fishing
- add of a sleep function to avoid overwork

### How to Play and win condition ? :

- You need to run your script with your IDE or with the command ```python gamedev.py```

In my game the goal (Win condition) is to get the treaasure but unlike most of the games the goal is also to take your time to finish the game and gather a lot of items.

### ***When you start a party you have a choice of 7 commands :***

````go (south,north,west,east)```: Change your zone to catch new fish species !

```fishing``` : catch a random fish between all the species in your zone, BE CAREFULL YOUR ENERGY DICREASE RANDOMLY AFTER EACH CAPTURE BE CAREFULL TO NOT OVERWORK YOURSELF

```sleep``` : important to recover your energy ! In this game you can't loose but its important to be carefull of your health !

```look``` : show my current location informations.

```stats``` : Usefull to know if you're tired or not but when you use this command your energy isn't shown with statistics but only with a sentence so be carefull to listen yourself.

```help``` : display all my commands

```quit``` : end the game

## Playtrought examples : 

### Winning route :
1.  - What do you want to do?  ```fishing```

    - A rock... Useless
    
    - What do you want to do?  ```fishing```

    - Normal Fish ! Continue like that !

    - What do you want to do?  ```go south```
    
    - You're going to the south

    - What do you want to do?  ```look```

                        ============
                        LOCATION: LAKE
                        ============
          a serene lake with crystal-clear water. Fish swim peacefully below.
          exits: north, hidden

    - What do you want to do?  ```go hidden```
    
    - You're going to the hidden
    
    - What do you want to do?  ```look```

                        ===========
                        LOCATION: LEGENDARY WATER WELL
                        ===========
                ... The fishing road in your hands begin   to shine... You are the chosen one

    - What do you want to do?  ```fishing```

    - Treasure Chest you finished the game you are the GOAT of all fishermans

                  =========================================
          🎉 CONGRATULATIONS! YOU WON! 🎉
          You beacame the best and completed your adventure!
          Final Score: ???
          Items Collected: 8
          =========================================