import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")

    client = node.create_client(Query, 'query')
    
    # サービスが利用可能になるまで待機
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('サービスを待機中...')

    # サービスリクエストの作成
    req = Query.Request()
    req.name = "岡湧育"
    
    # 非同期でサービス呼び出し
    future = client.call_async(req)

    # サービス応答を待機
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                # サービスの結果を取得
                response = future.result()
            except Exception as e:
                node.get_logger().info('サービス呼び出しに失敗しました: {}'.format(e))
            else:
                node.get_logger().info("年齢: {}".format(response.age))
            break  # 応答が来たのでループを抜ける

    # ノードの終了処理
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()


