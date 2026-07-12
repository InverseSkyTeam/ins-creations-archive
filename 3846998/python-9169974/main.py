from time import*
from xes.AIspeak import*
A=strftime("现在的时间是%H:%M:%S")
print(A)
speak(A)
if A=="现在的时间是09:00:00":
    print("上课")
    speak("上课")
else:
    print("什么都不用干")
    speak("什么都不用干")