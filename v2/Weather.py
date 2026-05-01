import pandas as pd
import matplotlib.pyplot as plt

# Reads the csv file
class Weather:
    def __init__(self):
        self.df = pd.read_csv("weather.csv", sep=None, engine='python')
        self.df.columns = self.df.columns.str.strip()
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df["Day"] = self.df["Date"].dt.strftime("%B %d, %Y")

    def data(self):
        return self.df

# Shows a brief summary of the csv file
class Summary:
    def __init__(self, df):
        self.df = df

    def show_summary(self):
        print("\n--- Key Highlights ---")

        # For the Maximum Temperature
        max_temp = self.df["Temperature (°C)"].max()
        max_temp_day = self.df[self.df["Temperature (°C)"] == max_temp]["Day"].values[0]

        # For the Minimum Temperature
        min_temp = self.df["Temperature (°C)"].min()
        min_day = self.df[self.df["Temperature (°C)"] == min_temp]["Day"].values[0]

        # For the Worst AQI
        max_aqi = self.df["AQI"].max()
        max_aqi_day = self.df[self.df["AQI"] == max_aqi]["Day"].values[0]

        # For the Maximum Humidity
        max_humid = self.df["Humidity (%)"].max()
        max_humid_day = self.df[self.df["Humidity (%)"] == max_humid]["Day"].values[0]

        # For the maximum rainfall probability
        max_rain = self.df["Rainfall Probability (%)"].max()
        max_rain_day = self.df[self.df["Rainfall Probability (%)"] == max_rain]["Day"].values[0]

        # Prints the temp, aqi, humid, rainfall
        print(f"Max Temp: {max_temp}°C on {max_temp_day}")
        print(f"Min Temp: {min_temp}°C on {min_day}")
        print(f"Worst AQI: {max_aqi} on {max_aqi_day}")
        print(f"Highest Humidity: {max_humid}% on {max_humid_day}")
        print(f"Highest Rainfall Probability: {max_rain}% on {max_rain_day}")


# Plotting for temperature
class Temperature:
    def __init__(self, df):
        plt.plot(df["Day"], df["Temperature (°C)"], marker="o",
                                                        color="#2A3663")

        plt.title("Temperature Trend")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

# bar for humidity
class Humidity:
    def __init__(self, df):
        plt.bar(df["Day"], df["Humidity (%)"], color="#703B3B")

        plt.title("Humidity Trend")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

# Scatter for humid vs aqi
class Scatter:
    def __init__(self, df):
        plt.scatter(df["Humidity (%)"], df["AQI"], color="#4B352A",
                                                            s=111,
                                                        alpha=0.7)

        plt.title("Humidity vs AQI")
        plt.show()

# Pie chart for rainfall :)
class Rainfall:
    def __init__(self, df):
        plt.pie(df["Rainfall Probability (%)"], labels=df["Day"], autopct="%1.1f%%",
                                                                        shadow=True)

        plt.title("Rainfall Probability")
        plt.show()

# Shows the menu for user choice
class Menu:
    def __init__(self, df):
        self.df = df
        self.summary = Summary(df)

    def show_menu(self):
        print("\nThe Weather Menu:")

        # THe menu bar
        print("1. Display Summary statistics\n",
              "2. Plot temperature\n",
              "3. Plot Humidity\n",
              "4. Display Humidity vs AQI (Scatter Plot)\n",
              "5. Show Rainfall Probability (Pie Chart)\n",
              "6. Exit")

        try:
            choice = int(input("Choose a number: "))
        except ValueError:
            print("Oops, that’s not possible. Try again, dude.")
            return self.show_menu()

        actions = {
            1: self.run_summary,
            2: self.run_temperature,
            3: self.run_humidity,
            4: self.run_scatter,
            5: self.run_rainfall,
            6: self.exit_program
        }

        if choice in actions:
            actions[choice]()
        else:
            print("Not an option, bro.")

        if choice != 6:
            return self.show_menu()

    def run_summary(self):
        self.summary.show_summary()

    def run_temperature(self):
        Temperature(self.df)

    def run_humidity(self):
        Humidity(self.df)

    def run_scatter(self):
        Scatter(self.df)

    def run_rainfall(self):
        Rainfall(self.df)

    def exit_program(self):
        print("Bye bye Brotha! :)")
