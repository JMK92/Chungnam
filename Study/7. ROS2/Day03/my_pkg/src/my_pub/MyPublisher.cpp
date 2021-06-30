#include<chrono>
#include<algorithm> // bind을 사용하기 때문
#include<string>
#include"MyPublisher.h"
using namespace std::chrono_literals; 


MyPublisher::MyPublisher()
:Node("my_pub"), count_(0)
{
    this->publisher_= this->Node::create_publisher<std_msgs::msg::String>("/my_topic", 10);
    this->timer_ = this->create_wall_timer(500ms, std::bind(&MyPublisher::timer_callback, this));
}

rclcpp::TimerBase::SharedPtr timer_;// smart pointer

void MyPublisher::timer_callback()
{
    // std_msgs::msg::String msg;
    auto msg = std_msgs::msg::String();   // auto 사용하면 type이 자동으로 됨  

    msg.data = "hello, world" + std::to_string(count_++); // hello world 1, hello world 2 ..-> 0.5 초마다

    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", msg.data.c_str());

    this->publisher_->publish(msg);
}