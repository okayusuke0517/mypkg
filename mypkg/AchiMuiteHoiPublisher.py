#!/usr/bin/python3
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
from datetime import datetime
class AchiMuiteHoiPublisher(Node):
    def __init__(self):
        super().__init__("AchiMuiteHoiPublisher")
        self.pub_game_status = self.create_publisher(String, "game_status", 10)

        # タイマーの間隔を１．０秒に設定
        self.create_timer(1.0, self.publish_status)
        self.n = 0

    def publish_status(self):
            direction = random.choice(["上", "下", "左", "右"])
            current_day = datetime.now().strftime('%A')
            message = f"Round:{self.n} Direction:{direction} The day we are playing:{current_day}"            
            status_msg = String()
            status_msg.data = message
            self.pub_game_status.publish(status_msg)
            self.n += 1

def main():
    rclpy.init()
    node = AchiMuiteHoiPublisher()
    rclpy.spin(node)

if __name__ == "__main__":
    main()




