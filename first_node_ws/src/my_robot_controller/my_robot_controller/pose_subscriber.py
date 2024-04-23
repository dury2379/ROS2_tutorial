#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):
    
    def __init__(self):
        super().__init__("pose_subscriber")
        self.pose_subsciber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
    
    def pose_callback(self, msg: Pose):
        self.get_logger().info("\nx: " + str(msg.x) + "\ny: " + str(msg.y) + "\n")

def main(args=None):
    rclpy.init(args=args)
    nd = PoseSubscriber()
    rclpy.spin(nd)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
