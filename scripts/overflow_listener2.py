#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.loginfo("🚨 OVERFLOW DETECTED 🚨")
    rospy.loginfo("Message: %s", msg.data)
    rospy.loginfo("🔔" * 30)

def overflow_listener():
    rospy.init_node('overflow_listener')
    
    # Получение параметра listener_id
    listener_id = rospy.get_param('~listener_id', 'default_listener')
    
    rospy.Subscriber('overflow_topic', String, overflow_callback, queue_size=10)
    rospy.loginfo("Overflow listener %s started. Waiting for overflow messages...", listener_id)
    rospy.spin()

if __name__ == '__main__':
    overflow_listener()
