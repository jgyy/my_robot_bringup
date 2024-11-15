from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = DeclareLaunchArgument(
        "use_sim_time",
        default_value="false",
        description="Use simulation clock if true"
    )

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="turtlesim",
        output="screen"
    );

    turtle_spawner_node = Node(
        package="my_cpp_pkg",
        executable="turtle_spawner",
        name="turtle_spawner",
        output="screen"
    );

    turtle_controller_node = Node(
        package="my_cpp_pkg",
        executable="turtle_controller",
        name="turtle_controller",
        output="screen"
    );

    return LaunchDescription([
        use_sim_time,
        turtlesim_node,
        turtle_spawner_node,
        turtle_controller_node
    ])
