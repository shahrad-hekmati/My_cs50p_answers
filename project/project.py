import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

def fetch_astronaut_data(url):
    try:
        response = urllib.request.urlopen(url, timeout=30)
        result = json.loads(response.read())
        return result["people"]
    except Exception as e:
        print("Error fetching astronaut data:", e)
        return []

def write_astronaut_data_to_file(data, filename):
    try:
        with open(filename, "w") as file:
            file.write("There are currently " + str(len(data)) + " astronauts on the ISS: \n\n")
            for person in data:
                file.write(person['name'] + " - on board" + "\n")
    except Exception as e:
        print("Error writing astronaut data to file:", e)

def get_current_coordinates():
    try:
        g = geocoder.ip('me')
        return g.latlng
    except Exception as e:
        print("Error fetching current coordinates:", e)
        return None

def retry_on_timeout(max_retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except TimeoutError:
                    print("Connection timed out. Retrying...")
                    retries += 1
                    time.sleep(5)  # Wait for a few seconds before retrying
            print("Max retries reached. Unable to establish a connection.")
            return None
        return wrapper
    return decorator

@retry_on_timeout(max_retries=3)
def get_iss_position(url):
    try:
        response = urllib.request.urlopen(url, timeout=30)
        result = json.loads(response.read())
        location = result["iss_position"]
        return float(location['latitude']), float(location['longitude'])
    except Exception as e:
        print("Error fetching ISS position:", e)
        raise TimeoutError("Unable to get ISS position")

def main():
    url_iss = "http://api.open-notify.org/iss-now.json"
    url_astronauts = "http://api.open-notify.org/astros.json"

    astronaut_data = fetch_astronaut_data(url_astronauts)
    write_astronaut_data_to_file(astronaut_data, "iss.txt")

    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")

    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.setheading(45)
    iss.penup()

    while True:
        coordinates = get_current_coordinates()
        if coordinates:
            lat, lon = coordinates
            update_iss_position(iss, lat, lon)
            print("\nLatitude: " + str(lat))
            print("Longitude: " + str(lon))
        time.sleep(5)

if __name__ == "__main__":
    main()
