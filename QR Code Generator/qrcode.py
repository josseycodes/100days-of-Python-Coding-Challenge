import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    user_data = input("Enter the text or data for QR code generation: ")
    file_name = input("Enter the name of the QR code file (with extension, e.g., example.png): ")
    
    generate_qr_code(user_data, file_name)
    print(f"QR code generated and saved as {file_name}")
