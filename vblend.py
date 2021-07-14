import  cv2
video1=cv2.VideoCapture('bg1.mp4')
video2=cv2.VideoCapture('bg2.mp4')
video3=cv2.VideoCapture('bg3.mp4')
video4=cv2.VideoCapture('bg4.mp4')
video5=cv2.VideoCapture('bg5.mp4')
video6=cv2.VideoCapture('bg6.mp4')
video7=cv2.VideoCapture('v1.mp4')

def  bground1():
    while video1.isOpened() and video7.isOpened():
        success1,frame1=video1.read()
        success7,frame7=video7.read()
        if success1 and success7:
            frame1 = cv2.resize(frame1, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame1, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break

def  bground2():
    while video2.isOpened() and video7.isOpened():
        success2,frame2=video2.read()
        success7,frame7=video7.read()
        if success2 and success7:
            frame2 = cv2.resize(frame2, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame2, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break

def  bground3():
    while video3.isOpened() and video7.isOpened():
        success3,frame3=video3.read()
        success7,frame7=video7.read()
        if success3 and success7:
            frame3= cv2.resize(frame3, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame3, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break

def  bground4():
    while video4.isOpened() and video7.isOpened():
        success4,frame4=video4.read()
        success7,frame7=video7.read()
        if success4 and success7:
            frame4 = cv2.resize(frame4, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame4, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break


def  bground5():
    while video5.isOpened() and video7.isOpened():
        success5,frame5=video5.read()
        success7,frame7=video7.read()
        if success5 and success7:
            frame5 = cv2.resize(frame5, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame5, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break

def  bground6():
    while video6.isOpened() and video7.isOpened():
        success6,frame6=video6.read()
        success7,frame7=video7.read()
        if success6 and success7:
            frame6 = cv2.resize(frame6, (frame7.shape[1], frame7.shape[0]))
            blended_video = cv2.addWeighted(frame6, 0.4, frame7, 0.5, gamma=1)
            cv2.imshow('Blended video', blended_video)
            choose()
        else:
            break


def choose():
    k = cv2.waitKey(100)

    if k & 0xff == ord('1'):
        print("BackGround-1")
        bground1()
    if k & 0xff == ord('2'):
        print("BackGround-2")
        bground2()
    if k & 0xff == ord('3'):
        print("BackGround-3")
        bground3()
    if k & 0xff == ord('4'):
        print("BackGround-4")
        bground4()
    if k & 0xff == ord('5'):
        print("BackGround-5")
        bground5()
    if k & 0xff == ord('6'):
        print("BackGround-6")
        bground6()


bground1()
cv2.destroyAllWindows()


