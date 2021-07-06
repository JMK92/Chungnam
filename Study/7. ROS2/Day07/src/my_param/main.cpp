#include "MyParam.h"

int main(int argc, char ** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyParam>());

    rclcpp::shutdown();
    return 0;
}