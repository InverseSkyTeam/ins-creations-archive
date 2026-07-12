#include <bits/stdc++.h>
using namespace std;
long long calderta(int a,int b,int c){
	return b*b - 4*a*c;
}
int gcds(int a,int b){
	if(a < b) return gcds(b,a);
	else if(a % b ==0) return b;
	else return gcds(b,a%b);
}
int maxwp(int x){
	int sum = 1;
	for(int i=2;i<=sqrt(x);i++) {
		while((x % (i*i)) == 0){
			sum *= i;
			x /= (i*i);
		}
	}
	return sum;
}
int main(){

	//freopen("uqe.in","r",stdin);
	//freopen("uqe.out","w",stdout);
	int t,m;
	cin >> t >> m;
	while(t){
		t--;
		int a,b,c;
		cin >> a >> b >> c;
		
		int derta = calderta(a,b,c);
		if(derta < 0){
			cout << "NO" <<endl; 
			continue;
		} 
		
		int fenmu = 2*a;
		int fenzishu = (-1) *b;
		
		//计算derta 
		
		int beikai = derta;
		//cout << beikai <<" ";
		int beikaixi = maxwp(derta);
		beikai /= (beikaixi *beikaixi);
		//cout << beikai <<" " <<beikaixi<<" ";
		if(derta == 0) beikaixi = 0; 
		
		//分母有理数 
		
		if(beikai == 1 || derta ==0){
			int nfenmu = fenmu;
			int nfenzi = fenzishu + beikaixi;
			if(nfenzi / nfenmu < (fenzishu - beikaixi)/nfenmu){
				nfenzi = fenzishu - beikaixi;
			}
			//cout << nfenmu <<" "<< nfenzi<<endl;
			if(nfenzi==0){
				cout << "0";
			} 
			else{
				bool isfu = true;//是否为负 
				if((nfenzi < 0 && nfenmu < 0 )||(nfenzi >= 0 && nfenmu >= 0 )){
					isfu = false;//正数 
				}
				int gcdab = gcds(abs(nfenmu),abs(nfenzi));
				nfenmu /= gcdab;
				nfenzi /= gcdab; 
				
				if(nfenzi%nfenmu == 0){
					if(!isfu){
						cout << abs(nfenzi/nfenmu) ;
					}
					else{
						cout << "-"<<abs(nfenzi/nfenmu) ;
					}
				} 
				else if(!isfu){
					cout << abs(nfenzi) <<"/" << abs(nfenmu);
				}
				else{
					cout << "-"<<abs(nfenzi) <<"/" << abs(nfenmu);
				}
			}
		}
		
		// 分母有无理数 
		else{
			//处理整数部分 
			
			if(fenzishu  != 0){
				bool isfu = true;//是否为负 
				if((fenzishu < 0 && fenmu < 0 )||(fenzishu >= 0 && fenmu >= 0 )){
					isfu = false;//正数 
				}
				int gcdab = gcds(abs(fenmu),abs(fenzishu));
				fenmu /= gcdab;
				fenzishu /= gcdab; 
				
				if(fenzishu%fenmu == 0){
					if(!isfu){
						cout << abs(fenzishu/fenmu) ;
					}
					else{
						cout << "-"<<abs(fenzishu/fenmu) ;
					}
				} 
				else if(!isfu){
					cout << abs(fenzishu) <<"/" << abs(fenmu);
				}
				else{
					cout << "-"<<abs(fenzishu) <<"/" << abs(fenmu);
				}
				cout << "+";
			}	
			//处理根号部分 
			
			int labfenzi = beikaixi,labfenmu = 2*a;
			bool isfus = true;//是否为负 
			if((labfenzi <= 0 && labfenmu <= 0 )||(labfenzi >= 0 && labfenmu >= 0 )){
				isfus = false;//正数 
			}
			int gcdabs = gcds(abs(labfenmu),abs(labfenzi));
			labfenmu /= gcdabs;
			labfenzi /= gcdabs;
			
			if(labfenzi % labfenmu == 0){
				int addshu = abs(labfenzi) / abs(labfenmu);
				if(addshu == 1){
					cout << "sqrt(" << beikai<<")";
				}
				else{
					cout << abs(addshu)<< "*sqrt(" << beikai<<")";
				}
			}
			else if(labfenzi == 1){
				//if(isfus){
				//	cout << "-" <<  "sqrt(" << beikai<<")/"<< abs(labfenmu);
				//}
				//else{
					cout << "sqrt(" << beikai<<")/"<< abs(labfenmu);
				//}
			} 
			else{
				//if(isfus){
				//	cout << "-" << abs(labfenzi) <<"*sqrt(" << beikai<<")/"<< abs(labfenmu);
				//}
				//else{
					cout << abs(labfenzi) <<"*sqrt(" << beikai<<")/"<< abs(labfenmu);
				//}
			}
		}
		
			
		
		cout << endl;
		
	}
	
	return 0;
} 