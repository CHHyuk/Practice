#include<iostream>

inline int SQUARE(int x) // 인라인 함수의 정의 방법 표현, SQUARE 함수가 인라인 함수가 되었음
{
	return x * x; 
}

int main()
{
	std::cout << SQUARE(5) << std::endl; 
	std::cout << SQUARE(12) << std::endl; // SQUARE 함수를 호출하고있음, 그런데 이 함수는 인라인 함수이니 몸체부분이 호출문을 대체하게 됨
	return 0;
}