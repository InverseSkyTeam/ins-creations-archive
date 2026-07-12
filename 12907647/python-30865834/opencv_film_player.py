# 更据***的博客 opencv-cv2包视频播放器 改编
import cv2

def play(name):
    # 获得视频的格式
    videoCapture = cv2.VideoCapture(name)  # 本地mp4文件
    # videoCapture = cv2.VideoCapture('http://127.0.0.1:8080/static/mac-bruce-tpl-cn-2018_1280x720h.mp4')  # 服务端mp4文件
    
    # 获得码率及尺寸
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    width = int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    # print(fps, size)
    
    # 编码格式
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    f = cv2.VideoWriter_fourcc('M', 'P', '4', '2')  # ？？
    
    # 指定写视频的格式, I420-avi, MJPG-mp4
    videoWriter = cv2.VideoWriter('player.avi', f, fps, size)
    
    # 读帧
    success, frame = videoCapture.read()
    
    while success :
        videoWriter.write(frame)  # 写视频帧
        cv2.imshow("video", frame)  # 显示
    
        cv2.waitKey(int(1000/int(fps)))  # 延迟
    
        # if ord("q") == cv2.waitKey(41):
        #     break
        success, frame = videoCapture.read()  # 获取下一帧
    # 资源释放
    cv2.destroyAllWindows()
    videoCapture.release()
    videoWriter.release()