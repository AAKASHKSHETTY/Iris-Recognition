# Iris-Recognition
Python

## Introduction

Biometrics are biological — or physical — measures that can be used to identify people. Fingerprint scanning, facial recognition, and retinal scanners are all examples of biometric technology, but these are just the most known choices. Iris recognition is the most accurate and precise method of biometric identification. Segmentation of iris is one of the essential processing measures in an iris identification procedure. The key objective of this iris segmentation phase is to classify the correct area of the iris for recognition purposes. However, upper and lower eyelids, eyelashes, light reflections, shadows obstruct iris texture regions. Iris segmentation thus includes the localization of the eyelids and the removal of the effects of occlusions caused by eyelashes, shadows and light reflections. The performance of the iris segmentation method adopted directly affects the overall efficiency of Iris recognition. On the one hand, it is important for the high quality of the derived iris characteristics used for identification, while, on the other, it is a determining factor of the biometrically real-time response since it is the most time- consuming element of an iris recognition system.

## Implementation

<img width="816" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/4c545444-20de-4cb7-bd33-34f97d041807">

### Image Acquisition:
This section is a part that helps acquire images from source like a user of datasets. Image is acquired using IMREAD for further processing. This image is later used for preprocessing and then is taken for the segmentation process which can help us decide how the images should be dealt for further processing. The functions called in the above images is used to process the input image.

<img width="280" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/9e133a1c-c3bd-468e-9339-93c41a7107c0">

### Image Preprocessing:
Image that are acquired are sent for preprocessing where we have used thresholding to segregate the pupil from the rest of the image and then sequentially applied medianBlur as we require a defined edge for the boundaries. It also helps get rid of any noise if present in the image. This all processes is done on a copy of the original image since the original image is required for further varied processes.

<img width="620" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/51e14627-4d84-4b5b-973a-6160ead0d4d8">

### Detecting pupil Coordinates:
We need to develop a circle that encapsulates the pupil to get segmentation. Thus, we need the coordinates of the pupil centre and it’s radius. For this process we have used the Hough Circle that takes parameters: (input image, circle detection method, inverse ratio of resolution, Minimum distance between detected centres, Upper threshold for the internal Canny edge detector, Threshold for centre detection, minimum and maximum radius of the circle)

<img width="299" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/d38e3596-4157-4dd4-b30f-edc28839f9d7">

### Detecting Iris Coordinates And Getting the Segments:

Similar to the pupil detection iris recognition also makes use of the hough circle to get the radius for circle detection with same parameters except the one for the minimum radius as the radius has to be greater than the pupil’s the radius is taken higher. Then the required circle is plotted to get a rough idea of only the iris segment.

<img width="315" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/7fce572c-76ad-450a-9dbd-3bd3fab26467">

### Encoding the unwrapped iris:
Images are encoded using a mathematical formula. The centre coordinates and the radius is taken as input and using these values a systematic mathematical code is generated. For this linespace is used which generates random values and is applied to develop unique pattern for representation of the segmented area. This system of coordinates generated is further sent for processing for feature extraction.

<img width="455" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/c62f0630-7a76-48c0-9346-3a6e0212d184">

### Feature Extraction from Encoded information:

The Gabor feature extraction method is used for the encoded values from the previous step and is later extracted as digital information. This digital information is as unique as the iris. The convolution is done and a code is generated for the development of a monochrome digital information which captures the uniqueness of the image.

<img width="442" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/02238471-20bb-4d84-9d12-efb84d594abc">

### Comparing two different iris:
The Last step is comparision between two entered images of iris and returns the difference. If the difference is seen to be 0, then iris is a match, otherwise it is a mismatch.

<img width="715" alt="image" src="https://github.com/AAKASHKSHETTY/Iris-Recognition/assets/58876667/79e16825-6e4e-4081-92ef-8ad83425b390">

### Conslusion

Image segmentation is the process of partitioning a digital image into multiple segments (sets of pixels, also known as image objects). The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze. We have tried to implement iris recognition using image segmentation, since, we felt that segmentation is a simple algorithm in image processing but is versatile as well. We read about iris recognition and realised that it has been tried with segmentation, but we did not find conclusive results. Hence, we decided to pre-process the image and use segmentation and we were able to achieve the desired results.
