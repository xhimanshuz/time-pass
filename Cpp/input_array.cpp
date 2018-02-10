#include<iostream>
void input_array(int *p_array,int  size)
{
  int i;
 for(i=0; i<10;i++)
 {
   std::cout<<">> ";
   std::cin>>*p_array++;
   std::cout<<"\t"<<i;
 }
}
