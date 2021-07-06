#ifndef MY_PARAM_H
#define MY_PARAM_H
#include<string>
#include <rclcpp/rclcpp.hpp>

class MyParam : public rclcpp::Node{
public:
    MyParam();

private:
    void timer_callback();

    std::string param_value_;

    rclcpp::TimerBase::SharedPtr timer_;
};

#endif