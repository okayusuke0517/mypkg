import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")

def cb(request, response):
    if request.name == "岡湧育":
        response.age = 70
    else:
        response.age = 255

    return response


def main():
    srv = node.create_service(Query, "query", cb) #サービスの作成     
    rclpy.spin(node)
