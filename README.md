# Image Encryption Tool

This application allows users to encrypt and decrypt images using pixel manipulation.

## Features
- Encrypt images
- Decrypt images

## Requirements
- Python 3.x
- `customtkinter`
- `Pillow`
- `numpy`

## Installation and Running the Code

### For Developers:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/aisaac498/PRODIGY_CS_04.git
    cd image-encryption-tool
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv cphr
    source cphr/bin/activate  # On Windows, use `cphr\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```sh
    pip install customtkinter Pillow numpy
    ```

4. **Run the Application**:
    ```sh
    python encrypt_pixel.py
    ```

### For Prodigy Reviewers:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/aisaac498/PRODIGY_CS_04.git
    cd image-encryption-tool
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv cphr
    source cphr/bin/activate  # On Windows, use `cphr\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```sh
    pip install customtkinter Pillow numpy
    ```

4. **Run the Application**:
    ```sh
    python encrypt_pixel.py
    ```

## Usage
- Click "Encryption" to load an image, encrypt it, and save the encrypted image and key.
- Click "Decryption" to load an encrypted image, load the key, decrypt the image, and save the decrypted image.

## License
This project is licensed under the MIT License.
