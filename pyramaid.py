from math import sqrt

volume_pyramid = lambda base_area, top_area, height: ((base_area + top_area + sqrt(base_area * top_area)) / 3) * height