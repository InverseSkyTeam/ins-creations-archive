print('''{
    /*
    这是一个dfs求8的全排列的integer3程序
    */
    import builtin;
    var n=8,answer=[0,0,0,0,0,0,0,0],visit=[0,0,0,0,0,0,0,0];
    func sleep(a){//sleep函数
        var begin=time();
        while time()-begin<a;
    }
    func dfs(k){//学过c++的应该知道dfs怎么写
        if k==n{
            foreach i in answer print(i," ");
            println();
            sleep(0.001);//防止输出超长
        }
        for var i=0;i<n;i=i+1 if visit[i]==0{
            visit[i]=1;
            answer[k]=i+1;
            dfs(k+1);
            answer[k]=0;
            visit[i]=0;
        }
    }
    dfs(0);
}''')