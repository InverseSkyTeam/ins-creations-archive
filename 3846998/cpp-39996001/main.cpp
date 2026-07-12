#ifndef __linux
#include<bits/stdc++.h>
#include<conio.h>
#include<unistd.h>
#include <windows.h>
using namespace std;
enum{
	BLACK=0,
	WHITE=127,
};
void color(int x)
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), x);
}
void print(char c){
	color(c);
	cout<<"  ";
	color(15);
}
struct Screen{
	char screen[10][10];
	int score;
	Screen(){
		score=0;
		memset(screen,WHITE,sizeof screen);
	}
	void show(){
		for(int i=0;i<10;i++,putchar(10))
			for(int j=0;j<10;j++)
				print(screen[i][j]);
		cout<<score<<endl;
	}
};
struct FallAble{
	int row,line=0;
	Screen*scr;
	FallAble(Screen *s=0,int a=0):scr(s),row(a){
		scr->screen[0][row]=0;
	}
	void fall(){
		scr->screen[line][row]=127;
		if(line!=9) line++;
		if(line!=9) scr->screen[line][row]=0;
		else scr->score--;
	}
};
struct Player{
	int row=0;
	Screen&scr;
	Player(Screen&s):scr(s){
		row=0;
		scr.screen[9][0]=scr.screen[9][1]=0;
	}
	bool touch(vector<FallAble> v){
		for(int _i=0;_i<v.size();_i++){
			FallAble &i=v[_i];
			if((i.row==row||i.row==row+1)&&i.line==8) return 1;
			return 0;
		}
	}
	void left(){
		scr.screen[9][row+1]=127;
		scr.screen[9][row-1]=0;
		row--;
	}
	void right(){
		scr.screen[9][row]=127;
		scr.screen[9][row+2]=0;
		row++;
	}
};
int main()
{
	Screen screen;
	vector<FallAble> fs;
	Player player(screen);
	int cnt=0;
	while(1){
		(cnt+=1)%=10;
		if(kbhit()){
			char cmd=getch();
			if(cmd=='a') player.left();
			if(cmd=='d') player.right();
		}
		if(player.touch(fs)) screen.score+=2;
		if(cnt==0){
			fs.push_back(FallAble(&screen,rand()%10));
		}
		for(int i=0;i<fs.size();i++) fs[i].fall();
		for(int i=0;i<fs.size();i++) if(fs[i].line==9){
			fs.erase(fs.begin()+i);
			break;
		}
		screen.show();
		usleep(100000);
		system("cls");
	}
    return 0;
}
#else
#include <iostream>
int main(){
    std::cout<<"\
这是我瞎写的一个C++小游戏\n\
就当水作吧\n\
请在Windows系统下编译运行\n";
}
#endif