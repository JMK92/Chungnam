#include<memory>
#include<rclcpp/rclcpp.hpp>
#include<std_msgs/msg/string.hpp>

//using std_msgs::msg::String; // 헤더 파일에서 이렇게 사용X -> 내가 만든 헤더 파일을 다른 사람이 사용할때 문제가됨

class MySubscriber : public rclcpp::Node {
public:
    MySubscriber();

private:
    //void msg_callback(const String::SharedPtr msg) const;
    void msg_callback(const std_msgs::msg::String::SharedPtr msg) const;  
    // callback 함수 -> 어떤 이벤트가 발생했을때 호출(사용자가 정의)

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    
};
