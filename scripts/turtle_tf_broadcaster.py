#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

def handle_turtle_pose(msg):
    # Получаем объект для публикации TF
    br = tf.TransformBroadcaster()
    # Публикуем преобразование между системами координат
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     "turtle1",
                     "world")

if __name__ == '__main__':
    rospy.init_node('tf_turtle_broadcaster')
    rospy.Subscriber('/turtle1/pose',
                     Pose,
                     handle_turtle_pose)
    rospy.loginfo("TF Broadcaster started")
    rospy.spin()
