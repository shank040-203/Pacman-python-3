# PACMAN PYTHON 3

Port of pacman to python 3 using pygame

## SETUP

Install the requirements with

```bash
pip install -r requirements.txt
```

And run the program with

```bash
python game.py
```

## REQUIREMENTS

requirements.txt

```
pygame==2.0.2
```


## GAMEPLAY

Use the arrow keys to move pacman

The objective is to eat all the smaller white squares on the map

The larger white squares make it possible for pacman to eat the ghosts for a short amount of time. Once eaten the ghosts will go to the center box and respawn (Since no animations have been included for this yet, it is a good idea to stay away from the entrance to the box when lesser than 4 ghosts are seen on screen)

Once the first level is complete, it resets the level, makes the ghosts faster and repeats endlessly
