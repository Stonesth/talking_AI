import requests

# Make a GET request to the website
response = requests.get('https://www.example.com/roland-garros/2024')

# Check if the request was successful
if response.status_code == 200:
    # Extract the winner from the response content
    winner = response.text

    # Print the winner
    print(f"The winner of Roland Garros 2024 is: {winner}")
else:
    print("Failed to retrieve the winner of Roland Garros 2024")