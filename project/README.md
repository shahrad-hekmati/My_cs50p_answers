# International Space Station (ISS) Tracker
#### Video Demo:  <https://youtu.be/KFUMexOjGas>
#### Description:

This Python script provides real-time tracking information about the International Space Station (ISS) and the astronauts currently on board. It retrieves data from the Open Notify API to obtain details about astronauts and the ISS's location.

## Features

- Fetches and displays the names of astronauts currently on the ISS.
- Retrieves the ISS's real-time position in terms of latitude and longitude.
- Maps the ISS's location on a world map.
- Stores astronaut data in a text file for reference.
- Displays your current location's latitude and longitude.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using `pip install geocoder turtle`.

## Usage

1. Run the Python script.

```bash
python iss_tracker.py
```

2. The script will display real-time information about the astronauts on the ISS and their current location. It will also update the ISS's position on a world map.

3. The data about astronauts is saved in a file named `iss.txt` for reference.

## Dependencies

- `geocoder` - Used to fetch your current location's coordinates.
- `turtle` - Used to display the world map and ISS position.
- `urllib.request` - Used to make HTTP requests to retrieve data from the Open Notify API.
- `json` - Used for JSON data parsing.
- `time` - Used for timing and delays.
- `webbrowser` - Used to open the astronaut data file.

## Notes

- The script handles timeouts and connection errors gracefully, with a retry mechanism.

Please note that this script relies on external APIs and services for real-time data. Ensure that your system has internet access to fetch the required data.

**Disclaimer:** This script is for educational purposes and relies on external services. It may be subject to changes or disruptions due to API updates.