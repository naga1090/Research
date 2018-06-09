import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from PIL import Image
import os
import colorsys

# By: Naga Nannapuneni
# VERSION 1.0.0
# Image analysis of Intervertebral Discs stained by Albumin blue and Fast Green
# NOTE: Change Directory (Line 4) ONCE, Change Image accordingly

# Changes Directory; CHANGE THIS TO THE LOCATION OF THE IMAGE FILE
os.chdir("/Users/naga/Desktop")

# Gets image for 3D Graph; CHANGE THIS TO THE IMAGE AT THE LOCATION DEFINED FROM LINE 9
getImage = Image.open("Histology Sample Image.jpg")
img = getImage.load()

# Constructs a blank matrix representing the pixels in the image
[xs, ys] = getImage.size
max_intensity = 100
hues = {}

# Examines each pixel in the image file
for x in range(0, xs):
  for y in range(0, ys):

    [r, g, b] = img[x, y]

    r /= 255.0
    g /= 255.0
    b /= 255.0

    [h, s, v] = colorsys.rgb_to_hsv(r, g, b)
    if h not in hues:
      hues[h] = {}
    if v not in hues[h]:
      hues[h][v] = 1
    else:
      if hues[h][v] < max_intensity:
        hues[h][v] += 1

# Creates 3D Graph
h_ = []
v_ = []
i = []
colours = []

for h in hues:
  for v in hues[h]:
    h_.append(h)
    v_.append(v)
    i.append(hues[h][v])
    [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
    colours.append([r, g, b])

# Plots the graph
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.scatter(h_, v_, i, s=10, c=colours, lw=0)

ax.set_xlabel('Hue')
ax.set_ylabel('Value')
ax.set_zlabel('Intensity')
fig.add_axes(ax)
plt.show()

# Opens image and converts it into 8-bit greyscale for 2D graph
# CHANGE THIS TO THE IMAGE AT THE LOCATION DEFINED FROM LINE 9
img2 = Image.open('Histology Sample Image.jpg').convert('L')
WIDTH, HEIGHT = img2.size

# Converts image data to a list of integers
data = list(img2.getdata())

# #Counts number of each greyscale number present in data
# print([[x,data.count(x)] for x in set(data)])

# Gets length of original untouched data
print(len(data))

# Delets the surrounding darkness, not part of sample
for i in data:
    if i < 6:
        data = [w for w in data if w !=i]

# Prints length of edited, raw data
print(len(data))

# Creates a copy of original data called a
a = data

# Deletes dark spots in data
for i in a:
    if i < 25:
        a = [w for w in a if w !=i]

# Prints length of copy array after deletion of dark spots
print(len(a))

# Prints Percentage of data that is tissue
print(len(a)/len(data)*100)

# Creates 2D Graph
labels, values = zip(*Counter(a).items())
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()
