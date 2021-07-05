#include <iostream>
#include <iomanip> // precision 때문에 사용
#include <string>
#include <vector>
#include<algorithm>

using namespace std;
using std::setprecision;
using std::streamsize;
using std::sort;


int main()
{
	cout << "input your name : ";
	string name;
	cin >> name;

	cout << "input your midterm final score : ";
	double midterm, finalterm;
	cin >> midterm >> finalterm;
	
	cout << "input all your homework score : [followed by EOF] : ";

	vector<double> homeworks;
	double hw;
	while(cin >> hw ){
		homeworks.push_back(hw);
	}

	vector<double>::size_type size = homework.size();
	if(size == 0) {
		cout << endl << "you must input your score." "please try again" << endl;

		return 1;
	}	
	
	sort(homework.begin(), homeworks.end());
	
	double median 
		= ( size % 2 /*! = 0*/ ) ? homeworks[mid] : (homeworks[mid] + homeworks[mid-1]) / 2;
	
	//if(size % 2 != 0){
		//median = homeworks[homeworks.size() / 2];
	//} else {
		//median = homeworks[homeworks.size() / 2] 
	//}

	//double hw;
	//int count = 0;
	//double sum = 0.0;

	//double hw;
	//while (cin >> hw) { // cin 이 while 문 만나면 true False가 됨
		//++count;
		//sum += hw;
	//}
	
	streamsize ss = cout.precision();
	cout << "Your final score : " << setprecision(3) // setprecision은 소수점 
	   <<0.2 * midterm + 0.4 * finalterm + 0.4 *sum / count 
	   << setprecision(ss) << endl; // 다시 되돌리기

	return 0;

}
