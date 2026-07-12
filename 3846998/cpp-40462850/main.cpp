#include <bits/stdc++.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
using namespace std;
const int SCREEN_SIZE=10;
void gotoxy(int x,int y){
    printf("\032[%d;%df",x,y);
}
int getch(void)
{
    struct termios tm, tm_old;
    int fd = 0, ch;
    if (tcgetattr(fd, &tm) < 0)return -1;
    tm_old = tm;
    cfmakeraw(&tm);
    if (tcsetattr(fd, TCSANOW, &tm) < 0)return -1;
    ch = getchar();
    if (tcsetattr(fd, TCSANOW, &tm_old) < 0)return -1;
    return ch;
}
//感谢李承运的kbhit
int kbhit(void)
{
    struct termios oldt, newt;
    int ch;
    int oldf;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
    fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    fcntl(STDIN_FILENO, F_SETFL, oldf);
    if(ch != EOF)
    {
        ungetc(ch, stdin);
        return 1;
    }
    return 0;
}
void show_color(int color){
    printf("\033[4%dm  \033[1;0m",color);
}
template<class T>
vector<vector<T> > mk_screen(int x,int y){
    vector<vector<T> > res;
    for(int i=0;i<x;i++) res.push_back(vector<T>(y));
    return res;
}
enum Color{
    Gray,Red,Green,Yellow,DarkBlue,Purple,LightBlue,White,Black
};
struct Screen{//屏幕，屏幕大小为10*10
    vector<vector<int> > mem=mk_screen<int>(4096,4096);
    int begin_line=4086,begin_row=0;
    Screen(){
        for(int i=0;i<4096;i++) mem[4095][i]=White;
        mem[4094][5]=White;
        mem[4094][6]=White;
        mem[4094][10]=Red;
        mem[4094][8]=Yellow;
    }
    void show(){
        cout<<"\033c";
        for(int i=begin_line;i<begin_line+SCREEN_SIZE;i++){
            for(int j=begin_row;j<begin_row+SCREEN_SIZE;j++){
                printf("\033[4%dm  \033[1;0m",mem[i][j]);
            }
            cout<<'\n';
        }
    }
    void erase(int x,int y){
        mem[x][y]=Gray;
    }
    void draw(int x,int y,int c=7){
        mem[x][y]=c;
    }
    void set_begin(int x,int y){
        if(x>begin_line+10) begin_line=x-7;
        if(y>begin_row+9) begin_row=y-9;
        if(x<begin_line) begin_line=x;
        if(y<begin_row) begin_row=y;
    }
    int color_of(int x,int y){
        return mem[x][y];
    }
} screen;
class Object{
public:
    int line=4095,row=0;
    int lr_speed=0;
    int ws_speed=0;
    Object(){
        while(screen.color_of(line,row)==White) line--;
        screen.draw(line,row,Green);
    }
    void move(char d){
        if(d=='w'&&touch_ground()) ws_speed-=3;
        if(d=='a') lr_speed-=2;
        if(d=='d') lr_speed+=2;
        if(lr_speed>0) lr_speed--;
        if(lr_speed<0) lr_speed++;
        screen.erase(line,row);
        line+=ws_speed;
        row+=lr_speed;
        if(row<0) row=0;
        if(row>4095) row=4095;
        if(line>4095) line=4095;
        while(screen.color_of(line,row)==White) line--;
        if(screen.color_of(line,row)==Yellow) ws_speed-=10,line--;
        if(screen.color_of(line,row)==Red) line=4094,row=0;
        screen.draw(line,row,Green);
        screen.set_begin(line,row);
        if(!touch_ground()&&line<4095) ws_speed++;
        else ws_speed=0;
    }
    bool touch_ground(){
        return line==4095||screen.color_of(line+1,row)==White;
    }
} obj;
int main()
{
    while(1){
        usleep(200000);
        screen.show();
        if(kbhit()){
            obj.move(getch());
        }
        else obj.move('.');
        if(0) break;
        cout<<obj.line<<" "<<obj.row<<" "<<obj.ws_speed<<" "<<obj.lr_speed;
    }
    return 0;
}