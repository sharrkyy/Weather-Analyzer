import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Weather.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Day"] = df["Date"].dt.strftime("%B %d, %Y")

print("Welcome to the Weather Analyzer!")

while True:
    print("\nChoose an option: ")
    print("1. Display summary statistics")
    print("2. Plot Temperature")
    print("3. Plot Humidity")
    print("4. Display Humidity vs AQI (Scatter Plot)")
    print("5. Show Rainfall Probability (Pie Chart)")
    print("6. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        print(df.drop(columns=["Date", "Day"]).describe())

        print("\n--- Key Highlights ---")

    # Storing in a dictionary
        highlights = {
            "Max Temperature": [df["Temperature (°C)"].max(),
                                pd.to_datetime(df[df["Temperature (°C)"] == df["Temperature (°C)"].max()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Min Temperature": [df["Temperature (°C)"].min(),
                                pd.to_datetime(df[df["Temperature (°C)"] == df["Temperature (°C)"].min()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Max AQI": [df["AQI"].max(),
                        pd.to_datetime(df[df["AQI"] == df["AQI"].max()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Min AQI": [df["AQI"].min(),
                        pd.to_datetime(df[df["AQI"] == df["AQI"].min()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Max Humidity": [df["Humidity (%)"].max(),
                            pd.to_datetime(df[df["Humidity (%)"] == df["Humidity (%)"].max()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Min Humidity": [df["Humidity (%)"].min(),
                            pd.to_datetime(df[df["Humidity (%)"] == df["Humidity (%)"].min()]["Date"].values[0]).strftime("%B %d, %Y")],

            "Max Rainfall Probability": [df["Rainfall Probability (%)"].max(),
                                        pd.to_datetime(df[df["Rainfall Probability (%)"] == df["Rainfall Probability (%)"].max()]["Date"].values[0]).strftime("%B %d, %Y")],
                                        
            "Min Rainfall Probability": [df["Rainfall Probability (%)"].min(),
                                        pd.to_datetime(df[df["Rainfall Probability (%)"] == df["Rainfall Probability (%)"].min()]["Date"].values[0]).strftime("%B %d, %Y")]
        }

        summary_df = pd.DataFrame(highlights, index=["Value", "Date"]).T
        print(summary_df)

    # For Temperature plotting
    elif choice == 2:
        plt.plot(df["Day"], df["Temperature (°C)"], marker="o", 
                                                    color="#2A3663")
            
        plt.title("Temperature Trend")

        plt.xlabel("Date")

        plt.ylabel("Temperature (°C)")

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # For Humidity plotting
    elif choice == 3:
        plt.bar(df["Day"], df["Humidity (%)"], 
                                color="#703B3B")
            
        plt.title("Humidity Trend")

        plt.xlabel("Date")

        plt.ylabel("Humidity (%)")

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # For Humidity vs AQI scatter plotting
    elif choice == 4:
        plt.scatter(df["Humidity (%)"], df["AQI"], 
                        color="#4B352A", 
                        alpha=0.7,
                        s=111, 
                        label="Humidity vs AQI")
            
        plt.xlabel("Humidity (%)", color="blue")

        plt.ylabel("AQI", color="green")

        plt.title("Humidity vs AQI")

        plt.legend()
        plt.tight_layout()
        plt.show()

    # For Rainfall Probability pie chart
    elif choice == 5:
        plt.pie(df["Rainfall Probability (%)"], 
                    labels=df["Day"],
                    autopct="%1.1f%%",
                    shadow=True)
            
        plt.title("Rainfall Probability")

        plt.tight_layout()
        plt.show()

    elif choice == 6:
        print("Bye Bye Brotha")
        break

    else:
        print("Invalid decision, check again")

    # Replay or Quit inside Loop
    print("\n1) Again")
    print("2) Exit")

    choice = int(input("Enter choice: "))
    if choice == 2:
        print("Thank you boiii")
        break 