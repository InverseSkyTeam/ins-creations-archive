print("看源码里的fast_cloud.py")
import fast_cloud,time
token = "cff076b0-c3e1-4c1c-af4c-2d19303d83e5"
var = int(fast_cloud.get_var("run_times")["data"])+1
fast_cloud.set_var("run_times",var,token)
print(f"该作品被运行了{var}次")