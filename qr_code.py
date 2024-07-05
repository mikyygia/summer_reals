import qrcode

website_link = input("Link: ")
qrcode_name = input("Title: ")

qr = qrcode.QRCode(version=1, box_size=10, border=10)
qr.add_data(website_link)

try:
    option = input("Customize fill and background color? (y/n): ")

    if (option.lower() == "y" or option.lower() == "n"):
        fill = input("Fill color: ")
        backg = input("Background color: ")

        img = qr.make_image(fill_color=fill, back_color=backg)

except ValueError:
    print("Okay.. let's just stick to the default")
    img = qr.make_image(fill_color='black', back_color='white')

print("Done!")
img.save(f"{qrcode_name}.png")
