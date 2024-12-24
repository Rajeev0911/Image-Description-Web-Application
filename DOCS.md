# Image Captioning Web Application Documentation

## Overview

This web application allows users to upload an image, and it generates a caption describing the contents of the image. The caption generation is powered by the Hugging Face **BLIP** (Bootstrapping Language-Image Pre-training) model.

The application is built using **Flask**, a lightweight Python web framework, and it leverages the Hugging Face `transformers` library to use the pre-trained **BLIP model** for image captioning.

## Application Flow

1. **Upload an Image**: The user uploads an image using the front-end interface (HTML/JS).
2. **Process the Image**: The image is sent to the Flask server as a POST request.
3. **Caption Generation**: The Flask server processes the image with the BLIP model and generates a caption.
4. **Display Caption**: The caption is sent back to the front-end and displayed to the user.

## Technologies Used

- **Flask**: A Python web framework used to serve the application.
- **Hugging Face `transformers`**: Provides the pre-trained BLIP model for image captioning.
- **Werkzeug**: Used for secure file handling.
- **Pillow (PIL)**: Used for image handling and processing.
- **CORS (Cross-Origin Resource Sharing)**: Enables cross-origin requests between the front-end (HTML/JS) and back-end (Flask).
- **HTML, CSS, JavaScript**: Used for building the front-end interface.