from time import time, sleep
from turtlesim_robot_framework import TurtlesimExampleNode

class TurtlesimExampleLibrary(object):
    
    def __init__(self):
        pass

    def that_a_velocity_command_is_published_to_the_turtle(self, vel,  timeout=5.0):
        vel = float(vel)
        timeout_at = time() + timeout
        while (time() < timeout_at):
            self.ros_turtlesim_node.publish_velocity(vel)
        return True

    def verify_that_the_turtle_moved(self, timeout=5.0):
        timeout_at = time() + timeout
        while (time() < timeout_at):
            print("Checking if the robot moved...")
            moved = self.ros_turtlesim_node.has_moved()
            if moved is True:
                return True
            print("The robot did not move - moved is {:s}. I'll give it some time and try again".format(str(moved)))
            sleep(0.1)

    def send_a_service_call_to_reset_the_turtle(self, timeout=5.0):
        self.ros_turtlesim_node.reset_turtle_service()
        reset_completed = self.ros_turtlesim_node.reset_succeeded
        if reset_completed is True:
            return True
        else:
            raise Exception("Resetting the turtle failed")

    def send_an_action_to_rotate_the_turtle(self, orientation):
        orientation = float(orientation)
        rotation_action_client = self.ros_turtlesim_node.rotate_turtle_action(orientation)
        action_completed = self.ros_turtlesim_node.action_sent
        if action_completed is True:
            return True
        else:
            raise Exception("Rotating the turtle with an action failed")
            

    def Setup(self):
        self.ros_turtlesim_node = TurtlesimExampleNode()
        self.ros_turtlesim_node.setup()
    
    def Teardown(self):
        self.ros_turtlesim_node.teardown()
