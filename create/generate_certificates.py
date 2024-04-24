import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import zipfile
import os

# Load data from CSV, ensure there's no header and delimiter is correctly set
data = pd.read_csv('data/teams.csv', header=None, delimiter=',')

# Define the root directory for storing certificates
cert_dir = 'certificates'

# Define the path to the certificate template
template_path = 'static/template.jpg'

# Font settings
font_path = 'arial.ttf'
font_size_name = 40
font_size_date_venue = 24

# Load fonts
font_name = ImageFont.truetype(font_path, font_size_name)
font_date_venue = ImageFont.truetype(font_path, font_size_date_venue)

# Loop through each team in the DataFrame
for index, row in data.iterrows():
    serial_number = str(row[0]).strip()
    team_name = row[3].strip().replace(' ', '_').replace('\r', '').replace('\n', '')
    venue = row[1].strip().replace(' ', '_').replace('\r', '').replace('\n', '')
    date = row[2].strip().replace('\r', '').replace('\n', '')
    members = row[5:].dropna()  # Take non-NaN member names

    # Ensure the venue directory exists within the certificates directory
    venue_dir = os.path.join(cert_dir, venue)  # Spaces already replaced with underscores
    if not os.path.exists(venue_dir):
        os.makedirs(venue_dir)

    # Load the template image
    template = Image.open(template_path)

    # Zip file for each team, placed inside the venue directory
    zip_name = f"{venue_dir}/{team_name}.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for member in members:
            member_clean = member.strip().replace('\r', '').replace('\n', '')
            # Modify the image for each member
            cert_copy = template.copy()
            draw = ImageDraw.Draw(cert_copy)

            # Drawing text on the image
            draw.text((560, 500), member_clean, font=font_name, fill="black")
            draw.text((1395, 651), date, font=font_date_venue, fill="black")
            draw.text((595, 690), venue.replace('_', ' '), font=font_date_venue, fill="black")

            # Save the certificate
            cert_path = f"{venue_dir}/{serial_number}_{team_name}_{member_clean}.jpg"
            cert_copy.save(cert_path)
            zipf.write(cert_path, os.path.basename(cert_path))

            # Remove the individual certificate file after adding to zip
            os.remove(cert_path)

print("Certificates created and zipped successfully.")
