#include <iostream>
#include <iomanip> // precision 때문에 사용
#include <string>
#include <vector>
#include<algorithm>

using namespace std;
using std::cerr;
using std::istream;
using std::setprecision;
using std::streamsize;
using std::sort;
using std::domain_error;

double median(vector<double> vec)
{
	if(vec.size() == 0) {
		throw domain_error("vector is empty");
	}
		
	sort(vec.begin(), vec.end());

	vector<double>::size_type mid = vec.size() / 2;
	
	double median 
		= ( vec.size() % 2) ? vec[mid] : (vec[mid] + vec[mid-1]) / 2;

	return median;	
}

double grade(double midterm, double finalterm, double homework)
{
	return 0.2 * midterm + 0.4 * finalterm +0.4 * homework; 
}

//double median(const vector<double>& vec) // 값을 넘기면 복사생성자 생기고 여러가지 복잡하여 -> 주소를 넘김
//{
	//vector<double> tmp = vec;

	//sort(tmp.begin(), tmp.end());
//}

double grade(double midterm, double finalterm, const vector<double>& homeworks) // 중복 함수 -> 인자 다르게 사용
{
	if(homeworks.size() == 0){
		throw domain_error("student didn't any homework");
	}	

	return grade(midterm, finalterm, median(homeworks));
}

istream& read_hw(istream& in, vector<double>& homeworks)
{
	if(in){
		homeworks.clear();

		double hw;
		while(cin >> hw ){
			homeworks.push_back(hw);
		}

		in.clear();   // 
	}
	return in;
}

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
	read_hw(cin, homeworks);
	
	//vector<double>::size_type size = homework.size();
	//if(size == 0) {
		//cout << endl << "you must input your score." "please try again" << endl;

		//return 1;
	//}// -> 밑에 grade 함수를 만들었기 때문에 필요가 없음. 	
	
	//sort(homework.begin(), homeworks.end());
	
	try{
		streamsize ss = cout.precision();
		cout << "Your final score : " << setprecision(3) // setprecision은 소수점 
	   	<<grade(midterm, finalterm, homeworks) << setprecision(ss) << endl; // 다시 되돌리기

	} catch(const domain_error& e){
		cerr << endl << "you must enter your homework score" << endl; // cerr -> 표준 에러 장치
		return 1; // main함수 죽는 것                                  // 내부적으로 버퍼안쓰고 출력
	}                                                                     // clog -> log파일로
                                                                              // 구별해서 사용하는게 좋음
	                                                                      // redirect

	return 0;

}
