#include<iostream>
using namespace std;
int fact(int i)
{
  if(i>=1)
  return i*fact(i-1);
  else
  return 1;
}
double ux(double u, int i)
{
  if(i==0)
  {
    return 1;
  }
  if(i==1)
  return u;
  else
  {
    double ux = u;
    while(i!=1)
    {
      ux *= (u-(i-1)); i--;
    } cout<<ux; return ux;
  }
}

int main()
{ 
  for(int i = 0;i<5;i++)
  cout<<"UX: "<<ux(4, i)<<endl;
  // cout<<fact(6);
  return 0;
}
