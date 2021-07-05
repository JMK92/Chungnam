#include <iostream>
#include<string>

//#include<string.h> //-> namespace 사용하면서 없어짐
//#include<cstring> //-> C언어 스타일 string

using std::string;
using std::cout;
using std::endl;
using std::cin;

int main()
{
	//string str = "hello, World";

	string name;
	cout << "input your name : ";
	cin >> name;
	                                                     //const string greeting = "hello, World " + ", " + name; 
	const string greeting = "hello, World " ", " + name; // 문자열 상수 + 문자열 상수 -> 이렇게 사용 X

	const int pad = 1;
	const int rows = 3 + 2 * pad;
	const string::size_type cols = greeting.size() + 2 * pad + 2;

	for (int i = 0; i < rows; ++i) {// 여백 포함 뒤에 여백도 넣어줘야 함
		string::size_type c = 0;

		while (c != cols){
			if(i == pad + 1 && c == pad + 1){
				cout << greeting;	//greeting
				c += greeting.size();
			}else{
				if(i == 0 || i == rows - 1 || c == 0 || c == cols - 1)
					cout << '*';
				else
					cout << ' ';
				// '*' or ' '
				++c;
			}
		
		}
		//cout <<"*" or " " or greeting
		cout << endl;
	}
	
	//cout << greeting << endl;
	return 0;
}

//class string {
//public:
	//typedef unsigned int size_type;

//}

//rclcpp
//string::size_type
//************************
//*                      *
//* hello world, park    *
//*                      *
//************************

