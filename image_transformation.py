    
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageTransformation:
   
    _image:any
    
    
    def __init__(self, image):
        self._image = image
    
    def logarithmicTransformation(self):
        c = 255 / np.log(1 + np.max(self._image))
        log_image = c * (np.log(self._image + 1))
        
        log_image = np.array(log_image, dtype = np.uint8)
        
        cv2.imwrite('./assets/cat-edited.png', log_image)
    
    def powerLawTransformation(self, gamma):
        c = 255 / (255 ** gamma)
        power_image = c * (self._image ** gamma)
        
        power_image = np.array(power_image, dtype = np.uint8)
        
        cv2.imwrite('./assets/cat-edited.png', power_image)
    
    # def piecewiseLinearTransformation(self, r1, s1, r2, s2):
    #     c = 255 / (r2 - r1)
    #     piece_image = c * (self._image - r1) + s1
        
    #     piece_image = np.array(piece_image, dtype = np.uint8)
        
    #     cv2.imwrite('./assets/cat-edited.png', piece_image)

    def bitPlaneSlicing(self, bit):
        bit_image = self._image.copy()
        bit_image = cv2.cvtColor(bit_image, cv2.COLOR_BGR2GRAY)
        bit_image = bit_image >> bit
        bit_image = bit_image & 1
        bit_image = bit_image * 255
        
        cv2.imwrite('./assets/cat-edited.png', bit_image)
    
    def imageNegativeTransformation(self):
        negative_image = 255 - self._image
        cv2.imwrite('./assets/cat-edited.png', negative_image)
        
    def localHistogramEqualization(self):
        gray_image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        local_image = clahe.apply(gray_image)
        
        cv2.imwrite('./assets/cat-edited.png', local_image)
        
    def globalHistogramEqualization(self):
        gray_image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        global_image = cv2.equalizeHist(gray_image)
        
        cv2.imwrite('./assets/cat-edited.png', global_image)
    
    def espacialMedianFilter(self, size):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        median_image = cv2.medianBlur(image, size)
        
        cv2.imwrite('./assets/cat-edited.png', median_image)
    
    def espacialMeanFilter(self, size):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        mean_image = cv2.blur(image, (size, size))
        
        cv2.imwrite('./assets/cat-edited.png', mean_image)
    
    def laplacianFilter(self):
        laplacian_image = cv2.Laplacian(self._image, cv2.CV_64F)
        
        cv2.imwrite('./assets/cat-edited.png', laplacian_image)
    
    def sobelFilter(self):
        sobel_image = cv2.Sobel(self._image, cv2.CV_64F, 1, 0, ksize=5)
        
        cv2.imwrite('./assets/cat-edited.png', sobel_image)
    
    def highBoostFilter(self,boost_factor):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        resultant_image = image.copy()
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                blur_factor = (image[i-1, j-1] + image[i-1, j] - image[i-1, j+1] + image[i, j-1] + image[i, j] + image[i, j+1] + image[i+1, j+1] + image[i+1, j] + image[i+1, j+1])/9
                mask = boost_factor*image[i, j] - blur_factor
                resultant_image[i, j] = image[i, j] + mask
        
        cv2.imwrite('./assets/cat-edited.png', resultant_image)
    
    def RobertsFilter(self):
        roberts_image = cv2.filter2D(self._image, -1, np.array([[0, 1], [-1, 0]]))
        
        cv2.imwrite('./assets/cat-edited.png', roberts_image)

    def erosion(self, kernel):
        erosion_image = cv2.erode(self._image, kernel, iterations=1)
        
        cv2.imwrite('./assets/cat-edited.png', erosion_image)
    
    def dilation(self, kernel):
        dilation_image = cv2.dilate(self._image, kernel, iterations=1)
        
        cv2.imwrite('./assets/cat-edited.png', dilation_image)
    
    def opening(self, kernel):
        opening_image = cv2.morphologyEx(self._image, cv2.MORPH_OPEN, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', opening_image)
        
    def closing(self, kernel):
        closing_image = cv2.morphologyEx(self._image, cv2.MORPH_CLOSE, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', closing_image)
    
    def hitOrMiss(self, kernel):
        hit_image = cv2.morphologyEx(self._image, cv2.MORPH_HITMISS, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', hit_image)

    def boundaryExtraction(self):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        boundary_image = image.copy()
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                if image[i, j] == 0:
                    if image[i-1, j-1] == 255 or image[i-1, j] == 255 or image[i-1, j+1] == 255 or image[i, j-1] == 255 or image[i, j+1] == 255 or image[i+1, j-1] == 255 or image[i+1, j] == 255 or image[i+1, j+1] == 255:
                        boundary_image[i, j] = 255
                else:
                    boundary_image[i, j] = 255
        
        cv2.imwrite('./assets/cat-edited.png', boundary_image)

    def holeFilling(self):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        hole_image = image.copy()
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                if image[i, j] == 0:
                    if image[i-1, j-1] == 255 and image[i-1, j] == 255 and image[i-1, j+1] == 255 and image[i, j-1] == 255 and image[i, j+1] == 255 and image[i+1, j-1] == 255 and image[i+1, j] == 255 and image[i+1, j+1] == 255:
                        hole_image[i, j] = 255
        
        cv2.imwrite('./assets/cat-edited.png', hole_image)

    def connectedComponents(self):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image, 127, 255, 0)
        output = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)
        num_labels = output[0]
        labels = output[1]
        stats = output[2]
        centroids = output[3]
        
        for i in range(1, num_labels):
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imwrite('./assets/cat-edited.png', image)

    def watershed(self):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        sure_bg = cv2.dilate(opening, kernel, iterations=3)
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg, sure_fg)
        ret, markers = cv2.connectedComponents(sure_fg)
        markers = markers+1
        markers[unknown==255] = 0
        markers = cv2.watershed(self._image, markers)
        self._image[markers == -1] = [255, 0, 0]
        
        cv2.imwrite('./assets/cat-edited.png', self._image)
    
    def regionGrowing(self):
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        seed = (0, 0)
        mask = np.zeros(image.shape, np.uint8)
        cv2.floodFill(image, mask, seed, 255)
        
        cv2.imwrite('./assets/cat-edited.png', image)