#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--){
	    int C;
	    cin>>C;
	    if(C>20){
	        cout<<"HOT"<<"\n";
	    }
	    else{
	        cout<<"COLD"<<"\n";
	    }
	}
	return 0;
}
