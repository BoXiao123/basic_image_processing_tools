import sys
import numpy as np

dir_name=sys.argv[1]
txt_name=sys.argv[2]
train_percentage=85
with open(txt_name,'r') as gt:
    lines=gt.readlines()
    for i in range(len(lines)):
        chance=np.random.randint(100)
        raw_line = lines[i].strip().split(',')
        print raw_line
        if chance<train_percentage:
            with open(dir_name+'/result_train.txt','a') as writer_train:
                writer_train.write('%s\n'%raw_line[0])
        else:
            with open(dir_name+'/result_val.txt','a') as writer_val:
                writer_val.write('%s\n' % raw_line[0])



