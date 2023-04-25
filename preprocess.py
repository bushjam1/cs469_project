from PIL import Image, ImageFilter, ImageOps, ImageDraw
import sys

# take filename passed from stdin
if len(sys.argv) < 2 or len(sys.argv) > 2:
    raise Exception("usage: preprocess.py [filename]")
infile = sys.argv[1]

# open and load passed file
with Image.open(infile) as img:
    img.load()

# grayscale 
def grayscale(img):
    return img.convert("L")

# edging
def edge(img):
    return img.filter(ImageFilter.FIND_EDGES)

# thresholding 
def threshold(img, thresh):
    return img.point(lambda x: 255 if x > thresh else 0)

# invert
def invert(img):
    return ImageOps.invert(img)

# show loaded image
# img.show()

img_gray = grayscale(img)
# img_gray.show()

img_edge = edge(img_gray)
# img_edge.show()
# img_edge_enhance = img_edge.filter(ImageFilter.EDGE_ENHANCE)
# img_edge_enhance.show()
img_threshold = threshold(img_gray, 100)
# img_threshold.show()

img_threshold.show()

img_invert = invert(img_threshold)
img_invert.show()