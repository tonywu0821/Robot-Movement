# Robot-Movement

This program simulates a robot moving on a tabletop with dimensions of 5 units x 5 units.
The robot can roam around the tabletop and be prevented from falling to the ground.
Any command that would cause the robot to fall to the ground will be prevented.


## Technologies
This project is created with:
* Pycharm 
* Python 3.7.0

This project is tested with:
* Pytest 6.2.2

## Usage

Directly execute **robot.py** to interact with this program through commandline.

 Example:
```
$ python robot.py 
```

Use a external file to throw commands to this program.

Example:
```
$ python src/robot/robot -f example.txt
```
## Commands 
Commands can be like the following five:  
```
1. PLACE X,Y,F             # Place the robot. X = postion x, Y = postion y, F = facing.
2. MOVE                    # Move foward a unit.
3. LEFT                    # Turn left.
4. RIGHT                   # Ture right.
5. REPORT                  # Report the position of the robot and its facing.
```

Example:

```
$  python robot.py
Please enter your command: PLACE 1,1,WEST
Please enter your command: LEFT
Please enter your command: MOVE
Please enter your command: REPORT
1,0,SOUTH
```

## Directory Structure

    ├── README.md
    │
    ├── src            
    │   └─── robot      
    │         └── robot.py   # The main application
    │
    │
    │            
    └── tests
        ├── test_robot.py    # Test program contains both unit tests and integration tests.
        │                    # Some of them use a external file. 
        │
        │
        ├── test1            # External files for a integration test
        ├── test1.ans        # Answers for a integration test
        ├── test2            # External files for a integration test   
        └── test2.ans        # Answers for a integration test
        
## Assumptions

The robot can be placed  multiple times and any command will be ignored until the first valid PLACE is entered. 