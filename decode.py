from PIL import Image

# Function to extract the secret image from the stego image using LSB
def extract_secret_image(steg_image):
    steg_pixels = steg_image.load()
    
    width, height = steg_image.size
    secret_image = Image.new('L', (width, height))
    secret_pixels = secret_image.load()

    for x in range(width):
        for y in range(height):
            steg_pixel = steg_pixels[x, y]
            
            # Extract the LSB of the stego pixel and set it as the secret pixel's value
            secret_pixel = steg_pixel & 1
            secret_pixels[x, y] = secret_pixel * 255  # Scale the pixel value to 0 or 255 for grayscale

    return secret_image

# Load the steg image
steg_image = Image.open('steg_image.png')

# Extract the secret image from the stego image
secret_image = extract_secret_image(steg_image)

# Save the extracted secret image
secret_image.save('Decoded_secret_image.png')

print("Secret image extracted and saved as 'Decoded_secret_image.png'.")