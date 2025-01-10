import numpy as np

def get_angle(a,b,c):
    rad = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(np.degrees(rad))
    return angle

def length(landmark_list):
    if len(landmark_list) < 2:
        return
    (x1,y1),(x2,y2) = landmark_list[0],landmark_list[1]
    L = np.hypot(x2-x1,y2-y1)
    
    return np.interp(L,[0,1],[0,1000])


def mouse_movement(wrist):
    import csv
    with open('movement.csv', mode ='a')as file:
        writer  = csv.writer(file)
        writer.writerow([wrist.x,wrist.y,wrist.z])
    