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
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv enpix
    source enpix/bin/activate  # On Windows, use `enpix\Scripts\activate`
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
    ```
    
2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv enpix
    source enpix/bin/activate  # On Windows, use `enpix\Scripts\activate`
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

## Developer Notes
- This application was developed for cross-platform compatibility but primarily tested on Windows machines.
- Ensure that all required images (`sun.png`, `moon.png`, etc.) are present in the `images` directory if you implement the light/dark mode toggle in the future.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
