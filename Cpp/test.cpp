#include <iostream>
using namespace std;

void output(double y[][], double x[], int s)
{
    cout << "DIVIDED DEFFERENCE TABLE \n";
    for (int i = 0; i < s; i++)
    {
        if (i == 0)
            cout << "x\ty\t";
        else
            cout << "Δ" << i << "y\t";
    }
    cout << endl;
    for (int j = 0; j < s; j++)
    {
        cout << x[j] << "\t";
        for (int i = 0; i < (s - j); i++)
        {
            cout << y[i][j] << "\t";
        }
    }
}
void algo(double *y,double *x,int s)
{
    for (int j = 1; j < s; j++)
    {
        for (int i = 0; i < (s - j); i++)
        {
            y[j][i] = (y[j - 1][i + 1] - y[j - 1][i]) / (x[i + j] - x[i]);
        }
    }
    output(y[][], x[], s);
}

void input()
{  
    int s;
    cout << "Enter Number of Row: ";
    cin >> s;
    double x[s];
    double y[s][s];
    cout << "Enter X: \n";
    for (int i = 0; i < s; i++)
    {
        cout << "x>> ";
        cin >> x[i];
    }
    cout << "Enter Y: \n";
    for (int i = 0; i < s; i++)
    {
        cout << "y>> ";
        cin >> y[0][i];
    }
    algo(y[][], x[], s);
}
    
    int main()
    {
        input();
    }
