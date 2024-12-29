#!/usr/bin/python3
#SPDX-FileCopyrightText: 2024 Yusuke Oka
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String
import random
from datetime import datetime
class HoiSender(Node):
    def __init__(self):
        super().__init__("HoiSender")
        self.pub_count = self.create_publisher(Int16, "countup", 10)
        self.pub_direction = self.create_publisher(String, "direction", 10)

        # タイマーの間隔を１．５秒に設定
        self.create_timer(1.5, self.timer)
        self.n = 0
        self.toggle = True   # Trueならカウント、Falseなら方向

    def timer(self):
        if self.toggle:
            # カウントメッセージを作成
            count_msg = Int16()
            count_msg.data = self.n
            self.pub_count.publish(count_msg)
            self.n += 1
        else:
            # ランダム方向メッセージと今日の曜日を作成
            direction_msg = String()
            direction = random.choice(["上", "下", "左", "右"])
            current_day = datetime.now().strftime('%A')
            direction_msg.data = f"{direction} - {current_day}"

            self.pub_direction.publish(direction_msg)

        # 次は方向かカウントかを切り替える
        self.toggle = not self.toggle

def main():
    rclpy.init()
    node = HoiSender()
    rclpy.spin(node)

if __name__ == "__main__":
    main()




