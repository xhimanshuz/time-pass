#include<iostream>
void input_array(int*, int);
void output_array(int*, int);
void switchcase(int* p_array, int size)
{
  int choice;
  std::cout<<size;

  std::cout<<"What You want to do: \n1.Display Array \n2.Input Array \n3.Delete Array \n4. Exit \nEnter Your Choice: ";
  std::cin>>choice;
  do
  {
  switch(choice)
  {
  case 1:
  output_array(p_array, size);
  break;
  std::cout<<"Break";
  case 2:
  input_array(p_array, size);
  break;
  case 3:
  //del_array(array[],size)
  case 4:
  break;
  default:
  std::cout<<"Wrong Input";
  }
  } while(choice!=4);
}
