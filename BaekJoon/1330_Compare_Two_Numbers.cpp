#include <iostream>

using namespace std;

int main(void) {
    int num1, num2;
    cin >> num1 >> num2;

    if (num1 > num2)
        cout << ">";
    else if (num1 == num2)
        cout << "==";
    else   
        cout << "<";
    cout << "\n";
    return 0;
}