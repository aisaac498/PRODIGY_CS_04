# Image Encryption Tool

This application allows users to encrypt and decrypt images using pixel manipulation. Additionally, it features a light/dark mode toggle.

## Features
- Encrypt images
- Decrypt images
- Toggle between light and dark modes

## Requirements
- Python 3.x
- `customtkinter`
- `Pillow`
- `numpy`

## Installation

### For Progidy Reviewers:

1. **Download the Executable**:
   - Download the executable file from the provided link.
   - Double-click the `image_encryption_tool.exe` file to run the application.

### For Developers:

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/image-encryption-tool.git
    cd image-encryption-tool
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv enpix
    source enpix/bin/activate  # On Windows, use `enpix\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python encrypt_pixel.py
    ```

## Usage
- Click "Encryption" to load an image, encrypt it, and save the encrypted image and key.
- Click "Decryption" to load an encrypted image, load the key, decrypt the image, and save the decrypted image.
- Use the theme toggle button at the top right to switch between light and dark modes.

## License
This project is licensed under the MIT License.
