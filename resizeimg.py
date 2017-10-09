from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=640,height=480):
    img=Image.open(jpgfile)   
    new_img=img.resize((width,height),Image.BILINEAR)   
    new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
for jpgfile in glob.glob('/home/b_xi/codes/video2img/result/*.jpg'):
    convertjpg(jpgfile,'/home/b_xi/codes/video2img/resize/')
