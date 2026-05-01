from Weather import Weather, Menu

if __name__ == "__main__":
    weather_instance = Weather()
    app = Menu(weather_instance.data())
    app.show_menu()
