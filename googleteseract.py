import cv2
import pytesseract
import matplotlib.pyplot as plt
from pylab import rcParams
from IPython.display import Image

# Configure plot size
rcParams['figure.figsize'] = 8, 16

# Load the image
file_name = "text.jpg"
img = cv2.imread(file_name)

# Display the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

# Perform OCR on the image
text_out = pytesseract.image_to_string(img)

# Display the extracted text
print(text_out)
