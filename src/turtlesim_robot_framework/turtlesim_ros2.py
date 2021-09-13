import rclpy
import threading
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
        self.action_result = None
        self.action_result_condition = threading.Condition()

    def publish_velocity(self, vel):
        move_cmd = Twist()
        move_cmd.linear.x = vel
        self.cmd_vel_publisher.publish(move_cmd)
        self.__movement_detected = False
        self.__expecting_to_move = True

    def cmd_vel_listener_callback(self, pose_msg):
        print("pose received")
        if self.__expecting_to_move is False:
            return
        self.__movement_detected = True

    def has_moved(self):
        return self.__movement_detected

    def reset_turtle_service(self, timeout=1.0):
        print('reset turtle')
        try:
            service_request = Empty.Request()
            while not self.reset_turtle_client.wait_for_service(timeout_sec=timeout):
                print('service not available, waiting...')
            self.reset_turtle_client.call(service_request)
            return True
        except:
            return False

    def reset_turtle_service_async(self, timeout=1.0):
        print('resetting turtle')
        try:
            service_request = Empty.Request()
            while not self.reset_turtle_client.wait_for_service(timeout_sec=timeout):
                print('service not available, waiting...')
            return self.reset_turtle_client.call_async(service_request)
        except:
            return None

    def rotate_turtle_action(self, theta):
        print('rotating turtle')
        goal_orientation = RotateAbsolute.Goal()
        goal_orientation.theta = theta

        self._action_client.wait_for_server()
        self.action_result = None
        send_goal_future = self._action_client.send_goal_async(goal_orientation, feedback_callback=self.feedback_callback)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        print('goal response received')
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        print('goal result received')
        with self.action_result_condition:
            self.action_result = future.result().result
            self.get_logger().info('Result: {0}'.format(self.action_result))
            self.action_result_condition.notify()                                                      

    def feedback_callback(self, feedback_msg):
        print('goal feedback received')
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback))

    def wait_for_action_result(self, timeout=None):
        with self.action_result_condition:                                                              
            ret = self.action_result_condition.wait_for(self.action_result_available, timeout=timeout) 
            return self.action_result if ret is True else None

    def action_result_available(self):
        return self.action_result is not None

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

