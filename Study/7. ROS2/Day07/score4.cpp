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
using std::max;
using std::sort;
using std::domain_error;

struct Student_info{
	string name;
	double midterm;
	double finalterm;
	vector<double> homeworks;
};

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

double grade(const Student_info student)
{
	return grade(student.midterm, student.finalterm, student.homeworks);
}

istream& read(istream& in, Student_info& student)
{
	in >> student.name >> student.midterm >> student.finalterm;
	
	read_hw(in, student.homeworks);	

	return in;
}

bool compare(const Student_info& s1, const Student_info& s2)
{
	return s1.name < s2.name;

}

int main()
{
	string::size_type maxLen = 0;	
	vector<Student_info> students;
	
	Student_info student;

	
	while (read(cin, student)){
		//       template(int, unsigned int(string::size) -> error 난다.
		maxLen = max(maxLen, student.name.size());
		students.push_back(student);
	}
	
	sort(students.begin(), students.end(), compare); // 사용할려면 비교하는 연산자를 구조체 안에 넣어줘야함 

	try{	
		for (vector<Student_info>::size_type i = 0; i != students.size(); ++i)
		{
			streamsize ss = cout.precision();
			cout << students[i].name << string(maxLen - students[i].name.size(), ' ') << " : " << setprecision(3) 
			<< grade(students[i]) << setprecision(ss) << endl; // 다시 되돌리기
		}
	} catch(const domain_error& e){
		cerr << endl << "you must enter your homework score" << endl; // cerr -> 표준 에러 장치
		return 1; // main함수 죽는 것                                  // 내부적으로 버퍼안쓰고 출력
	}                                                                     // clog -> log파일로
                                                                              // 구별해서 사용하는게 좋음
	                                                                      // redirect

	return 0;

}
