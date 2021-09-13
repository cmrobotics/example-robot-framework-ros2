from time import time, sleep
from turtlesim_robot_framework import TurtlesimExampleNode

class TurtlesimExampleLibrary(object):
    
    def __init__(self):
        pass

    def that_a_velocity_command_is_published_to_the_turtle(self, vel,  timeout=4.0):
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
            sleep(0.1)

    def send_a_service_call_to_reset_the_turtle(self, timeout=5.0):
        reset_completed = self.ros_turtlesim_node.reset_turtle_service(timeout=timeout)
        if reset_completed is True:
            return True
        else:
            raise Exception("Resetting the turtle failed")

    def send_an_async_service_call_to_reset_the_turtle(self, timeout=5.0):
        future_res = self.ros_turtlesim_node.reset_turtle_service_async(timeout=timeout)
        if future_res is not None:
            now = time()
            timeout_time = now + timeout
            while not future_res.done() and now < timeout_time:
                sleep(0.01)
                print("Waiting for the service call to resolve itself...")
                now = time()
            if (now >= timeout_time):
                raise Exception("Timed out while waiting for the service call to resolve itself")
            return True
        else:
            raise Exception("Resetting the turtle failed")

    def send_an_action_to_rotate_the_turtle(self, orientation):
        orientation = float(orientation)
        self.ros_turtlesim_node.rotate_turtle_action(orientation)
        action_result = self.ros_turtlesim_node.wait_for_action_result(timeout=10.0)
        if action_result is not None:
            return True
        else:
            raise Exception("Rotating the turtle with an action failed")
            

    def Setup(self):
        self.ros_turtlesim_node = TurtlesimExampleNode()
        self.ros_turtlesim_node.setup()
    
    def Teardown(self):
        self.ros_turtlesim_node.teardown()
