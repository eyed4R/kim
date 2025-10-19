#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard: %s", msg.data)

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('my_chat_topic', String, callback, queue_size=10)
    rospy.loginfo("Listener node started. Waiting for messages...")
    rospy.spin()

if __name__ == '__main__':
    listener()
