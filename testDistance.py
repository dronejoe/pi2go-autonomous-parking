import robot
import pi2go
from time import sleep


def main():
    """
    Function to test the distance sensor
    Pointing at a long wall and taking distance data for small increments of degrees
    """
    rob = robot.Robot()
    distances = [(0, pi2go.getDistance())]

    for i in range(35):
        rob.rotateAngle(2, tolerance=1)
        sleep(1)
        distances.append((5 * (i+1), rob.heading.getHeading(),pi2go.getDistance()))

    # rob.rotateAngle(-50)
    #
    # for i in range(10):
    #     rob.rotateAngle(-5, tolerance=2.5)
    #     sleep(1)
    #     distances.append((-50 + 5 * (i+1), pi2go.getDistance()))

    del rob

    return distances




if __name__ == "__main__":
    data = main()
    print(data)