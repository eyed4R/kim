#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Int32MultiArray, Int32

class RequestNode:
    def __init__(self, numbers):
        rospy.init_node('request_node', anonymous=True)
        
        self.numbers = numbers
        self.final_result = None
        self.input_pub = rospy.Publisher('input_numbers', Int32MultiArray, queue_size=10)
        self.result_sub = rospy.Subscriber('final_result', Int32, self.result_callback)
        rospy.loginfo("Request node started with numbers: %s", numbers)
    def result_callback(self, msg):
        self.final_result = msg.data
        rospy.loginfo("Final result received: %d", self.final_result)
        rospy.signal_shutdown("Result received")
    
    def send_request(self):
        rospy.sleep(1)
        input_msg = Int32MultiArray()
        input_msg.data = self.numbers
        self.input_pub.publish(input_msg)
        
        rospy.loginfo("Sent numbers: %s", self.numbers)
        timeout = 10
        start_time = rospy.get_time()
        while not rospy.is_shutdown() and self.final_result is None:
            if rospy.get_time() - start_time > timeout:
                rospy.logerr("Timeout waiting for result")
                break
            rospy.sleep(0.1)
        
        return self.final_result

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: rosrun study_pkg request_node.py <num1> <num2> <num3>")
        sys.exit(1)
    
    try:
        numbers = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
        
        node = RequestNode(numbers)
        result = node.send_request()
        
        if result is not None:
            print(f"Final result: {result}")
        else:
            print("No result received")
            
    except rospy.ROSInterruptException:
        pass
    except ValueError:
        print("Error: All arguments must be integers")
