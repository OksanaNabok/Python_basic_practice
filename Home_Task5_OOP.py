import datetime

def write_news(city, text):
    today = datetime.datetime.now()
    date_str = today.strftime("%Y-%m-%d %H:%M")
    news_format = f"News -------------------------\nCity: {city}\nText: {text}\nDate: {date_str}\n\n"
    with open("newsfeed.txt", "a") as file:
        file.write(news_format)

def write_ad(expiration_date, text):
    today = datetime.datetime.now()
    expiration = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
    days_left = (expiration - today).days
    ad_format = f"Private Ad -------------------\nText: {text}\nExpiration Date: {expiration_date}\nDays left: {days_left} days\n\n"
    with open("newsfeed.txt", "a") as file:
        file.write(ad_format)

def write_weather(city, temperature):
    today = datetime.datetime.now()
    date_str = today.strftime("%Y-%m-%d %H:%M")
    weather_format = f"Weather Update ----------------\nCity: {city}\nTemperature: {temperature}C\nDate: {date_str}\n\n"
    with open("newsfeed.txt", "a") as file:
        file.write(weather_format)

def main():
    while True:
        print("Select the type of data you want to add:")
        print("1: News")
        print("2: Private Ad")
        print("3: Weather Update")
        print("4: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city: ")
            text = input("Enter news text: ")
            write_news(city, text)
        elif choice == "2":
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            text = input("Enter ad text: ")
            write_ad(expiration_date, text)
        elif choice == "3":
            city = input("Enter city: ")
            temperature = input("Enter temperature (Celsius): ")
            write_weather(city, temperature)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()