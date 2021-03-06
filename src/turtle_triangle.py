#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from math import pi

rospy.init_node('turtle_triangle')

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 1)
rate = rospy.Rate(1)

move_cmd = Twist()
rotate_cmd = Twist()
move_cmd.linear.x = 5
rotate_cmd.angular.z = 2*pi/3

while not rospy.is_shutdown():
    pub.publish(move_cmd)
    rate.sleep()
    pub.publish(rotate_cmd)
    rate.sleep()
