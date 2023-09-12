from PIL import Image

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    return image.convert('L')

# Function to embed a secret image into a cover image using LSB
def embed_image(cover_image, secret_image, output_path):
    cover = Image.open(cover_image)
    secret = Image.open(secret_image)

    # Ensure both images have the same dimensions
    if cover.size != secret.size:
        raise ValueError("Both images must have the same dimensions")

    cover = convert_to_grayscale(cover)
    secret = convert_to_grayscale(secret)

    # Get pixel data for both images
    cover_pixels = list(cover.getdata())
    secret_pixels = list(secret.getdata())

    # Embed secret image into the cover image using LSB
    embedded_pixels = []
    for cover_pixel, secret_pixel in zip(cover_pixels, secret_pixels):
        new_pixel_value = (cover_pixel & 0xFE) | (secret_pixel >> 7)
        embedded_pixels.append(new_pixel_value)

    # Create a new image with the embedded data
    embedded_image = Image.new('L', cover.size)
    embedded_image.putdata(embedded_pixels)

    # Save the embedded image to the specified output path
    embedded_image.save(output_path)

if __name__ == "__main__":
    cover_image = "cover.png"
    secret_image = "secret.png"
    output_image = "steg_image.png"

    embed_image(cover_image, secret_image, output_image)
    print("Image embedded successfully.")
