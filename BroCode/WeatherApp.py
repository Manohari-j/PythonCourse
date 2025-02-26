import sys  # System args
import requests  # API requests
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)  # label
        self.city_input = QLineEdit(self)  # text box
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)  # alt+0176
        self.emoji_label = QLabel(self)
        self.desc_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.get_weather_button.setObjectName("get_weather_button")
        self.desc_label.setObjectName("desc_label")

        self.setStyleSheet("""
            Qlabel,QPushButton{
                font-family: calibri;            
            }
            QLabel#city_label{
                font-size: 40px;
                font-style:Italic
            }
            QLineEdit#city_input{
                font-size:40px;
            }
            QPushButton#get_weather_button{
                font-size:30px;
                font-weight: bold;
            }
            QLabel#temp_label{
                font-size:75px;
            }
            QLabel#emoji_label{
                font-size:100px;
                font-family: Segoe UI emoji;
            }
            QLabel#desc_label{
                font-size:50px;
            }
        
        
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "" # get it from openweatherapi
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # raise an exception if there is any HTTP error
            data = response.json()
            # print(data)

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not Found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")


        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe requests timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self,message):
        self.temp_label.setStyleSheet("font-size:30px;")
        self.temp_label.setText(message)
        self.emoji_label.clear()
        self.desc_label.clear()

    def display_weather(self,data):
        self.temp_label.setStyleSheet("font-size:50px;")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        temp_f = (temp_k * 9/5) - 459.67

        self.temp_label.setText(f"{temp_c:.0f}°C")

        weather_desc = data["weather"][0]["description"]
        self.desc_label.setText(weather_desc)

        weather_id = data["weather"][0]["id"]
        weather_emoji = self.get_weather_emoji(weather_id)
        self.emoji_label.setText(weather_emoji)

    @staticmethod # not instance specific
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "⛅️"
        elif 500 <= weather_id <= 531:
            return "🌧️️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 700 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""




if __name__ == "__main__":
    app = QApplication(sys.argv)  # for cmd line arg
    weather = WeatherApp()
    weather.show()
    sys.exit(app.exec_())  # close the window
