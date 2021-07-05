#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

int main(){
	
	int nums[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	vector<int> vec1(nums, nums +10);

	vector<int> vec2(10, 0);
	vector<int> vec3;
	vector<int> vec4 = vec1;
	vector<int> vec5(vec1.begin(), vec1.begin() + 5); 

	for (vector<int>::size_type i = 0; i <vec1.size(); ++i) // size타입은 int X 
		cout << vec1[i] * vec1[i] << endl;

	return 0;
}
