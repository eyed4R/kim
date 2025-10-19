#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.loginfo("🚨 OVERFLOW ALERT! 🚨")
    rospy.loginfo("Message: %s", msg.data)
    rospy.loginfo("Timestamp: %s", rospy.get_time())
    rospy.loginfo("🔔" * 20)

def overflow_listener():
    rospy.init_node('overflow_listener')
    rospy.Subscriber('overflow_topic', String, overflow_callback, queue_size=10)
    rospy.loginfo("Overflow listener started. Waiting for overflow messages...")
    rospy.spin()

if __name__ == '__main__':
    overflow_listener()
