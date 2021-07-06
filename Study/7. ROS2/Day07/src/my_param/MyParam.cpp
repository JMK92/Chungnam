#include<chrono>
#include<functional>
#include"MyParam.h"

using namespace std::chrono_literals;
using std::bind;

MyParam::MyParam()
:Node("my_param"), param_value_()
{
    this->timer_ = this->create_wall_timer(1000ms, std::bind(&MyParam::timer_callback, this));

    this->declare_parameter<std::string>("my_parameter", "hello");
}

void MyParam::timer_callback()
{
    this->get_parameter("my_parameter", this->param_value_);
    RCLCPP_INFO(this->get_logger(), "my_parameter : %s", this->param_value_.c_str());
}