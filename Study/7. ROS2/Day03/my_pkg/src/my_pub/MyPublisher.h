#ifndef MY_PUBLISHER_H
#define MY_PUBLISHER_H
#include<memory> // sharedptr 사용할려면

#include <rclcpp/rclcpp.hpp> // rcl -> robot control library
#include"std_msgs/msg/string.hpp"

class MyPublisher : public rclcpp::Node{
public:
    MyPublisher();


private:    
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;

    rclcpp::TimerBase::SharedPtr timer_;// smart pointer
    int count_;
    void timer_callback(); // 0.5초마다 계속 호출
};

#endif