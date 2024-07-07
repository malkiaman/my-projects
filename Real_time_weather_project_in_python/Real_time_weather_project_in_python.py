import win32com.client as wincom  # Import the library for text-to-speech conversion
import requests                   # Import the requests library for weather API
import json                       # Import the JSON library to convert text to dictionary

speak = wincom.Dispatch('sapi.spvoice')  # Initialize the text-to-speech engine
def cl():
    print("press \"q\" to Exit")
    while True:
        loc = input('Enter your location: ')
        if loc=='q'or loc=='Q':
            print("Exited..!")
            speak.Speak("Exited...!")
            return
        url = f'https://api.weatherapi.com/v1/current.json?key=e084bcaef5a64b76ae962540240707&q={loc}'  # Weather API URL
        res = requests.get(url)  # Fetch weather API details
        # print(res)
        dic = json.loads(res.text)  # Convert API details to dictionary

        while True:
            query = input("What do you want? i.e., country name, region, temperature, condition, date & time: ")
            lower_query = query.lower()
            
            if lower_query == 'q':
                print("Exited...!")
                speak.Speak("Exited...!")
                return  # Exit the function and script if 'q' is pressed
            
            match lower_query:
                case 'country name':
                    cn = dic['location']['country']  # Fetch country value from API data
                    print(f'The country name of {loc} is {cn}')
                    speak.Speak(f'The country name of {loc} is {cn}')
                case 'region':
                    r = dic['location']['region']
                    print(f'The region of {loc} is {r}')
                    speak.Speak(f'The region of {loc} is {r}')
                case 'temperature':
                    temp = dic['current']['temp_c']
                    print(f'The current temperature of {loc} is {temp} degree Centigrade')
                    speak.Speak(f'The current temperature of {loc} is {temp} degree Centigrade')
                case 'condition':
                    con = dic['current']['condition']['text']
                    print(f'The current condition of {loc} is \"{con}\"')
                    speak.Speak(f'The current condition of {loc} is {con}')
                case 'date & time':
                    dt = dic['location']['localtime']
                    print(f'The current date and time in {loc} is {dt}')
                    speak.Speak(f'The current date and time in {loc} is {dt}')
                case _:
                    print("You have chosen the wrong option")
                    speak.Speak("You have chosen the wrong option")

            chng_loc = input("Do you want to change the location? Press y for \"YES\" and N for \"NO\": ")
            if chng_loc.lower() == 'y':
                break  # Break inner loop to change location

def main():
    cl()  # Call the cl function

if __name__ == "__main__":
  try:
    main()  # Run the main function if the script is executed directly
  except:
      print("You have Entered wrong Country Name")
      speak.Speak("You have Entered wrong Country Name")
