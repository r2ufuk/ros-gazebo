#!/usr/bin/env python
"""Habitat: cart.world"""

import rospy
from gazebo_msgs.srv import ApplyJointEffort

rospy.init_node("cart_forward")


def forward():
    """Habitat: coke.world"""
    try:
        apply_effort = rospy.ServiceProxy("/gazebo/apply_joint_effort", ApplyJointEffort)

        axle = "cart::link_0_JOINT_12"

        duration = rospy.Duration(0.3)

        apply_effort(joint_name=axle, effort=500, duration=duration)

    except rospy.ServiceException as e:
        print(e)


if __name__ == "__main__":
    forward()
