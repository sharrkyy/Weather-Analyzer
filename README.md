# Weather Analyzer

## 🔀 Version Comparison

### 🟢 Version 1
- 🔁 Controlled by a single **while True loop**.
- 📑 Menu choices handled with **if/elif statements** (1, 2, 3, etc.).
- 📊 Summary and visualization logic triggered directly inside the loop.
- 🖥️ All functionality lived together in one place.

### 🔵 Version 2
- 🔄 Menu replay uses **recursion** (no loops).
- 📑 Menu choices handled with **dictionary dispatch** (no long if/elif chains).
- 🧩 Modular design: separate classes for Summary, Temperature, Humidity, Scatter, Rainfall.
- 📝 Summary values extracted directly from the dataframe (manual filtering).
- 😎 Casual error and exit messages add personality.
