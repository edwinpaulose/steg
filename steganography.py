from PIL import Image


def convert_to_grayscale(image):
    return image.convert('L')


def embed_image(cover_image, secret_image, output_path):
    cover = Image.open(cover_image)
    secret = Image.open(secret_image)

   
    if cover.size != secret.size:
        raise ValueError("Both images must have the same dimensions")

    cover = convert_to_grayscale(cover)
    secret = convert_to_grayscale(secret)

    
    cover_pixels = list(cover.getdata())
    secret_pixels = list(secret.getdata())

   
    embedded_pixels = []
    for cover_pixel, secret_pixel in zip(cover_pixels, secret_pixels):
        new_pixel_value = (cover_pixel & 0xFE) | (secret_pixel >> 7)
        embedded_pixels.append(new_pixel_value)


    embedded_image = Image.new('L', cover.size)
    embedded_image.putdata(embedded_pixels)

    
    embedded_image.save(output_path)

if __name__ == "__main__":
    cover_image = "cover.png"
    secret_image = "secret.png"
    output_image = "steg_image.png"

    embed_image(cover_image, secret_image, output_image)
    print("Image embedded successfully.")
