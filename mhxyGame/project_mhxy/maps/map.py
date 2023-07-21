class Maps(object):
    """
    地图父类

    Parameters:name, top_left_corner, top_right_corner, left_lower_corner, right_lower_corner
    name:地图名字
    top_left_corner:左上角
    top_right_corner:右上角
    left_lower_corner:左下角
     right_lower_corner:右上角
    """
    def __init__(self, name, top_left_corner, top_right_corner, left_lower_corner, right_lower_corner):
        self.name = name
        self.top_left_corner = top_left_corner
        self.top_right_corner = top_right_corner
        self.left_lower_corner = left_lower_corner
        self.right_lower_corner = right_lower_corner
