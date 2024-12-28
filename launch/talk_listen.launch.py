import launch.actions
import launch.substitutions
import launch
import launch_ros.actions


def generate_launch_description():
    # talker ノードを定義
    talker = launch_ros.actions.Node(
        package='mypkg',       # パッケージ名
        executable='talker',   # 実行するノード
    )

    # listener ノードを定義
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen',       # ログを端末に出力
    )

    # LaunchDescription を返す
    return launch.LaunchDescription([
        talker,
        listener,
    ])



