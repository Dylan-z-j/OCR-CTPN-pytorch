import numpy as np

def nms(boxes,thresh):
    
    if len(boxes) == 0:
        return []

    if boxes.dtype.kind == 'i':
        boxes = boxes.astype('float')

    pick = []
    
    x1 = boxes[:,0]
    y1 = boxes[:,1]
    x2 = boxes[:,2]
    y2 = boxes[:,3]
    
    score = boxes[:,4]

    aera = (x2 - x1 + 1) * (y2 - y1 + 1)
    #按照评分的升序排列
    index = np.argsort(score)[: : -1]

    while len(index) > 0:
      
        i = index[0]
        
        pick.append(i)
        
        xx1 = np.maximum(x1[i],x1[index[1:]])
        yy1 = np.maximum(y1[i],y1[index[1:]])
        xx2 = np.minimum(x2[i],x2[index[1:]])
        yy2 = np.minimum(y2[i],y2[index[1:]])

        w = np.maximum(0,xx2-xx1+1)
        h = np.maximum(0,yy2-yy1+1)

        if w>0 and h>0:
            overlap = (w*h)/(aera[i] + aera[1:] - (w*h))
        inds = np.where(overlap <= thresh)[0]
        index = index[inds + 1]

    return index
