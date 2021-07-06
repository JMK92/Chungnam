#include <iostream>
#include <iomanip> // precision 때문에 사용
#include<ios>
#include <string>
#include <vector>
#include<algorithm>
#include<stdexcept>

//#include"grade.h"
//#include"median.h"
#include"student_info.h"

using namespace std;
using std::cerr;
using std::istream;
using std::setprecision;
using std::streamsize;
using std::max;
using std::sort;
using std::domain_error;


int main()
{
	string::size_type maxLen = 0;
	vector<Student_info> students;	

	try {
		Student_info student;
		while (read(cin, student)) {
			maxLen = max(maxLen, student.name.size());
			students.push_back(student);
		}
		
	} catch (const domain_error& e) {
		cerr << endl << e.what() << endl;
		return 1;
	}

	sort(students.begin(), students.end(), compare);

	for(vector<Student_info>::size_type i = 0; i!=students.size(); ++i)
	{
		streamsize ss = cout.precision();

		cout << students[i].name << string(maxLen - students[i].name.size(), ' ') 
			 << " : " << setprecision(3)
 			 //<< grade(students[i])  << setprecision(ss) << endl;
			 << students[i].finalScore  << setprecision(ss) << endl;
	}
	return 0;
}
