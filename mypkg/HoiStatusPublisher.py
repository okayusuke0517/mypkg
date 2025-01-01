#!/usr/bin/python3
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
from datetime import datetime
class HoiStatusPublisher(Node):
    def __init__(self):
        super().__init__("HoiStatusPublisher")
        self.pub_game_status = self.create_publisher(String, "game_status", 10)

        # タイマーの間隔を１．０秒に設定
        self.create_timer(1.0, self.publish_status)
        self.n = 0

    def publish_status(self):
            direction = random.choice(["上", "下", "左", "右"])
            current_day = datetime.now().strftime('%A') # 曜日
            current_month = datetime.now().strftime('%B')# 月
            message = f"Round: {self.n}, Direction: {direction}, The day and month we are playing on: {current_day}, {current_month}"            
            status_msg = String()
            status_msg.data = message
            self.pub_game_status.publish(status_msg)
            self.get_logger().info(f"Published: {message}")
            self.n += 1

def main():
    rclpy.init()
    node = HoiStatusPublisher()
    rclpy.spin(node)

if __name__ == "__main__":
    main()




