#include <iostream>
#include <string>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int arr[10]={};
    int num=1;
    int a,b,c;

    cin >> a >> b >> c;
    num=a*b*c;
    
    while(num>0){
        arr[num%10]++;
        num/=10;
    }

    for(int i=0; i<10; i++){
        cout << arr[i] << '\n';
    }
}