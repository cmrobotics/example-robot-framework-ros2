from time import time, sleep
from example_calculations import all_calculations
from ros_robot_framework import ExampleVelocityNode
import rclpy


class ExampleLibrary(object):
    
    def __init__(self):
        pass

    def check_that_addition_is_larger_than_threshold(self, a, b, threshold):

        if self.all_calculations.addition(int(a), int(b)) > int(threshold):
            print("Addition is larger than threshold")
        else:
            raise Exception("Addition is not larger than threshold")

    def message(self, msg):
        print ('your message is ' + msg)
        return True

    def that_we_publish_a_velocity(self, vel):
        vel = float(vel)
        self.ros_velocity_node.publish_velocity(vel)
        return True

    def verify_that_the_robot_moved(self, timeout=5.0):
        timeout_at = time() + timeout
        while (time() < timeout_at):
            print("Checking if the robot moved...")
            moved = self.ros_velocity_node.has_moved()
            if moved is True:
                return True
            print("The robot did not move - moved is {:s}. I'll give it some time and try again".format(str(moved)))
            sleep(0.1)

        raise Exception("The robot has not moved when it should have")

    def setup(self):
        self.all_calculations = all_calculations.Calculations()
        self.ros_velocity_node = ExampleVelocityNode()
        self.ros_velocity_node.setup()
    
    def teardown(self):
        self.ros_velocity_node.teardown()
