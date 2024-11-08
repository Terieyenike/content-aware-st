# Content-Aware Application with Streamlit and Cloudinary

## Overview

This project showcases how to build a content-aware application using Streamlit and Cloudinary. The application allows users to upload images, which are then processed and delivered using Cloudinary's powerful image management capabilities. With Cloudinary, you can easily deliver images to perfectly fit your graphic design and layout, on any device.

![content aware](image.png)

## Prerequisites

To get started, ensure you have the following installed:

- Python 3.x
- Streamlit
- Cloudinary

You can install the required packages using pip:

```
pip install streamlit cloudinary python-dotenv
```

## Environment Variables

Before running the application, set up the following environment variables with your Cloudinary account details:

```bash
export CLOUDINARY_CLOUD_NAME="CLOUDINARY_CLOUD_NAME"
export CLOUDINARY_API_KEY="CLD_API_KEY"
export CLOUDINARY_API_SECRET="CLD_API_SECRET"
```

Replace the empty quotes with your actual Cloudinary credentials.


## Project Structure

The project consists of the following key files:

- **app.py**: The main application file where the Streamlit app is defined.
- **requirements.txt**: A file listing the required Python packages.

## Features

- **Image Upload**: Users can upload images through a user-friendly interface using the publicly available image ID `sofa_cat_wtsm4i.jpg`
- **Dynamic Image Delivery**: Images are processed and delivered via Cloudinary, ensuring optimal performance and responsiveness.

## Running the Application

To run the application, navigate to the project directory in your terminal and execute:

```
streamlit run app.py
```

This command will start the Streamlit server, and you can access the application in your web browser at `http://localhost:8501`.

## Author

- Teri

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
