#!/usr/bin/env python3

#Developed by Andrei Smirnov. 2024
#MSU Rover Team. Voltbro. NIIMech 

from geometry_msgs.msg import Twist
from std_msgs.msg import UInt8MultiArray
from sensor_msgs.msg import JointState
import numpy as np
from math import atan, sqrt, pi
import rclpy
from rclpy.node import Node
import pandas as pd
from time import sleep


lin_vel_gain = 1
ang_vel_gain = .6

wheel_diameter = .2

class test_drive(Node):
    def __init__(self):
        super().__init__('test_drive')
        self.pub = self.create_publisher(Twist, "cmd_vel", 10)

    def send(self):
        twist = Twist()
        twist.linear.x = float(0.4)
        for c in range(200):
            self.pub.publish(twist)
            sleep(.1)
        twist.linear.x = 0.0
        self.pub.publish(twist)




def main(args=None):
    rclpy.init()
    test = test_drive()
    test.send()

    
    test.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()