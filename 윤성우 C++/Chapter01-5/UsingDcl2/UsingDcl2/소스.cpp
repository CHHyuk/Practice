#include<iostream>
using std::cin;
using std::cout;
using std::endl; //using 선언을 함수 밖에서 전역의 형태로 삽입하였다. 그래서 std:: 라는 이름공간의 사용이 필요 없어짐

int main()
{
	int num = 20;
	cout << "Hello World" << endl;
	cout << "Hello " << "World" << endl;
	cout << num << ' ' << 'A';
	cout << ' ' << 3.14 << endl; // using 선언을 통해 코드의 구성이 한결 간단해졌음을 알 수 있다.
	return 0;
}