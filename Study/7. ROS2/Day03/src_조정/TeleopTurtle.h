#ifndef TeleopTurtle_H
#define TeleopTurtle_H

#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

class TeleopTurtle : public rclcpp::Node {
public:
    TeleopTurtle();

    void foward();
    void backward();
    void rotateLeft();
    void rotateRight();

private:   

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    geometry_msgs::msg::Twist msg_;  // 멤버변수로 사용

    void initMsg();       

    void timer_callback();
};

#endif