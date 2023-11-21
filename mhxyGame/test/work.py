# 定义四边形A和四边形B的坐标
A_top_left = (0, 0)
A_bottom_right = (1920, 1080)

B_top_left_relative_to_A = (635, 269)
B_bottom_right_relative_to_A = (1444, 930)

# 定义四边形C的坐标
C_top_left_relative_to_B = (760, 480)
C_bottom_right_relative_to_B = (1317, 766)

# 定义点d相对于C的坐标
d_relative_to_C = (100, 200)

# 计算四边形B相对于A的坐标
B_top_left_absolute = (A_top_left[0] + B_top_left_relative_to_A[0], A_top_left[1] + B_top_left_relative_to_A[1])

# 计算四边形C相对于A的坐标
C_top_left_absolute = (B_top_left_absolute[0] + C_top_left_relative_to_B[0], B_top_left_absolute[1] + C_top_left_relative_to_B[1])

# 计算点d相对于A的坐标
d_absolute_position = (C_top_left_absolute[0] + d_relative_to_C[0], C_top_left_absolute[1] + d_relative_to_C[1])

print("点d相对于A的坐标为:", d_absolute_position)