import cv2
import os
import matplotlib.pyplot as plt

if __name__=='__main__':
    data_dir='/home/b_xi/codes/combineimages'
    image1_dir='image1'
    image2_dir='image2'
    output_dir='result'
    frame_list1=os.listdir(image1_dir)
    frame_list1.sort()
    frame_list2=os.listdir(image2_dir)
    frame_list2.sort()
    print frame_list2
    for f,frame in enumerate(frame_list1):
        img1=cv2.imread(os.path.join(data_dir,image1_dir,frame))
        img2=cv2.imread(os.path.join(data_dir,image2_dir,frame_list2[f]))
        fig,(ax0,ax1)=plt.subplots(1,2,figsize=(16,6))
        plt.tight_layout()
        ax0.imshow(img1)
        ax0.set_title('labeled image')
        ax0.set_axis_off()
        ax1.imshow(img2)
        ax1.set_title('detected image')
        ax1.set_axis_off()
        plt.savefig(os.path.join(data_dir, output_dir, frame))

