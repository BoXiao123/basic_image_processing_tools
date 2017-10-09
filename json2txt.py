
import os
import json
import pprint
import pickle

#read file
if not os.path.isfile('data.p'):
    path = '/home/b_xi/codes/darkflow/img/out/'
    files = []

    data = []

    for filename in os.listdir(path):
        files.append(path+filename)

    for file in files:
        with open(file,'r') as fin:
            content = json.load(fin)
        filename = file.replace(path,'')
        imagedata = {}
        imagedata['file'] = filename
        for dict in content:
            if dict['label'] in imagedata:
                imagedata[dict['label']].append(dict)
            else:
                imagedata[dict['label']] = [dict]
        data.append(imagedata)
    pickle.dump(data, open('data.p','wb'))
else:
    data = pickle.load(open('data.p','rb'))
##processing data
i=0
#def car_posion(car):
   # car_pos = [(car['bottomright']['x']+car['topleft']['x'])/2,(car['bottomright']['y']+car['topleft']['y'])/2]
   # car_size= [(car['bottomright']['x']-car['topleft']['x']),(car['bottomright']['y']-car['topleft']['y'])]
    #return car_pos car_size
while (i<len(data)):
	#if len(data[i]['car']) == 1:
        cardict = data[i]['car'][0]
	 
	#elif  len(data[i]['car'])==2
	 #cardict1 = data[i]['car'][0]
	 #cardict2 = data[i]['car'][1]
	#elif  len(data[i]['car'])==3
	 #cardict1 = data[i]['car'][0]
	 #cardict2 = data[i]['car'][1]
   	 #cardict3 = data[i]['car'][2]
	#elif  len(data[i]['car'])==4
	 #cardict1 = data[i]['car'][0]
	 #cardict2 = data[i]['car'][1]
   	 #cardict3 = data[i]['car'][2]
         #cardict4 = data[i]['car'][3]
	car_coords = [cardict['topleft']['x'],cardict['topleft']['y'],cardict['bottomright']['x'],cardict['bottomright']['y']]
	i=i+1
	print car_coords
	with open('/home/b_xi/codes/darkflow/img/' + 'results' + ".txt", "a") as writer:
            writer.write('%d,%d,%d,%d\n' % (car_coords[0], car_coords[1],
car_coords[2], car_coords[3]))
        

