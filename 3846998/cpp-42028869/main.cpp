#include <bits/stdc++.h>
using namespace std;
enum{
    Add,Sub,Mul,Div,Mod,
    Eq,Ne,Gt,Lt,Ge,Le,
    Lsh,Rsh,
    And,Or,BitAnd,BitOr,Xor,
    Not,Inv,
};
struct value{
    string ctos(char a){
        stringstream ss;
        ss<<a;
        return ss.str();
    }
    enum{
        Int,Float,Bool,Str,Null,List,Func,
    };
    int tp;
    void* val;
    value(int a):tp(Int),val((void*)(new int(a))){}
    value(float a):tp(Float),val((void*)(new float(a))){}
    value(bool a):tp(Bool),val((void*)(new bool(a))){}
    value(string a):tp(Str),val((void*)(new string(a))){}
    value():tp(Null),val(0){}
    value(vector<value> a):tp(List),val(new vector<value>(a)){}
    value unary(int op){
        if(tp==Int||tp==Bool){
            int v;
            if(tp==Int) v=*(int*)val;
            else v=*(bool*)val;
            switch(op){
                case Add:return v;
                case Sub:return -v;
                case Not:return !v;
                case Inv:return ~v;
                default:throw "Unary:Invalid operator.";
            }
        }
        if(tp==Float){
            float v=*(float*)val;
            switch(op){
                case Add:return v;
                case Sub:return -v;
                case Not:return !v;
                default:throw "Unary:Invalid operator.";
            }
        }
        throw "Unary:Invalid type.";
    }
    value binary(int op,value b){
        if((tp==Int||tp==Float||tp==Bool)&&(b.tp==Int||b.tp==Float||b.tp==Bool)){
            if(tp==Float||b.tp==Float){
                float av,bv;
                if(tp==Float) av=*(float*)val;
                if(tp==Int) av=*(int*)val;
                if(tp==Bool) av=*(bool*)val;
                if(b.tp==Float) bv=*(float*)b.val;
                if(b.tp==Int) bv=*(int*)b.val;
                if(b.tp==Bool) bv=*(bool*)b.val;
                switch(op){
                    case Add:return av+bv;
                    case Sub:return av-bv;
                    case Mul:return av*bv;
                    case Div:return av/bv;
                    case Eq:return av==bv;
                    case Ne:return av!=bv;
                    case Gt:return av>bv;
                    case Lt:return av<bv;
                    case Ge:return av>=bv;
                    case Le:return av<=bv;
                    case And:return av&&bv;
                    case Or:return av||bv;
                    default:throw "Binary:Invalid operator.";
                }
            }
            else{
                int av,bv;
                if(tp==Int) av=*(int*)val;
                if(tp==Bool) av=*(bool*)val;
                if(b.tp==Int) bv=*(int*)b.val;
                if(b.tp==Bool) bv=*(bool*)b.val;
                switch(op){
                    case Add:return av+bv;
                    case Sub:return av-bv;
                    case Mul:return av*bv;
                    case Div:return av/bv;
                    case Mod:return av%bv;
                    case Eq:return av==bv;
                    case Ne:return av!=bv;
                    case Gt:return av>bv;
                    case Lt:return av<bv;
                    case Ge:return av>=bv;
                    case Le:return av<=bv;
                    case Lsh:return av<<bv;
                    case Rsh:return av>>bv;
                    case And:return av&&bv;
                    case Or:return av||bv;
                    case BitAnd:return av&bv;
                    case BitOr:return av|bv;
                    case Xor:return av^bv;
                    default:throw "Binary:Invalid operator.";
                }
            }
        }
        if(op==Add&&tp==Str&&b.tp==Str) return *(string*)val+*(string*)b.val;
        throw "Binary:Invalid type.";
    }
    value noref_index(value v){
        if(v.tp!=Int) throw "Index:Index is not integer.";
        if(tp==List) return (*(vector<value>*)val)[*(int*)v.val];
        if(tp==Str) return ctos((*(string*)val)[*(int*)v.val]);
        throw "Index:Object is not list or str.";
    }
    value& ref_index(value v){
        if(v.tp!=Int) throw "Index:Index is not integer.";
        if(tp==List) return (*(vector<value>*)val)[*(int*)v.val];
        throw "Index:Object is not list.";
    }
    void print(){
        switch(tp){
            case Int:cout<<*(int*)val;break;
            case Float:cout<<*(float*)val;break;
            case Str:cout<<*(string*)val;break;
            case Null:cout<<"null";break;
            case Bool:cout<<*(bool*)val;break;
            case List:{
                cout<<"[";
                vector<value> v=*(vector<value>*)val;
                if(v.size()){
                    for(int i=0;i<v.size()-1;i++){
                        v[i].print();
                        cout<<", ";
                    }
                    v[v.size()-1].print();
                }
                cout<<"]";
                break;
            }
            default:throw "Print:Can't convert the value to str.";
        }
    }
    bool to_bool(){
        switch(tp){
            case Int:return *(int*)val;
            case Bool:return *(bool*)val;
            case Float:return *(float*)val;
            case Str:return ((string*)val)->size();
            case List:return ((vector<value>*)val)->size();
            case Null:return 0;
            default:return "ToBool:Can't convert the value to bool.";
        }
    }
};
int main()
{
    return 0;
}