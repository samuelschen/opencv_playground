import sys
import os.path
import cv2
import numpy
from scipy.ndimage import label

# reference: http://stackoverflow.com/questions/11294859/how-to-define-the-markers-for-watershed-in-opencv

def segment_on_dt(a, img, thres):
    border = cv2.dilate(img, None, iterations=5)
    border = border - cv2.erode(border, None)

    dt = cv2.distanceTransform(img, 2, 3)
    dt = ((dt - dt.min()) / (dt.max() - dt.min()) * 255).astype(numpy.uint8)
    _, dt = cv2.threshold(dt, thres, 255, cv2.THRESH_BINARY)

    lbl, ncc = label(dt) # label and its num_of_features
    lbl = lbl * (255/ncc)
    # Completing the markers now. 
    lbl[border == 255] = 255

    lbl = lbl.astype(numpy.int32)
    cv2.watershed(a, lbl)

    lbl[lbl == -1] = 0
    lbl = lbl.astype(numpy.uint8)
    return 255 - lbl

def num_major_segment(img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256]) # compute histogram
    low_values_indices = hist < 10*10  # Where values are low (small than 10*10 pixals)
    hist[low_values_indices] = 0  # All low values set to 0
    print "Segement count:", numpy.count_nonzero(hist) - 1 # remove one background

def thres_from_args():
    try:
        return int(sys.argv[2])
    except IndexError:
        print "Use zero as threshold"
        return 0
    except ValueError:
        print "Not valid number, use zero as threshold"
        return 0

#############################################################################################
# main function 
#############################################################################################

img = cv2.imread(sys.argv[1])
thres = thres_from_args()

# segment image and overlay image
seg = os.path.splitext(sys.argv[1])[0] + '_seg' + os.path.splitext(sys.argv[1])[1]
lay = os.path.splitext(sys.argv[1])[0] + '_lay' + os.path.splitext(sys.argv[1])[1]

# Pre-processing.
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, numpy.ones((3, 3), dtype=int))

cv2.imwrite(seg, img_bin)

result = segment_on_dt(img, img_bin, thres)
cv2.imwrite(seg, result)

num_major_segment(result)

result[result != 255] = 0
result = cv2.dilate(result, None)
img[result == 255] = (0, 0, 255)
cv2.imwrite(lay, img)

