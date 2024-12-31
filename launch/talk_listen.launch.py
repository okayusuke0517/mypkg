import launch.actions
import launch.substitutions
import launch
import launch_ros.actions


def generate_launch_description():
    HoiStatusPublisher = launch_ros.actions.Node(
        package='mypkg',       # パッケージ名
        executable='HoiStatusPublisher',   # 実行するノード
        output='screen'
    )

    # LaunchDescription を返す
    return launch.LaunchDescription([
          HoiStatusPublisher
    ])



