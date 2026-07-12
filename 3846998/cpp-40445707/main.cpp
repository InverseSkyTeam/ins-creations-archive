#if 1//问题已解决？
#include <bits/stdc++.h>
#include <termios.h>
#include <unistd.h>
#include <fcntl.h>
using namespace std;
const int SCREEN_SIZE=10;
void gotoxy(int x,int y){
    printf("\032[%d;%df",x,y);
}
int getch() {
    struct termios oldt, newt;
    int ch;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    ch = getchar();
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
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
class Screen;
bool touch(Screen*screen,int x,int y,Color color);
class Screen{//屏幕，屏幕大小为10*10
public:
    vector<vector<int> > mem=mk_screen<int>(4096,4096);
    int begin_line=0,begin_row=0;
    Screen(){}
    void show(){
        printf("\033c");
        for(int i=begin_line;i<begin_line+SCREEN_SIZE;i++){
            for(int j=begin_row;j<begin_row+SCREEN_SIZE;j++){
                printf("\033[4%dm  \033[1;0m",mem[i][j]);
                if(mem[i][j]==Green&&touch(this,i,j,Black)) erase(i,j);
            }
            cout<<'\n';
        }
        srand(time(0));
        for(int i=0;i<10000;i++) mem[rand()%4096][rand()%4096]=Green;
    }
    void erase(int x,int y){
        mem[x][y]=Gray;
    }
    void draw(int x,int y,int c=7){
        mem[x][y]=c;
    }
};
enum Direction{
    Up,Down,Left,Right,Unknown
};
pair<int,int> backward(int x,int y,int d){
    d%2?d--:d++;
    d==Up?x--:
    d==Down?x++:
    d==Left?y--:
    y++;
    return make_pair(x,y);
}
pair<int,int> forward(int x,int y,int d){
    return backward(x,y,d%2?d-1:d+1);
}
pair<int,int> forward(pair<int,int> a,int d){
    return forward(a.first,a.second,d);
}
bool touch(Screen*screen,int x,int y,Color color){
    if(x==0||x==4095||y==0||y==4095) return 0;
    #define scr screen->mem
    return scr[x+1][y]==color||scr[x-1][y]==color||scr[x][y+1]==color||scr[x][y-1]==color;
    #undef scr
}
class Point{
public:
    int x,y,direction=Right,color=White;
    Screen*screen=0;
    Point(){}
    Point(int a,int b,Screen*s,int c=White):x(a),y(b),screen(s),color(c){
        screen->draw(x,y,color);
    }
    void move(){
        screen->erase(x,y);
        switch(direction){
            case Up:x--;break;
            case Down:x++;break;
            case Left:y--;break;
            case Right:y++;break;
        }
        screen->draw(x,y,color);
    }
    void changeDirection(Direction d){
        direction=d;
    }
    void destroy(){
        screen->erase(x,y);
    }
    bool touch(Color color){
        if(x==0||x==4095||y==0||y==4095) return 0;
        #define scr screen->mem
        return scr[x+1][y]==color||scr[x-1][y]==color||scr[x][y+1]==color||scr[x][y-1]==color;
        #undef scr
    }
};
int middle(int from,int to){
    //printf("middle(from=%s(aka %d),to=%s(aka %d))\n",convert[from],from,convert[to],to);
    if(from==to) return to;
    if(
        (from==Up||from==Down)&&(to==Left||to==Right)||
        (from==Left||from==Right)&&(to==Up||to==Down)
    ) return to;
    return
        from==Up&&to==Down||from==Down&&to==Up?to:
        from==Left&&to==Right||from==Right&&to==Left?to:
        Unknown;
}
class Snake{
public:
    vector<Point> body;
    Screen*screen;
    Snake(Screen*s):screen(s){
        body.push_back(Point(5,5,screen,Black));
        body.push_back(Point(5,4,screen));
        body.push_back(Point(5,3,screen));
        body.push_back(Point(5,2,screen));
        body.push_back(Point(5,1,screen));
    }
    void move(int direction){
        Point tail=*(body.end()-1);
        pair<int,int> bk=backward(tail.x,tail.y,tail.direction);
        //tail.x=bk.first;
        //tail.y=bk.second;
        if(direction!=Unknown) body[0].direction=direction;
        for(int i=0;i<body.size();i++) body[i].move();
        if(body[0].touch(Green)) body.push_back(tail);
        for(int i=body.size();i>=0;i--){
            body[i+1].direction=middle(body[i+1].direction,body[i].direction);
        }
        /*for(int i=0;i<body.size()-1;i++){
            if(body[i].direction!=body[i+1].direction){
                if(i<body.size()-2) body[i+2].direction=body[i+1].direction;
                int d=body[i+1].direction;
                body[i+1].direction=body[i].direction;
                ++++i;
                while(i<body.size()&&body[i].direction==d) i++;
                --i;
            }
        }*/
        if(body[0].x>=screen->begin_line+SCREEN_SIZE) screen->begin_line++;
        if(body[0].x<screen->begin_line) screen->begin_line--;
        if(body[0].y>=screen->begin_row+SCREEN_SIZE) screen->begin_row++;
        if(body[0].y<screen->begin_row) screen->begin_row--;
    }
    void redirect(int direction) __attribute_deprecated__{
        body[0].direction=direction;
        for(int i=body.size();i>=0;i--){
            body[i+1].direction=middle(body[i+1].direction,body[i].direction);
        }
    }
};
int main()
{
    Screen screen;
    Snake snake(&screen);
    screen.show();
    while(1){
        usleep(200000);
        char ch=0;
        if(kbhit()){
            ch=getch();
        }
        snake.move(//是不是很像Haskell？
            ch=='w'?Up:
            ch=='s'?Down:
            ch=='a'?Left:
            ch=='d'?Right:
            Unknown
        );
        screen.show();
        printf("%d %d\n长度：%d\n",snake.body[0].x,snake.body[0].y,snake.body.size());
        //for(Point i:snake.body) cout<<i.direction<<" ";
        if(0) break;
    }
    return 0;
}
#else//下面相当于草稿纸
/*
很明显这已经变成了题
现在只需要解决这道题就可以了
*/

#include <bits/stdc++.h>
using namespace std;
int snake[5]={3,3,3,3,3};
enum Direction{
    Up,Down,Left,Right,Unknown
};
const char* convert[5]={
    "Up",
    "Down",
    "Left",
    "Right",
    "Unknown"
};
int middle(int from,int to){
    //printf("middle(from=%s(aka %d),to=%s(aka %d))\n",convert[from],from,convert[to],to);
    if(from==to) return to;
    if(
        (from==Up||from==Down)&&(to==Left||to==Right)||
        (from==Left||from==Right)&&(to==Up||to==Down)
    ) return to;
    return
        from==Up&&to==Down||from==Down&&to==Up?to:
        from==Left&&to==Right||from==Right&&to==Left?to:
        Unknown;
}
void solve(int d){
    if(d!=Unknown) snake[0]=d;
    for(int i=4;i>=0;i--){
        snake[i+1]=middle(snake[i+1],snake[i]);
    }
}
int main(){
    string s;
    cin>>s;
    for(char ch:s){
        solve(
            ch=='w'?Up:
            ch=='s'?Down:
            ch=='a'?Left:
            ch=='d'?Right:
            Unknown
        );
    }
    for(int i=0;i<5;i++) cout<<(
        snake[i]==Up?"Up":
        snake[i]==Down?"Down":
        snake[i]==Left?"Left":
        snake[i]==Right?"Right":
        "Unknown"
    )<<" ";
    return 0;
}
#endif