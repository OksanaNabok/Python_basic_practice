import datetime
import os


class NewsFeedManager:
    def __init__(self, file_path=None):
        self.file_path = file_path or "input.txt"

    def process_file(self):
        if not os.path.exists(self.file_path):
            print(f"No file found at {self.file_path}")
            return

        with open(self.file_path, 'r') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(';')
            if len(data) == 3:
                if data[0] == "news":
                    city, text = data[1], data[2]
                    self.write_news(city, text)
                elif data[0] == "ad":
                    expiration_date, text = data[1], data[2]
                    self.write_ad(expiration_date, text)
                elif data[0] == "weather":
                    city, temperature = data[1], data[2]
                    self.write_weather(city, temperature)

        os.remove(self.file_path)
        print(f"Processed and removed file: {self.file_path}")

    def write_news(self, city, text):
        today = datetime.datetime.now()
        date_str = today.strftime("%Y-%m-%d %H:%M")
        news_format = f"News -------------------------\nCity: {city}\nText: {text}\nDate: {date_str}\n\n"
        with open("newsfeed.txt", "a") as file:
            file.write(news_format)

    def write_ad(self, expiration_date, text):
        today = datetime.datetime.now()
        expiration = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")
        days_left = max((expiration - today).days, 0)
        ad_format = f"Private Ad -------------------\nText: {text}\nExpiration Date: {expiration_date}\nDays left: {days_left} days\n\n"
        with open("newsfeed.txt", "a") as file:
            file.write(ad_format)

    def write_weather(self, city, temperature):
        today = datetime.datetime.now()
        date_str = today.strftime("%Y-%m-%d %H:%M")
        weather_format = f"Weather Update ----------------\nCity: {city}\nTemperature: {temperature}C\nDate: {date_str}\n\n"
        with open("newsfeed.txt", "a") as file:
            file.write(weather_format)


def main():
    choice = input("Would you like to process a specific file? (y/n) ")
    if choice.lower() == 'y':
        file_path = input("Enter the file path: ")
        manager = NewsFeedManager(file_path)
    else:
        manager = NewsFeedManager()

    manager.process_file()


if __name__ == "__main__":
    main()