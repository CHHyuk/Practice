#include<iostream>

namespace BestComImpl
{
	void SimpleFunc(void);     // BestComImpl이라는 이름공간 안에 함수의 선언만 삽임
}                           

namespace ProgComImpl
{
	void SimpleFunc(void);     // ProgComImpl이라는 이름공간 안에 함수의 선언만 삽입
}

int main(void)
{
	BestComImpl::SimpleFunc();
	ProgComImpl::SimpleFunc();
	return 0;
}

void BestComImpl::SimpleFunc(void)  // simplefunc가 정의된 부분, 해당 문구가 출력되는 함수
{
	std::cout << "BestCom이 정의한 함수" << std::endl;
}

void ProgComImpl::SimpleFunc(void)  // simplefunc가 정의된 부분, 해당 문구가 출력되는 함수
{
	std::cout << "ProgCom이 정의한 함수" << std::endl;
}