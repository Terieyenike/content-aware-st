import streamlit as st
import cloudinary
from cloudinary import CloudinaryImage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

def generate_image_url(public_id: str, aspect_ratio: float, width: int) -> str:
    """
    Generates a Cloudinary image URL with content-aware cropping.

    Args:
        public_id (str): The public ID of the image in Cloudinary.
        aspect_ratio (float): Desired aspect ratio for cropping.
        width (int): Width for the output image.

    Returns:
        str: URL of the processed image.
    """
    image = CloudinaryImage(public_id)
    transformation = [
        {'aspect_ratio': aspect_ratio, 'gravity': "auto", 'width': width, 'crop': "fill"},
        {'quality': "auto"},
        {'fetch_format': "auto"}
    ]
    return image.build_url(transformation=transformation)

def main():
    st.title("AI-Powered Content-Aware Cropping with Cloudinary and Streamlit")
    st.write("This app demonstrates content-aware cropping using Cloudinary's AI capabilities.")

    # User input for Cloudinary image public ID
    public_id = st.text_input("Enter the Cloudinary image public ID:", "hjh1ji5iszp2qucxozuk.jpg")

    # Aspect ratio options with corresponding widths
    aspect_ratio_options = {
        "1:2": (0.5, 433),
        "5:2": (2.5, 1300),
        "1:1": (1.0, 867)
    }

    st.subheader("Aspect Ratio:")
    selected_option = st.radio("Select Aspect Ratio", list(aspect_ratio_options.keys()))

    # Get aspect ratio and width based on selection
    aspect_ratio, width = aspect_ratio_options[selected_option]

    # Generate and display image URL
    if public_id:
        image_url = generate_image_url(public_id, aspect_ratio, width)
        st.image(image_url, caption="Content-Aware Cropped Image")

if __name__ == "__main__":
    main()
