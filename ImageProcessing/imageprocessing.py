pip install Pillow

from PIL import Image, ImageFilter

def resize_image(input_path, output_path, new_width, new_height):
    """
    Resize the image to the specified width and height.
    """
    image = Image.open(input_path)
    resized_image = image.resize((new_width, new_height))
    resized_image.save(output_path)

def crop_image(input_path, output_path, left, top, right, bottom):
    """
    Crop the image using the specified coordinates.
    """
    image = Image.open(input_path)
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(output_path)

def apply_filter(input_path, output_path):
    """
    Apply a simple Gaussian blur filter to the image.
    """
    image = Image.open(input_path)
    filtered_image = image.filter(ImageFilter.GaussianBlur(5))
    filtered_image.save(output_path)

if __name__ == "__main__":
    # Replace these paths with the paths to your input and output images
    input_image_path = "input_image.jpg"
    resized_image_path = "resized_image.jpg"
    cropped_image_path = "cropped_image.jpg"
    filtered_image_path = "filtered_image.jpg"

    # Resize the image
    new_width = 300
    new_height = 200
    resize_image(input_image_path, resized_image_path, new_width, new_height)

    # Crop the image
    left = 50
    top = 50
    right = 250
    bottom = 150
    crop_image(input_image_path, cropped_image_path, left, top, right, bottom)

    # Apply a filter to the image
    apply_filter(input_image_path, filtered_image_path)

    print("Image processing completed!")

