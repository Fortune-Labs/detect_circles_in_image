import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to detect and highlight circles in an image
def highlight_circles_in_image(image_path):
    # Step 1: Read the input image
    original_image = cv2.imread(image_path)
    
    # Step 2: Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Step 3: Apply edge detection to identify the edges in the image
    edge_image = cv2.Canny(gray_image, threshold1=30, threshold2=100)
    
    # Step 4: Use the Hough Transform to detect circles in the edge-detected image
    min_radius = 10  # Minimum radius of circles to be detected
    max_radius = 100  # Maximum radius of circles to be detected
    circles = cv2.HoughCircles(edge_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=min_radius, maxRadius=max_radius)
    
    # Step 5: Highlight the detected circles in the original image
    if circles is not None:
        circles = np.uint16(np.around(circles))
        highlighted_image = original_image.copy()
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(highlighted_image, center, radius, (0, 0, 255), 3)
    else:
        highlighted_image = original_image.copy()
    
    # Display the result
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(highlighted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Detected Circles')
    axes[1].axis('off')
    plt.show()

# Usage
image_path = 'path/to/your/image.jpg'  # Replace with the actual image path
highlight_circles_in_image(image_path)
