#this code works push to git hub
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import os
import json

# Global variables
current_image = None
encryption_key = None
is_encrypted = False
is_decrypted = False
encrypted_image_saved = False
marker_value = 255  # This can be any value that doesn't normally occur in the image

# Function to load the image
def load_image():
    global current_image, encryption_key, is_encrypted, is_decrypted, encrypted_image_saved
    try:
        file_path = filedialog.askopenfilename(title="Open Image to be Encrypted")
        if file_path:
            image = Image.open(file_path)
            img_display = ctk.CTkImage(light_image=image, size=(300, 300))  # Adjust size to fit GUI
            img_label.configure(image=img_display, text="")
            img_label.image = img_display
            current_image = image
            encryption_key = None
            is_encrypted = False
            is_decrypted = False
            encrypted_image_saved = False
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")

# Function to load the encrypted image
def load_encrypted_image():
    global current_image, encryption_key, is_encrypted, is_decrypted, encrypted_image_saved
    try:
        file_path = filedialog.askopenfilename(title="Open Encrypted Image")
        if file_path:
            image = Image.open(file_path)
            img_display = ctk.CTkImage(light_image=image, size=(300, 300))  # Adjust size to fit GUI
            img_label.configure(image=img_display, text="")
            img_label.image = img_display
            current_image = image
            encryption_key = None
            is_encrypted = False
            is_decrypted = False
            encrypted_image_saved = False
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {e}")

# Function to generate an encryption key
def generate_key(image):
    width, height = image.size
    channels = 4 if image.mode == 'RGBA' else 3
    key = np.random.randint(0, 256, (height, width, channels), dtype=np.uint8)
    return key

# Function to add a marker to the encrypted image
def add_marker(image):
    pixels = np.array(image)
    pixels[0, 0, 0] = marker_value  # Set a marker value at a known location
    return Image.fromarray(pixels, image.mode)

# Function to check for the marker in the encrypted image
def check_marker(image):
    pixels = np.array(image)
    return pixels[0, 0, 0] == marker_value

# Function to encrypt the image
def encrypt_image(image, key):
    pixels = np.array(image)
    key = key[:pixels.shape[0], :pixels.shape[1], :pixels.shape[2]]
    encrypted_pixels = np.bitwise_xor(pixels, key)
    encrypted_image = Image.fromarray(encrypted_pixels, image.mode)
    encrypted_image = add_marker(encrypted_image)
    return encrypted_image

# Function to decrypt the image
def decrypt_image(image, key):
    if not check_marker(image):
        raise ValueError("The provided image is not encrypted.")
    pixels = np.array(image)
    key = key[:pixels.shape[0], :pixels.shape[1], :pixels.shape[2]]
    decrypted_pixels = np.bitwise_xor(pixels, key)
    decrypted_image = Image.fromarray(decrypted_pixels, image.mode)
    return decrypted_image

# Handle encryption button click
def handle_encrypt():
    global encryption_key, is_encrypted
    if current_image:
        if encryption_key is None:
            encryption_key = generate_key(current_image)
            key_saved = save_key(encryption_key)
            if key_saved:
                encrypted_img = encrypt_image(current_image, encryption_key)
                display_image(encrypted_img)
                is_encrypted = True
            else:
                messagebox.showwarning("Warning", "Please select a name for the key")
                encryption_key = None
    else:
        messagebox.showwarning("Warning", "Please add an image to be encrypted")

# Handle decryption button click
def handle_decrypt():
    global encryption_key, is_decrypted
    if current_image:
        encryption_key = load_key("Select a Key")
        if encryption_key is not None:
            try:
                decrypted_img = decrypt_image(current_image, encryption_key)
                display_image(decrypted_img)
                is_decrypted = True
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Failed to load encryption key.")
    else:
        messagebox.showwarning("Warning", "Please add an image to be decrypted")

# Save the encryption key to a file
def save_key(key):
    key_file_path = filedialog.asksaveasfilename(title="Save Encryption Key", defaultextension=".key", filetypes=[("Key files", "*.key"), ("All files", "*.*")])
    if key_file_path:
        with open(key_file_path, 'w') as key_file:
            json.dump(key.tolist(), key_file)
        return True
    return False

# Load the encryption key from a file
def load_key(title="Select a Key"):
    key_file_path = filedialog.askopenfilename(title=title, filetypes=[("Key files", "*.key"), ("All files", "*.*")])
    if key_file_path:
        with open(key_file_path, 'r') as key_file:
            key = np.array(json.load(key_file), dtype=np.uint8)
        return key
    return None

# Display the image
def display_image(image):
    img_display = ctk.CTkImage(light_image=image, size=(300, 300))  # Adjust size to fit GUI
    img_label.configure(image=img_display, text="")
    img_label.image = img_display
    global current_image
    current_image = image

# Save the encrypted image to a file
def save_encrypted_image():
    global encrypted_image_saved
    if is_encrypted:
        try:
            file_path = filedialog.asksaveasfilename(title="Save Encrypted Image", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                current_image.save(file_path)
                encrypted_image_saved = True
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")
    else:
        messagebox.showwarning("Warning", "Please encrypt image before saving")

# Save the decrypted image to a file
def save_decrypted_image():
    if is_decrypted:
        try:
            file_path = filedialog.asksaveasfilename(title="Save Decrypted Image", defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                current_image.save(file_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {e}")
    else:
        messagebox.showwarning("Warning", "Please decrypt image before saving")

# Show encryption buttons
def show_encryption_buttons():
    hide_initial_buttons()
    clear_image()
    load_button.pack(side='left', padx=10)
    encrypt_button.pack(side='left', padx=10)
    save_encrypted_button.pack(side='left', padx=10)
    go_back_button_encryption.pack(side='left', padx=10)

# Show decryption buttons
def show_decryption_buttons():
    hide_initial_buttons()
    clear_image()
    load_encrypted_button.pack(side='left', padx=10)
    decrypt_button.pack(side='left', padx=10)
    save_decrypted_button.pack(side='left', padx=10)
    go_back_button_decryption.pack(side='left', padx=10)

# Hide all buttons and show initial buttons
def go_back_encryption():
    if not current_image or (current_image and not is_encrypted) or encrypted_image_saved:
        hide_encryption_buttons()
        clear_image()
        show_initial_buttons()
    elif is_encrypted and not encrypted_image_saved:
        messagebox.showwarning("Warning", "Please save the encrypted image")

def go_back_decryption():
    hide_decryption_buttons()
    clear_image()
    show_initial_buttons()

# Hide initial buttons
def hide_initial_buttons():
    encryption_button.pack_forget()
    decryption_button.pack_forget()

# Show initial buttons
def show_initial_buttons():
    encryption_button.pack(pady=20)
    decryption_button.pack(pady=20)

# Hide encryption buttons
def hide_encryption_buttons():
    load_button.pack_forget()
    encrypt_button.pack_forget()
    save_encrypted_button.pack_forget()
    go_back_button_encryption.pack_forget()

# Hide decryption buttons
def hide_decryption_buttons():
    load_encrypted_button.pack_forget()
    decrypt_button.pack_forget()
    save_decrypted_button.pack_forget()
    go_back_button_decryption.pack_forget()

# Clear the displayed image
def clear_image():
    blank_image = Image.new('RGBA', (300, 300), (255, 255, 255, 0))  # Adjust size to fit GUI
    img_display = ctk.CTkImage(light_image=blank_image, size=(300, 300))
    img_label.configure(image=img_display, text="")
    img_label.image = img_display
    global current_image, is_encrypted, is_decrypted, encrypted_image_saved
    current_image = None
    is_encrypted = False
    is_decrypted = False
    encrypted_image_saved = False

# Function to center the frame in the window
def center_frame(event=None):
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()
    x = (app.winfo_width() // 2) - (width // 2)
    y = (app.winfo_height() // 2) - (height // 2)
    frame.place(x=x, y=y)

# Initialize the app
app = ctk.CTk()
app.geometry("800x600")
app.title("Image Encryption Tool")

# Create a frame to contain all widgets
frame = ctk.CTkFrame(app)
frame.pack(expand=True)

# Bind the configure event to center the frame
app.bind('<Configure>', center_frame)

# Initial buttons
encryption_button = ctk.CTkButton(frame, text="Encryption", command=show_encryption_buttons)
decryption_button = ctk.CTkButton(frame, text="Decryption", command=show_decryption_buttons)
encryption_button.pack(pady=20)
decryption_button.pack(pady=20)

# Encryption buttons
load_button = ctk.CTkButton(frame, text="Load Image", command=load_image)
encrypt_button = ctk.CTkButton(frame, text="Encrypt", command=handle_encrypt)
save_encrypted_button = ctk.CTkButton(frame, text="Save Image", command=save_encrypted_image)
go_back_button_encryption = ctk.CTkButton(frame, text="Go Back", command=go_back_encryption)

# Decryption buttons
load_encrypted_button = ctk.CTkButton(frame, text="Load Encrypted Image", command=load_encrypted_image)
decrypt_button = ctk.CTkButton(frame, text="Decrypt", command=handle_decrypt)
save_decrypted_button = ctk.CTkButton(frame, text="Save Image", command=save_decrypted_image)
go_back_button_decryption = ctk.CTkButton(frame, text="Go Back", command=go_back_decryption)

# Image label
img_label = ctk.CTkLabel(frame, text="")
img_label.pack(pady=20)

# Run the app
app.mainloop()
