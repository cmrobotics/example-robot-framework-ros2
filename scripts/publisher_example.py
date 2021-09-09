import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class SelfSpinningNode(Node):

    def __init__(self, name, period=0.1):
        super().__init__(name)
        self.__period = period
        self.__timer_spin = self.create_timer(period, self.__spin_callback)
        rclpy.spin_once(self, timeout_sec=self.__period)
        print('Timer created')

    def __spin_callback(self):
        # Multiplying the expected period by an arbitrary constant
        # smaller than 1 to avoid missing the desired spin period.
        # I chose 0.618 because I like the golden ratio.
        rclpy.spin(self)


class MinimalTalker(SelfSpinningNode):

    def __init__(self):
        super().__init__('minimal_talker')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.subscriber_ = self.create_subscription(String, 'hello', self.hello_callback, 10)
        self.i = 0
        self.timer = None

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


def main(args=None):
    rclpy.init(args=args)

    instance_self_spinning = SelfSpinningNode('self_spinning')

    minimal_talker = MinimalTalker()
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