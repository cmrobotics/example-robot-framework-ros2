import threading
from rclpy.executors import SingleThreadedExecutor
from rclpy.node import Node


class SelfSpinningNode(Node):
    def __init__(self, name):
        super().__init__(name)
        self.executor_ = SingleThreadedExecutor()
        self.executor_.add_node(self)
        self.executor_thread_ = threading.Thread(target=self.executor_.spin, daemon=True)

    def start_spinning(self):
        self.executor_thread_.start()

    def stop_spinning(self):
        self.executor_.shutdown()
