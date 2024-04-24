from PIL import Image, ImageDraw, ImageFont


def write_certificate(name, venue, date, template_path, output_path):
    try:
        # Load the certificate template
        template = Image.open(template_path)

        # Prepare the drawing context
        draw = ImageDraw.Draw(template)

        # Specify the font type and font size
        font_path = 'arial.ttf'
        font_size_name = 40
        font_size_date_venue = 24

        # Load fonts
        font_name = ImageFont.truetype(font_path, font_size_name)
        font_date_venue = ImageFont.truetype(font_path, font_size_date_venue)

        # Coordinates and text to draw
        coordinates_name = (560, 500)
        coordinates_date = (1395, 651)
        coordinates_venue = (595, 690)

        # Drawing text on the image
        draw.text(coordinates_name, name, font=font_name, fill="black")
        draw.text(coordinates_date, date, font=font_date_venue, fill="black")
        draw.text(coordinates_venue, venue, font=font_date_venue, fill="black")

        # Save the modified image
        template.save(output_path)

        print("Certificate created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
template_path = 'static/template.jpg'
output_path = 'custom_certificate.jpg'
write_certificate('John Doe', 'Conference Center', 'April 24, 2024', template_path, output_path)
