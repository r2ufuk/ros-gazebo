#!/usr/bin/env python
"""Habitat: cart.world"""

import rospy
from gazebo_msgs.srv import ApplyJointEffort
from pynput import keyboard

rospy.init_node("cart_teleop")

apply_effort = rospy.ServiceProxy("/gazebo/apply_joint_effort", ApplyJointEffort)


def move_forward(effort=75, duration=0.5):
    model_name = "cart::link_0_JOINT_12"

    duration = rospy.Duration(duration)

    apply_effort(joint_name=model_name, effort=effort, duration=duration)


def move_backward(effort=75, duration=0.5):
    move_forward(effort * -1, duration)


def turn_left(effort=400, duration=0.1):
    model_name = "cart::link_0_JOINT_0"

    duration = rospy.Duration(duration)

    apply_effort(joint_name=model_name, effort=effort, duration=duration)


def turn_right(effort=400, duration=0.1):
    turn_left(effort * -1, duration)


def on_press(key):
    keys = ["up", "down", "left", "right"]
    funs = [move_forward, move_backward, turn_left, turn_right]

    key_map = dict(zip(keys, funs))

    if key == keyboard.Key.esc:
        return
    try:
        k = key.char
    except AttributeError:
        k = key.name

    if k in keys:
        key_map[k]()


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
