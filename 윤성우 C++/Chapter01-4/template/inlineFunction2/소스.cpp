#include<iostream>

template <typename T> // template 활용, 자료형의 구분 없이 데이터의 손실이 일어나지 않게 함
inline T SQUARE(T x)
{
	return x * x;
}

int main(void)
{
	std::cout << SQUARE(5.5) << std::endl;
	std::cout << SQUARE(12) << std::endl;
	return 0;
}