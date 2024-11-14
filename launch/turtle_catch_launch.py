from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    spawn_frequency = DeclareLaunchArgument("spawn_frequency", default_value="5.0",
        description="Frequency at which to spawn new turtles")

    catch_distance = DeclareLaunchArgument("catch_distance", default_value="0.5",
        description="Distance threshold for catching turtles")

    return LaunchDescription([
        spawn_frequency,
        catch_distance,
        Node(
            package="turtlesim",
            executable="turtlesim_node",
            name="turtlesim"
        ),
        Node(
            package="my_py_pkg",
            executable="spawner",
            name="turtle_spawner",
            parameters=[{
                "spawn_frequency": LaunchConfiguration('spawn_frequency')
            }]
        ),
        Node(
            package="my_py_pkg",
            executable="controller",
            name="turtle_controller",
            parameters=[{
                "spawn_frequency": LaunchConfiguration('catch_distance')
            }]
        ),
        Node(
            package="my_py_pkg",
            executable="catch_them_all",
            name="catch_them_all",
            parameters=[{
                "spawn_frequency": LaunchConfiguration('catch_distance')
            }]
        )
    ])
