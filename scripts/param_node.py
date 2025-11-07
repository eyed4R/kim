#!/usr/bin/env python3
import rospy

def param_study():
    rospy.init_node('param_study_node')
    rospy.loginfo("=== Чтение параметров ===")
    rosdistro = rospy.get_param('/rosdistro')
    rospy.loginfo("ROS distro: %s", rosdistro)
    try:
        local_param = rospy.get_param('local_param')
        rospy.loginfo("Local param: %s", local_param)
    except KeyError:
        rospy.logwarn("Local param not found, setting default")
        rospy.set_param('local_param', 'default_local_value')
    private_param = rospy.get_param('~private_param', 'default_private_value')
    rospy.loginfo("Private param: %s", private_param)
    rospy.loginfo("=== Запись параметров ===")
    rospy.set_param('~ros_priv_param', 'Hi, I am private =)')
    rospy.set_param('ros_loc_param', 'Hi, I am local =)')
    rospy.set_param('/ros_glob_param', 'Hi, I am global =)')
    
    rospy.loginfo("Parameter study completed!")

if __name__ == '__main__':
    try:
        param_study()
    except rospy.ROSInterruptException:
        rospy.logerr("Parameter study interrupted!")
