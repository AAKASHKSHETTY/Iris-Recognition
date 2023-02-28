from segmentation import *
from coding import *


def compare_codes(a, b, mask_a, mask_b, rotation=False):
    if rotation:
        d = []
        for i in range(-rotation, rotation + 1):
            c = np.roll(b, i, axis=1)
            mask_c = np.roll(mask_b, i, axis=1)
            d.append(np.sum(np.remainder(a + c, 2) * mask_a * mask_c) / np.sum(mask_a * mask_c))
        return np.min(d)
    return np.sum(np.remainder(a + b, 2) * mask_a * mask_b) / np.sum(mask_a * mask_b)

def encode_photo(image):

    img = preprocess(image)
    x, y, r = find_pupil_hough(img)
    x_iris, y_iris, r_iris = find_iris_hough(img)
    iris = unravel_iris(image, x, y, r, x_iris, y_iris, r_iris)
    return iris_encode(iris)

if __name__ == '__main__':
    image = cv2.imread('iris1.bmp')
    image2 = cv2.imread('iris1.bmp')
    print(image.shape)
    print(image2.shape)
    code, mask = encode_photo(image)
    code2, mask2 = encode_photo(image2)

    if compare_codes(code, code2, mask, mask2) == 0:
        print(compare_codes(code, code2, mask, mask2))
        print("Iris Matched")
    else:
        print("No match found")
        print("Difference: "+str(compare_codes(code, code2, mask, mask2)))