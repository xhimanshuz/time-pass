#include<iostream>
/*class array
{
public:
  int array[10];
  int size = 10;
  int* ptr;
*/  void input_array(int*, int);
  void output_array(int*, int);
  void switchcase(int*, int);
//};
//void array::input_array(int*, int);
//void array::output_array(int*, int);
//void array::switchcase(int*, int);

int main()
{
//  array a
  int size = 10;
int array[size];

  int *ptr=&array[0];
  switchcase(ptr, size);
  return 0;
}
