import random
import cv2
import numpy as np


def random_hexstring_color():
    """generate random hexstring color"""
    return "{:06X}".format(random.randint(0, 0xFFFFFF))
    
    
def blank_image(height, width, layers=3, value=255):
    """create blank image, with specified shape, layers and initial value"""
    img = np.ones((height, width, layers), dtype=np.uint8)*value
    return img
    
    
def show_image(title, image):
    """
    WINDOW_AUTOSIZE
    WINDOW_FREERATIO
    WINDOW_FULLSCREEN
    WINDOW_GUI_EXPANDED
    WINDOW_GUI_NORMAL
    WINDOW_KEEPRATIO
    WINDOW_NORMAL
    WINDOW_OPENGL
    """
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return True
    
    
def roll_image(img, x_axis, y_axis):
    """roll specified img in x_axis(px) and y_axis(px)"""
    img = np.roll(img, y_axis, axis=0)   # axis: 0-up-down, 1-right-left
    img = np.roll(img, x_axis, axis=1)   # axis: 0-up-down, 1-right-left
    return img
    
    
def convert_rotation(deg, radius):
    """convert rotation in degree to radius"""
    # R layer
    R_a = math.cos((deg/360)*2*math.pi)*radius
    R_b = math.sin((deg/360)*2*math.pi)*radius
    # G layer
    G_a = math.cos(((deg+120)/360)*2*math.pi)*radius
    G_b = math.sin(((deg+120)/360)*2*math.pi)*radius
    # B layer
    B_a = math.cos(((deg+240)/360)*2*math.pi)*radius
    B_b = math.sin(((deg+240)/360)*2*math.pi)*radius
    dictio = {"R_a":R_a,
              "R_b":R_b,
              "G_a":G_a,
              "G_b":G_b,
              "B_a":B_a,
              "B_b":B_b}
    dictio = dict(zip(dictio.keys(), [round(item) for item in list(dictio.values())]))
    return dictio
    
    
def roll_layers(img, deg, radius):
    """roll specified img layers with degree and radius"""
    dictio = convert_rotation(deg, radius)
    img_copy = img.copy()
    
    b_channel, g_channel, r_channel = cv2.split(img_copy)                  # split to R-G-B
    b_channel = roll_image(b_channel, dictio['B_a'], dictio['B_b'])     # move each one
    g_channel = roll_image(g_channel, dictio['G_a'], dictio['G_b'])
    r_channel = roll_image(r_channel, dictio['R_a'], dictio['R_b'])
    img_BGRA = cv2.merge((b_channel, g_channel, r_channel))             # join layers
    return img_BGRA
    
    
if __name__ == "__main__":
    pass
    