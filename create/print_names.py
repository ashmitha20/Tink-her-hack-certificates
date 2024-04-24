import os


def list_venues_and_teams(cert_dir):
    venues = {}

    # Check each directory within the certificates directory
    for venue in os.listdir(cert_dir):
        venue_path = os.path.join(cert_dir, venue)

        # Ensure it's a directory (and not a file)
        if os.path.isdir(venue_path):
            venues[venue] = []

            # For each file in the venue directory
            for file in os.listdir(venue_path):
                # Ensure it's a file and ends with .zip
                if file.endswith('.zip'):
                    # Remove the .zip extension to get the team name
                    team_name = file[:-4]  # removes the last 4 characters '.zip'
                    venues[venue].append(team_name)

    return venues


# Define the root directory for storing certificates
cert_dir = 'certificates'

# Get the venue and team information
venues = list_venues_and_teams(cert_dir)

# Print the dictionary in the required format
print("venues = {")
for venue, teams in venues.items():
    print(f"    '{venue}': {teams},")
print("}")
