import numpy as np
from PIL import Image

def sobel_edge_detection(image_path):
    # Load the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    img = np.array(img)

    # Sobel Kernels
    Gx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Initialize matrices for gradients
    Ix = np.zeros_like(img)
    Iy = np.zeros_like(img)

    # Sobel Edge Detection
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            Ix[i, j] = np.sum(Gx * img[i-1:i+2, j-1:j+2]) # Horizontal
            Iy[i, j] = np.sum(Gy * img[i-1:i+2, j-1:j+2]) # Vertical

    # Calculate the gradient magnitude
    G = np.sqrt(Ix ** 2 + Iy ** 2)

    # Normalize to the range 0 to 255
    G = (G / G.max()) * 255
    G = G.astype(np.uint8)  # Convert to uint8
    return G

# Example usage
file_path = 'app/files/image2.jpg'  # Replace with your file path
edges = sobel_edge_detection(file_path)
Image.fromarray(edges).save("app/files/image2-edge.jpg")
