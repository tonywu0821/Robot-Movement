from robot.robot import Robot, DIRECTIONS


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
    robot = Robot()
    assert not robot.turn_right()

    robot.place(0, 0, 'EAST')
    assert DIRECTIONS[robot.turn_right()] == "SOUTH"
    assert DIRECTIONS[robot.turn_right()] == "WEST"
    assert DIRECTIONS[robot.turn_right()] == "NORTH"


def test_turn_left():
    robot = Robot()
    assert not robot.turn_left()

    robot.place(0, 0, 'EAST')
    assert DIRECTIONS[robot.turn_left()] == "NORTH"
    assert DIRECTIONS[robot.turn_left()] == "WEST"
    assert DIRECTIONS[robot.turn_left()] == "SOUTH"


def test_move():
    robot = Robot()
    assert not robot.move()

    robot.place(0, 0, 'EAST')
    assert robot.move() == (1, 0)
    assert robot.move() == (2, 0)
    assert robot.move() == (3, 0)
    assert robot.move() == (4, 0)
    assert robot.move() == (4, 0)


def test_place():
    robot = Robot()
    assert robot.place(1, 1, 'EAST')
    assert robot.place(2, 2, 'WEST')
    assert robot.place(3, 3, 'NORTH')
    assert robot.place(4, 4, 'SOUTH')
    assert not robot.place(5, 5, 'SOUTH')


def test_execute():
    robot = Robot()
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


def test_from_files():
    assert True
