# Cipher Desktop GUI App

## Overview
Cipher Desktop App is a graphical user interface (GUI) application for performing encryption and decryption using various classical cryptographic algorithms. The application is built using **Python** with **CustomTkinter** for the interface.

## Features
- **Caesar Cipher**
  - Encrypt and decrypt text using the Caesar cipher.
  - Specify a shift key for encoding and decoding.
- **Playfair Cipher**
  - Encrypt and decrypt messages using the Playfair cipher.
  - Input a key to generate a Playfair matrix.
- **Monoalphabetic Substitution Cipher**
  - Encrypt and decrypt text using a predefined character substitution method.
- **CustomTkinter UI**
  - A modern graphical user interface with a sidebar for selecting encryption types and operations.
  - Beautiful color theme and smooth user interactions.
- **Error Handling**
  - Displays appropriate error messages for missing input, invalid characters, or incorrect keys.
  
## Installation
### Prerequisites
Ensure you have Python installed. You also need to install the required dependencies:
```sh
pip install customtkinter CTkMessagebox Pillow
```

### Running the Application
To start the application, run the following command:
```sh
python main.py
```

## Usage
1. Select a cipher from the dropdown menu:
   - **Caesar**
   - **Playfair**
   - **Monoalphabetic**
2. Choose an operation:
   - **Encrypt**
   - **Decrypt**
3. Enter the required input:
   - Plain text
   - Shift key (for Caesar Cipher)
   - Playfair key (for Playfair Cipher)
4. Click the **Do Operation** button to execute.
5. View the results in the pop-up message box.

## Author
Developed by **Ahmed Ramadan**.


