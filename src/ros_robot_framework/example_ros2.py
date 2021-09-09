import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from ros_robot_framework import SelfSpinningNode


class ExampleVelocityNode(SelfSpinningNode):
    def __init__(self):
        super().__init__('robot_framework_node')
        timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.cmd_vel_publisher_callback)
        self.__movement_detected = False
        self.__expecting_to_move = False

    def publish_velocity(self, vel):
        move_cmd = Twist()
        move_cmd.linear.x = vel
        self.cmd_vel_publisher.publish(move_cmd)
        self.__movement_detected = False
        self.__expecting_to_move = True


    def cmd_vel_listener_callback(self, cmd_msg):
        self.get_logger().info(f'Velocity Command Received: {cmd_msg}')
        print("Velocity received")
        if self.__expecting_to_move is False or cmd_msg.linear.x == 0:
            return

        self.__movement_detected = True

    def has_moved(self):
        return self.__movement_detected

    def setup(self):
        self.cmd_vel_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.cmd_vel_subscription = self.create_subscription(Twist, 'robot_twist', self.cmd_vel_listener_callback, 10)
        self.start_spinning()

    def teardown(self):
        pass
