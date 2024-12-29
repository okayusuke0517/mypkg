import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

class HoiReceiver(Node):
    def __init__(self):
        super().__init__("HoiReceiver")
        self.sub_count = self.create_subscription(Int16, "countup", self.cb_count, 10)
        self.sub_direction = self.create_subscription(String, "direction", self.cb_direction, 10)

    def cb_count(self, msg):
        self.get_logger().info(f"Received Count: {msg.data} あっち向いてホイ")

    def cb_direction(self, msg):
        self.get_logger().info(f"Received Direction: {msg.data}")

def main():
    rclpy.init()
    node = HoiReceiver()
    rclpy.spin(node)

if __name__ == "__main__":
    main()



