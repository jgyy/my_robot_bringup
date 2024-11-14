from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    robot_stations = [
        Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_giskard",
            parameters=[{"robot_name": "Giskard"}]
        ),
        Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_bb8",
            parameters=[{"robot_name": "BB8"}]
        ),
        Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_daneel",
            parameters=[{"robot_name": "Daneel"}]
        ),
        Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_lander",
            parameters=[{"robot_name": "Lander"}]
        ),
        Node(
            package="my_py_pkg",
            executable="robot_news_station",
            name="robot_news_station_c3po",
            parameters=[{"robot_name": "C3PO"}]
        )
    ]

    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone"
    )

    return LaunchDescription(robot_stations + [smartphone_node])
