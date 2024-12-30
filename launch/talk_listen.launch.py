import launch.actions
import launch.substitutions
import launch
import launch_ros.actions


def generate_launch_description():
    AchiMuiteHoiPublisher = launch_ros.actions.Node(
        package='mypkg',       # パッケージ名
        executable='AchiMuiteHoiPublisher',   # 実行するノード
    )

    # LaunchDescription を返す
    return launch.LaunchDescription([
        AchiMuiteHoiPublisher,
    ])



