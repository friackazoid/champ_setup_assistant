from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
                package="champ_setup_assistant",
                executable="setup_assistant.py",
                output="screen"
            )
        ])

