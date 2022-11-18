    
import cv2
import numpy as np
import matplotlib.pyplot as plt

class ImageTransformation:
   
    _image:any
    #private variable
    
    
    def __init__(self, image):
        self._image = image
    
    def logarithmicTransformation(self):
        # Apply log transformation method
        c = 255 / np.log(1 + np.max(self._image))
        log_image = c * (np.log(self._image + 1))
        
        # Specify the data type so that
        # float value will be converted to int
        log_image = np.array(log_image, dtype = np.uint8)
        
        cv2.imwrite('./assets/cat-edited.png', log_image)
    
    def powerLawTransformation(self, gamma):
        # Apply power law transformation method
        c = 255 / (255 ** gamma)
        power_image = c * (self._image ** gamma)
        
        # Specify the data type so that
        # float value will be converted to int
        power_image = np.array(power_image, dtype = np.uint8)
        
        cv2.imwrite('./assets/cat-edited.png', power_image)
    
    # def piecewiseLinearTransformation(self, r1, s1, r2, s2):
    #     # Apply piecewise linear transformation method
    #     c = 255 / (r2 - r1)
    #     piece_image = c * (self._image - r1) + s1
        
    #     piece_image = np.array(piece_image, dtype = np.uint8)
        
    #     cv2.imwrite('./assets/cat-edited.png', piece_image)

    def bitPlaneSlicing(self, bit):
        # Apply bit plane slicing method
        bit_image = self._image.copy()
        bit_image = cv2.cvtColor(bit_image, cv2.COLOR_BGR2GRAY)
        bit_image = bit_image >> bit
        bit_image = bit_image & 1
        bit_image = bit_image * 255
        #transform in gray
        
        cv2.imwrite('./assets/cat-edited.png', bit_image)
    
    def imageNegativeTransformation(self):
        # Apply image negative transformation method
        negative_image = 255 - self._image
        #save image
        cv2.imwrite('./assets/cat-edited.png', negative_image)
        
    def localHistogramEqualization(self):
        # Apply local histogram equalization method
        gray_image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        local_image = clahe.apply(gray_image)
        
        cv2.imwrite('./assets/cat-edited.png', local_image)
        
    def globalHistogramEqualization(self):
        # Apply global histogram equalization method
        gray_image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        global_image = cv2.equalizeHist(gray_image)
        
        cv2.imwrite('./assets/cat-edited.png', global_image)
    
    def espacialMedianFilter(self, size):
        # Apply spacial median filter method
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        median_image = cv2.medianBlur(image, size)
        
        cv2.imwrite('./assets/cat-edited.png', median_image)
    
    def espacialMeanFilter(self, size):
        # Apply spacial mean filter method
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        mean_image = cv2.blur(image, (size, size))
        
        cv2.imwrite('./assets/cat-edited.png', mean_image)
    
    def laplacianFilter(self):
        # Apply laplacian filter method
        laplacian_image = cv2.Laplacian(self._image, cv2.CV_64F)
        
        cv2.imwrite('./assets/cat-edited.png', laplacian_image)
    
    def sobelFilter(self):
        # Apply sobel filter method
        sobel_image = cv2.Sobel(self._image, cv2.CV_64F, 1, 0, ksize=5)
        
        cv2.imwrite('./assets/cat-edited.png', sobel_image)
    
    def highBoostFilter(self,boost_factor):
        # Apply high boost filter method
        image = cv2.cvtColor(self._image, cv2.COLOR_BGR2GRAY)
        resultant_image = image.copy()
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                blur_factor = (image[i-1, j-1] + image[i-1, j] - image[i-1, j+1] + image[i, j-1] + image[i, j] + image[i, j+1] + image[i+1, j+1] + image[i+1, j] + image[i+1, j+1])/9
                mask = boost_factor*image[i, j] - blur_factor
                resultant_image[i, j] = image[i, j] + mask
        
        cv2.imwrite('./assets/cat-edited.png', resultant_image)
    
    def RobertsFilter(self):
        # Apply Roberts filter method
        roberts_image = cv2.filter2D(self._image, -1, np.array([[0, 1], [-1, 0]]))
        
        cv2.imwrite('./assets/cat-edited.png', roberts_image)

    def erosion(self, kernel):
        # Apply erosion method
        erosion_image = cv2.erode(self._image, kernel, iterations=1)
        
        cv2.imwrite('./assets/cat-edited.png', erosion_image)
    
    def dilation(self, kernel):
        # Apply dilation method
        dilation_image = cv2.dilate(self._image, kernel, iterations=1)
        
        cv2.imwrite('./assets/cat-edited.png', dilation_image)
    
    def opening(self, kernel):
        # Apply opening method
        opening_image = cv2.morphologyEx(self._image, cv2.MORPH_OPEN, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', opening_image)
        
    def closing(self, kernel):
        # Apply closing method
        closing_image = cv2.morphologyEx(self._image, cv2.MORPH_CLOSE, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', closing_image)
    
    def hitOrMiss(self, kernel):
        # Apply hit or miss method
        hit_image = cv2.morphologyEx(self._image, cv2.MORPH_HITMISS, kernel)
        
        cv2.imwrite('./assets/cat-edited.png', hit_image)

    