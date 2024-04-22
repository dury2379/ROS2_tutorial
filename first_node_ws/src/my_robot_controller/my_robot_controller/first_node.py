#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("First_Node")
        self.get_logger().info("Hello from MyNode instance.")
        self.create_timer(1.0, self.timer_callback)
        self.counter_ = 0;
    
    def timer_callback(self):
        self.get_logger().info("Hello #" + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    # Create node
    nd = MyNode()
    rclpy.spin(nd)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
