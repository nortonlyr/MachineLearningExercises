import numpy as np
import tensorflow as tf
arr = np.array([1, 5.5, 3, 15, 20])
tensor = tf.convert_to_tensor(arr,tf.float64)
print(tensor)


# import numpy as np
# arr = np.array([1, 5.5, 3, 15, 20])
# print(arr)
# print(arr.ndim)
# print(arr.shape)
# print(arr.dtype)