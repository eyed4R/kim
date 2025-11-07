#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

class SummingNode:
    def __init__(self):
        rospy.init_node('summing_node')
        self.poly_sub = rospy.Subscriber('polynomial_result', Int32, self.poly_callback)
        self.final_pub = rospy.Publisher('final_result', Int32, queue_size=10)
        rospy.loginfo("Summing node started")
    def poly_callback(self, msg):
        number = msg.data
        rospy.loginfo("Received number from polynomial: %d", number)
        digit_sum = sum(int(digit) for digit in str(abs(number)))
        
        rospy.loginfo("Sum of digits: %d", digit_sum)
        result_msg = Int32()
        result_msg.data = digit_sum
        self.final_pub.publish(result_msg)

if __name__ == '__main__':
    try:
        node = SummingNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
