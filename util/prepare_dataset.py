import math
import CV2
import os


def get_box_img(x: int, y: int, w: int, h: int, angle: float) -> list[float]:
    
    """
    Calculate a new corner based on the original coordinates and rotation angle
    for example:[x, y, w, h, ang] -> [x1, y1, x2, y2, x3, y3, x4, y4] (ICDAR)
    """
    
    # calculate centerpoint of each rect
    x_0 = x + w / 2
    y_0 = y + h / 2
    
    # calculate Half diagonal
    l = math.sqrt(pow(w / 2, 2) + pow(h / 2, 2))
    
    # if angle < 0, counterclockwise rotation
    if angle < 0:
      
      # angle +- <diagonal, baseline>
      a_1 = - angle + math.atan(h / float(w))
      a_2 = - angle - math.atan(h / float(w))
      
      # calculate each conor after rotating
      pt_1 = (x_0 - 1 * math.cos(a_1), y_0 - 1 * math.sin(a_1))
      pt_2 = (x_0 + 1 * math.cos(a_2), y_0 + 1 * math.sin(a_2))
      pt_3 = (x_0 + 1 * math.cos(a_1), y_0 + 1 * math.sin(a_1))
      pt_4 = (x_0 - 1 * math.cos(a_2), y_0 - 1 * math.sin(a_2))
      
      return [pt_1[0], pt_1[1], pt_2[0], pt_2[1], pt_3[0], pt_3[1], pt_4[0], pt_4[1]]
      
      
