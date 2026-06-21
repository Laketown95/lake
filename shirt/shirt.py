from PIL import Image, ImageOps
import sys
import os

def main():
    # Check if the user specified exactly two command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python shirt.py input_image output_image")
        sys.exit(1)

    # Get the input and output file names
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input and output file names have valid extensions
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_extension = os.path.splitext(input_file)[1].lower()
    output_extension = os.path.splitext(output_file)[1].lower()
    if input_extension not in valid_extensions or output_extension not in valid_extensions:
        print("Invalid file extension. Only .jpg, .jpeg, and .png are supported.")
        sys.exit(1)

    # Check if the input and output file names have the same extension
    if input_extension != output_extension:
        print("Input and output file names must have the same extension.")
        sys.exit(1)

    # Check if the input file exists
    if not os.path.exists(input_file):
        print("Input file does not exist.")
        sys.exit(1)

    # Open the input image
    try:
        input_image = Image.open(input_file)
    except Exception as e:
        print(f"Failed to open input image: {e}")
        sys.exit(1)

    # Open the shirt image
    try:
        shirt_image = Image.open('shirt.png')
    except Exception as e:
        print(f"Failed to open shirt image: {e}")
        sys.exit(1)

    # Resize and crop the input image to the same size as the shirt image
    try:
        resized_input_image = ImageOps.fit(input_image, shirt_image.size)
    except Exception as e:
        print(f"Failed to resize and crop input image: {e}")
        sys.exit(1)

    # Overlay the shirt image on the resized input image
    try:
        output_image = resized_input_image.copy()
        output_image.paste(shirt_image, (0, 0), mask=shirt_image)
    except Exception as e:
        print(f"Failed to overlay shirt image: {e}")
        sys.exit(1)

    # Save the output image
    try:
        output_image.save(output_file)
    except Exception as e:
        print(f"Failed to save output image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


