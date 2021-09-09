import time
import rclpy
from rclpy.node import Node
import threading

from std_msgs.msg import String


class SelfSpinningNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.executor_ = rclpy.executors.SingleThreadedExecutor()
        self.executor_.add_node(self)
        self.executor_thread_ = threading.Thread(target=self.executor_.spin, daemon=True)

    def start_spinning(self):
        self.executor_thread_.start()

class MinimalTalker(SelfSpinningNode):

    def __init__(self):
        super().__init__('minimal_talker')
        self.i = 0
        self.timer = None
        self.publisher_ = None
        self.subscriber_ = None

    def run_timer(self):
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.publish_data)

    def publish_data(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
    
    def hello_callback(self, msg):
        self.get_logger().info('I have just received: {:s}'.format(msg.data))

    def setup(self):
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.subscriber_ = self.create_subscription(String, 'hello', self.hello_callback, 10)
        self.start_spinning()


def main(args=None):
    rclpy.init(args=args)

    instance_self_spinning = SelfSpinningNode('self_spinning')

    minimal_talker = MinimalTalker()
    minimal_talker.setup()
    minimal_talker.publish_data()
    minimal_talker.publish_data()

    time.sleep(10)

    # rclpy.spin_once(minimal_talker, timeout_sec=10.0)
    # rclpy.spin(minimal_talker)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_talker.destroy_node()
    instance_self_spinning.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()