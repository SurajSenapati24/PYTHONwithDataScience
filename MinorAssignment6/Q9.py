import numpy as np
def format_2d_array(arr):
    max_width = max(len(str(element)) for row in arr for element in row)
    return "\n".join(" ".join(f"{element:>{max_width}}" for element in row) for row in arr)

a=np.array([[1,2],[3,4]])
print(format_2d_array(a))