var n:int;
Srin >> n;
for i:int (2,n){
    var is:bool;
    is=true;
    for j:int (2,i-1,1){
        if(i%j==0){
            is=false;
        }else{
            break;
        }
    ;};
    if(is){Sout << i<<" ";};
};
