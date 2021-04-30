from robot.robot import Robot, DIRECTIONS

# The start of the unit tests


def test_is_valid_position():
    assert Robot.is_valid_position(0, 0)
    assert Robot.is_valid_position(1, 1)
    assert Robot.is_valid_position(2, 2)
    assert Robot.is_valid_position(3, 3)
    assert Robot.is_valid_position(4, 4)
    assert not Robot.is_valid_position(5, 5)
    assert not Robot.is_valid_position(-1, -5)
    assert not Robot.is_valid_position('a', 'b')


def test_is_valid_direction():
    assert Robot.is_valid_direction('EAST')
    assert Robot.is_valid_direction('SOUTH')
    assert Robot.is_valid_direction('WEST')
    assert Robot.is_valid_direction('NORTH')

    assert not Robot.is_valid_direction('Hi,')
    assert not Robot.is_valid_direction('how')
    assert not Robot.is_valid_direction('are')
    assert not Robot.is_valid_direction('you?')


def test_is_valid_command():
    assert Robot.is_valid_command('PLACE 2,2,NORTH')
    assert Robot.is_valid_command('PLACE 2  , 2 , NORTH')
    assert Robot.is_valid_command('LEFT')
    assert Robot.is_valid_command('RIGHT')
    assert Robot.is_valid_command('MOVE')
    assert Robot.is_valid_command('REPORT')

    assert not Robot.is_valid_command('PLACE 2,2,2')
    assert not Robot.is_valid_command(' LEFT ')
    assert not Robot.is_valid_command('RIGHT ')
    assert not Robot.is_valid_command('MOV E')
    assert not Robot.is_valid_command('  REPORT')
    assert not Robot.is_valid_command('MOVE ')


def test_turn_right():
    robot = Robot(verbose=False)
    assert not robot.turn_right()

    robot.place(0, 0, 'EAST')
    assert robot.turn_right() == "SOUTH"
    assert robot.turn_right() == "WEST"
    assert robot.turn_right() == "NORTH"


def test_turn_left():
    robot = Robot(verbose=False)
    assert not robot.turn_left()

    robot.place(0, 0, 'EAST')
    assert robot.turn_left() == "NORTH"
    assert robot.turn_left() == "WEST"
    assert robot.turn_left() == "SOUTH"


def test_move():
    robot = Robot(verbose=False)
    assert not robot.move()

    robot.place(0, 0, 'EAST')
    assert robot.move() == (1, 0)
    assert robot.move() == (2, 0)
    assert robot.move() == (3, 0)
    assert robot.move() == (4, 0)
    assert robot.move() == (4, 0)


def test_place():
    robot = Robot(verbose=False)
    assert robot.place(1, 1, 'EAST')
    assert robot.place(2, 2, 'WEST')
    assert robot.place(3, 3, 'NORTH')
    assert robot.place(4, 4, 'SOUTH')
    assert not robot.place(5, 5, 'SOUTH')


def test_execute():
    robot = Robot(verbose=False)
    assert not robot.execute('WRONG COMMAND1!')
    assert robot.execute('PLACE 1,1,EAST')
    assert robot.position_x == 1 and robot.position_y == 1
    assert robot.execute('LEFT')
    assert DIRECTIONS[robot.facing] == 'NORTH'
    assert robot.execute('RIGHT')
    assert DIRECTIONS[robot.facing] == 'EAST'
    assert robot.execute('MOVE')
    assert robot.execute('MOVE')
    assert not robot.execute('WRONG COMMAND2!!')
    assert robot.execute('MOVE')
    assert robot.execute('MOVE')
    assert not robot.execute('WRONG COMMAND3!!')
    assert robot.position_x == 4 and robot.position_y == 1

# The end of the unit tests


# The start of the integration test


def test_normal_report():
    robot = Robot(verbose=False)
    commands = ["PLACE 2,1,EAST", "MOVE", "REPORT", "MOVE", "LEFT", "REPORT",
                "WRONG", "LEFT", "WRONG", "MOVE", "REPORT"]
    answers = ["3,1,EAST", "4,1,NORTH", "3,1,WEST"]
    i = 0
    for command in commands:
        res = robot.execute(command)
        if command == "REPORT":
            assert res == answers[i]
            i += 1


def test_invalid_report():
    robot = Robot(verbose=False)
    commands = ["PLACE 10,10,NORTH", "REPORT", "REPORT",
                "PLACE 3,3,EAST", "MOVE", "MOVE", "LEFT",
                "REPORT", "WRONG", "LEFT", "WRONG", "MOVE", "REPORT"]
    answers = ["", "", "4,3,NORTH", "3,3,WEST"]
    i = 0
    for command in commands:
        res = robot.execute(command)
        if command == "REPORT":
            assert res == answers[i]
            i += 1


def test__from_input_file_1():
    robot = Robot(verbose=False)
    with open('test1.ans') as f:
        expected_output = f.read().splitlines()
    i = 0
    with open('test1', 'r') as f:
        commands = f.read().splitlines()
        for command in commands:
            if len(command) > 0:
                res = robot.execute(command)
                if command == "REPORT":
                    assert res == expected_output[i]
                    i += 1


def test__from_input_file_2():
    robot = Robot(verbose=False)
    with open('test2.ans') as f:
        expected_output = f.read().splitlines()
    i = 0
    with open('test2', 'r') as f:
        commands = f.read().splitlines()
        for command in commands:
            if len(command) > 0:
                res = robot.execute(command)
                if command == "REPORT":
                    assert res == expected_output[i]
                    i += 1

# The end of the integration test
