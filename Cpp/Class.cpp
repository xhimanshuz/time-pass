#include<iostream>
using namespace std;

class FDiffentialTable
{
private:
    int i,j;
    static int s;
    s = 5;
    double x[s];
    double y[s][s];
public:
    void input();
    void output();
    void algo();
    FDiffentialTable()
    {
        cin>>s;
    
    }
};

void FDiffentialTable :: input()
{
    cout<<"Enter Number of Row: ";
    cin>>s;
    double x[s], y[s][s];
    cout<<"Enter X: \n";
    for(i = 0;i<s;i++)
    {
        cout<<"x>> ";
        cin>>x[i];
    }
    cout<<"Enter Y: \n";
    for(i = 0;i<s;i++)
    {
        cout<<"y>> ";
        cin>>y[0][i];
    }
}
void FDiffentialTable :: algo()
{
 for(j = 1;j<s;j++)
 {
     for(i = 0;i<(s-j);i++)
     {
         y[j][i]=(y[j-1][i+1]-y[j-1][i])/(x[i+j]-x[i]);
     }
 }   
}
void FDiffentialTable :: output()
{
 cout<<"DIVIDED DEFFERENCE TABLE \n";
 for(i = 0;i<s;i++)
 {
     if(i==0)
     cout<<"x\ty\t";
     else
     cout<<"Δ"<<i<<"y\t";   
 }
 cout<<endl;
 for(j = 0;j<s;j++)
 {
     cout<<x[j]<<"\t";
     for(i =0;i<(s-j);i++)
     {
         cout<<y[i][j]<<"\t";
     }
 }   
}
int main()
{
    FDiffentialTable obj1;
    obj1.input();
    obj1.algo();
    obj1.output();
}
