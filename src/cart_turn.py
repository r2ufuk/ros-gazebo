#!/usr/bin/env python
"""Habitat: cart.world"""

import rospy
from gazebo_msgs.srv import ApplyJointEffort

rospy.init_node("cart_turn")


def turn():
    try:
        apply_effort = rospy.ServiceProxy("/gazebo/apply_joint_effort", ApplyJointEffort)

        axle = "cart::link_0_JOINT_12"
        steering_arm = "cart::link_0_JOINT_0"

        rate = rospy.Rate(0.5)

        steer_effort = 200

        while not rospy.is_shutdown():
            steer_effort *= 1.015
            apply_effort(joint_name=axle, effort=50, duration=rospy.Duration(0.5))
            apply_effort(joint_name=steering_arm, effort=steer_effort, duration=rospy.Duration(0.25))
            rate.sleep()

    except rospy.ServiceException as e:
        print(e)


if __name__ == "__main__":
    turn()
