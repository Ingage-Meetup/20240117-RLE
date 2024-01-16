from PIL import Image
import numpy as np

def add(a, b):
    return a + b

\
def subtract(a, b):
    return a - b

def readFile(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            return file_contents
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='cp1252') as file:
            file_contents = file.read()
        return file_contents
    
def readBinaryFile(file_path):

    with open(file_path, 'rb') as file:
        binary_data = file.read()
        try:
            text_data = binary_data.decode('utf-8')
            return text_data
        except UnicodeDecodeError: 
            print("Error")
            return "" 
    
def writeFile(file_path, contents):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(contents)

def rleParens(original_file_contents):
    if not original_file_contents:
        return "[]"
    prevChar = original_file_contents[0]
    charCount = 1
    encodedString = "["
    for char in original_file_contents[1:]:
        if char != prevChar:
            encodedString += "(" + str(prevChar) + "," + str(charCount) + "),"
            prevChar = char
            charCount=1
        else:
            charCount+=1
    encodedString += "(" + str(prevChar) + "," + str(charCount) + ")]"
    return encodedString

def rle(original_file_contents):
    if not original_file_contents:
        return ""
    prevChar = original_file_contents[0]
    charCount = 1
    encodedString = ""
    for char in original_file_contents[1:]:
        if char != prevChar:
            encodedString += str(prevChar) + str(charCount)
            prevChar = char
            charCount=1
        else:
            charCount+=1
    encodedString += str(prevChar) + str(charCount)
    return encodedString

def run_length_encode(img):
    """
    Apply simple run-length encoding to an image.
    """
    data = np.array(img)
    flat_data = data.flatten()
    encoded = []
    
    prev_pixel = flat_data[0]
    count = 1
    
    for pixel in flat_data[1:]:
        if pixel == prev_pixel:
            count += 1
        else:
            encoded.append((prev_pixel, count))
            prev_pixel = pixel
            count = 1

    # Add the last run
    encoded.append((prev_pixel, count))
    return encoded

def load_bitmap(file_path):
    """
    Load a bitmap image and convert it to grayscale.
    """
    img = Image.open(file_path).convert('L')  # Convert to grayscale
    return img


