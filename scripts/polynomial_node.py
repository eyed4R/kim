#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

class PolynomialNode:
    def __init__(self):
        rospy.init_node('polynomial_node')
        self.input_sub = rospy.Subscriber('input_numbers', Int32MultiArray, self.input_callback)
        self.output_pub = rospy.Publisher('polynomial_result', Int32, queue_size=10)
        rospy.loginfo("Polynomial node started")
    def input_callback(self, msg):
        numbers = msg.data
        if len(numbers) != 3:
            rospy.logwarn("Expected 3 numbers, got %d", len(numbers))
            return
        rospy.loginfo("Received numbers: %s", numbers)
        result = 0
        for i, num in enumerate(numbers):
            power = i + 1  # 1, 2, 3
            term = num ** power
            result += term
            rospy.loginfo("%d^%d = %d", num, power, term)
        
        rospy.loginfo("Polynomial result: %d", result)
        output_msg = Int32()
        output_msg.data = result
        self.output_pub.publish(output_msg)

if __name__ == '__main__':
    try:
        node = PolynomialNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
