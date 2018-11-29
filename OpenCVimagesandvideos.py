import numpy as np
from matplotlib import pyplot as plt
import cv2


def a(): #view image
    img = cv2.imread('fire.png', 1)
    print(img)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    img = cv2.imread('fire.png', 1)[:, :, ::-1]
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


def b(): # capture video and display
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    cv2.destroyAllWindows()


def c():    # capture video, flip, display, and save
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 60.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def d(cons): # Opens video and plays it
    cap = cv2.VideoCapture('output.avi')

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            blue = frame[:,:,0]
            green = frame[:,:,1]
            red = frame[:,:,2]
            vis = (blue - (green+red)//2)
            a = vis>cons
            print(vis)
            frame[a] = 0
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): # Wait time between frames.
            break

    cap.release()
    cv2.destroyAllWindows()

def e():

    lower_blue = np.array([])
    upper_blue = np.array([])

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        nframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow('HSV', nframe)
        cv2.imshow('normal', frame)
        if cv2.waitKey(50) & 0xFF == ord('q'):  # Wait time between frames.
            break
e()