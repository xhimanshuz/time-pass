#include<iostream>

// void display(int *p_array, int size)
// {
//   for(int i = 0;i<size;i++)
//   {
//     std::cout<<*p_array++;
//   }
// }
void merge()
{
  int size = 15;
  int a[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
  int n;
  int flag = 0;
  std::cout<<"Enter No. to search: \n >> ";
  std::cin>>n;
  //for(int i =0; i<size;i++)
  //{
  if(n<a[size/2])
  {
      //size = size/2;
      for(int i = 0;i<size/2;i++)
      {
      if(a[i]==n)
      {
      flag = 1;
      std::cout<<"No. Found at: "<<i<<std::endl;
      break;
      }
      }
    }
    if(n>a[size/2])
    {
      for(int i = ((size/2)+1); i<=size;i++)
      {
        if(a[i]==n)
        {
          flag = 1;
          std::cout<<"No. found at "<<i<<std::endl;
        }
      }
    }
    if(flag == 0)
    std::cout<<"Not Found";
  }


int main()
{
  merge();
  return 0;
}
