from sklearn import datasets
import scipy.misc
import numpy as np
digits = datasets.load_digits()

# print(digits.keys())
# print(digits.target_names)
# print(digits.target[0])

# Inspect the shape
digits_data = digits.data

print(digits_data.shape)


# Isolate the target values with `target`
digits_target = digits.target

# Inspect the shape
print(digits_target.shape)

# Print the number of unique labels
number_digits = len(np.unique(digits.target))

# Isolate the `images`
digits_images = digits.images

# Inspect the shape
print(digits_images.shape)

from PIL import Image
im = Image.fromarray(digits_images[0])
im.save("hello.jpeg")