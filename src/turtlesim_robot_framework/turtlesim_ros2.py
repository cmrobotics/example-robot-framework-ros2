import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from turtlesim_robot_framework import SelfSpinningNode
from turtlesim.action import RotateAbsolute

class TurtlesimExampleNode(SelfSpinningNode):
    def __init__(self):
        super().__init__('robot_framework_turtlesim_node')
        self.__movement_detected = False
        self.__expecting_to_move = False
        self.reset_succeeded = False
        self.action_sent = False

    def publish_velocity(self, vel):
        move_cmd = Twist()
        move_cmd.linear.x = vel
        self.cmd_vel_publisher.publish(move_cmd)
        self.__movement_detected = False
        self.__expecting_to_move = True

    def cmd_vel_listener_callback(self, pose_msg):
        print("Pose received")
        if self.__expecting_to_move is False:
            return
        self.__movement_detected = True

    def has_moved(self):
        return self.__movement_detected

    def reset_turtle_service(self):
        print('resetting turtle')
        try:
            service_request = Empty.Request()
            while not self.reset_turtle_client.wait_for_service(timeout_sec=1.0):
                print('service not available, waiting...')
            self.reset_turtle_client.call_async(service_request)
            self.reset_succeeded = True
        except:
            self.reset_succeeded = False

    def rotate_turtle_action(self, theta):
        print('rotating turtle')
        goal_orientation = RotateAbsolute.Goal()
        goal_orientation.theta = theta

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_orientation)
        self.action_sent = True


    def setup(self):
        self.cmd_vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.pose_subscription = self.create_subscription(Pose, 'turtle1/pose', self.cmd_vel_listener_callback, 10)
        self.reset_turtle_client = self.create_client(Empty, 'reset')
        self._action_client = ActionClient(self, RotateAbsolute, 'turtle1/rotate_absolute')
        self.start_spinning()

    def teardown(self):
        # Make sure the node is destroyed
        #self.destroy_node()

        # Just to be sure, ask the parent class to stop spinning the executor
        self.stop_spinning()

