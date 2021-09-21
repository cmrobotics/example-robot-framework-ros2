import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from example_robot_framework import SelfSpinningNode


class ExampleVelocityNode(SelfSpinningNode):
    def __init__(self):
        super().__init__('robot_framework_node')
        self.__movement_detected = False
        self.__expecting_to_move = False

    def publish_velocity(self, vel):
        move_cmd = Twist()
        move_cmd.linear.x = vel
        self.cmd_vel_publisher.publish(move_cmd)
        self.__movement_detected = False
        self.__expecting_to_move = True


    def cmd_vel_listener_callback(self, cmd_msg):
        print("Velocity received")
        if self.__expecting_to_move is False or cmd_msg.linear.x == 0:
            return
        self.__movement_detected = True

    def has_moved(self):
        return self.__movement_detected

    def setup(self):
        print("Setting up from within")
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd_vel_subscription = self.create_subscription(Twist, 'robot_twist', self.cmd_vel_listener_callback, 10)
        self.start_spinning()

    def teardown(self):
        # Just to be sure, ask the parent class to stop spinning the executor
        self.stop_spinning()

        # Make sure the node is destroyed
        self.destroy_node()
