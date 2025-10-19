#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

def even_numbers_publisher():
    # Инициализация узла
    rospy.init_node('even_numbers_publisher')
    
    # Получение параметров (если заданы при запуске)
    controller_id = rospy.get_param('~controller_id', 'default')
    max_number = rospy.get_param('~max_number', 100)
    
    # Создание publisher'ов с учетом пространства имен
    even_pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
    overflow_pub = rospy.Publisher('overflow_topic', String, queue_size=10)
    
    # Установка частоты 10 Гц
    rate = rospy.Rate(10)
    
    # Счетчик четных чисел
    even_number = 0
    
    rospy.loginfo("Controller %s started. Max number: %d", controller_id, max_number)
    rospy.loginfo("Publishing even numbers at 10 Hz...")
    
    while not rospy.is_shutdown():
        # Публикация текущего четного числа
        rospy.loginfo("[%s] Publishing even number: %d", controller_id, even_number)
        even_pub.publish(even_number)
        
        # Проверка на достижение максимального числа
        if even_number >= max_number:
            # Создание сообщения о переполнении
            overflow_msg = "Controller %s overflow! Reached %d at time %s" % (controller_id, even_number, rospy.get_time())
            
            # Публикация в топик переполнения
            rospy.logwarn("[%s] OVERFLOW: %s", controller_id, overflow_msg)
            overflow_pub.publish(overflow_msg)
            
            # Сброс счетчика
            even_number = 0
            rospy.loginfo("[%s] Counter reset to 0", controller_id)
        else:
            # Увеличение на 2 для следующего четного числа
            even_number += 2
        
        # Задержка для поддержания частоты 10 Гц
        rate.sleep()

if __name__ == '__main__':
    try:
        even_numbers_publisher()
    except rospy.ROSInterruptException:
        rospy.logerr("Even numbers publisher node interrupted!")
