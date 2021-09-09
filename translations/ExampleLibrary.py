from time import time, sleep
from example_calculations import all_calculations
from ros_robot_framework import ExampleVelocityNode
import rclpy


class ExampleLibrary(object):
    
    def __init__(self):
        self.all_calculations = all_calculations.Calculations()
        self.ros_velocity_node = ExampleVelocityNode()

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
            print("The robot did not moved - moved is {:s}. Spinning ROS with a 0.1 timeout...".format(str(moved)))
            rclpy.spin_once(self.ros_velocity_node, timeout_sec=0.1)

        raise Exception("The robot has not moved when it should have")

    def setup(self):
        self.ros_velocity_node.setup()
    
    def teardown(self):
        self.ros_velocity_node.teardown()

    # def subscribing_to_a_topic(self):
    #     self.ros_example_script.cmd_vel_listener_callback()


    # def call_a_service(self):
    # def call_an_action_client(self):
