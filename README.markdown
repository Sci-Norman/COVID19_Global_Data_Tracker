# COVID-19 Global Data Tracker Project
![image](covid.png)

## Overview
The **COVID-19 Global Data Tracker** is a Python-based GUI application designed to fetch and display real-time global COVID-19 statistics using the [disease.sh API](https://disease.sh/). The application is built using **Tkinter** for the graphical interface and is implemented in a **Jupyter Notebook** as part of a student assignment. It retrieves and displays metrics such as total cases, total deaths, today's cases, today's deaths, and today's recoveries, with a timestamp for the last update.

This project is intended for educational purposes, helping students learn to:
- Work with APIs to fetch real-time data.
- Use Tkinter to create a simple GUI.
- Handle JSON data and datetime formatting.
- Structure a data-driven application in a Jupyter Notebook.

## Features
- Fetches global COVID-19 data from the disease.sh API.
- Displays key metrics: total cases, total deaths, today's cases, today's deaths, and today's recoveries.
- Shows the timestamp of the last data update.
- Provides a simple Tkinter-based GUI with a light blue background.
- Includes a Jupyter Notebook with tasks for students to complete (e.g., fetching data, updating the GUI, adding a refresh button).

## Dataset
The project uses the [disease.sh COVID-19 API](https://disease.sh/v3/covid-19/all), which provides global COVID-19 statistics in JSON format. The API includes:
- `cases`: Total confirmed cases worldwide.
- `deaths`: Total deaths worldwide.
- `todayCases`: New cases reported today.
- `todayDeaths`: New deaths reported today.
- `todayRecovered`: New recoveries reported today.
- `updated`: Timestamp of the last update (in milliseconds since epoch).

## Requirements
To run this project, you need:
- **Python 3.6 or higher**
- **Jupyter Notebook** or **JupyterLab**
- Required Python libraries:
  - `tkinter` (included with standard Python installation)
  - `requests` (for API calls)
  - `datetime` (included with Python)

You can install the required library using pip:
```bash
pip install requests
```

## Project Structure
- `COVID19_Global_Data_Tracker.py'
- `README.md`: This file, providing project documentation.
- Generated files (optional):
  - Screenshots or images of the GUI (e.g., `tracker_screenshot.png`)

## Setup Instructions
1. **Clone or Download the Project**:
   - Download the repository or clone it using:
     ```bash
     git clone <repository-url>
     ```
2. **Install Dependencies**:
   - Ensure Python 3.6+ is installed.
   - Install the `requests` library:
     ```bash
     pip install requests
     ```
3. **Open the Jupyter Notebook**:
   - Navigate to the project directory:
     ```bash
     cd <project-directory>
     ```
   - Launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Open `COVID19_Global_Data_Tracker_Notebook.ipynb` in the Jupyter interface.
4. **Run the Notebook**:
   - Execute the cells in the notebook sequentially.
   - Complete the tasks marked with `# YOUR CODE HERE` (e.g., fetching API data, updating the Tkinter GUI).
   - Ensure an active internet connection to fetch data from the disease.sh API.

## Running the Application
- The notebook includes code to create a Tkinter window displaying COVID-19 statistics.
- Run the cell containing the Tkinter code to launch the GUI.
- The window will show:
  - Total cases, deaths, today's cases, deaths, and recoveries.
  - The timestamp of the last data update.
- To close the GUI, click the window's close button or stop the notebook cell execution.
- Optional: Complete advanced tasks (e.g., adding a refresh button) as outlined in the notebook.

## Example Output
The Tkinter GUI will look like this (example):
```
Total Cases: 700,000,000
Total Deaths: 7,000,000
Today Cases: 50,000
Today Deaths: 500
Today Recovered: 40,000
```
*(Note: Actual numbers depend on the API data at runtime.)*

## Assignment Tasks
The Jupyter Notebook includes the following tasks for students:
1. **Fetch Data**: Write code to retrieve JSON data from the disease.sh API.
2. **Process Data**: Extract and format metrics (e.g., cases, deaths, timestamp).
3. **Create GUI**: Use Tkinter to display the data in a window.
4. **Reflection**: Answer questions about the data and challenges faced.
5. **Optional Challenge**: Add a refresh button to update the data dynamically.

## Troubleshooting
- **API Errors**: If the API request fails, check your internet connection or verify the API URL (https://disease.sh/v3/covid-19/all). The disease.sh API is generally reliable but may occasionally be down.
- **Tkinter Issues**: Ensure Tkinter is installed (it’s included with standard Python). On some systems (e.g., Linux), you may need to install `python3-tk`:
  ```bash
  sudo apt-get install python3-tk
  ```
- **Notebook Display**: If the Tkinter window doesn’t appear in Jupyter, try running the code in a standalone Python script or use a different Jupyter backend (e.g., `%matplotlib tk`).

## Limitations
- The project uses global data only; it does not display country-specific statistics.
- The Tkinter GUI is basic and could be enhanced with additional features (e.g., styling, interactivity).
- The disease.sh API may have rate limits or occasional downtime, though this is rare.
- Tkinter in Jupyter Notebooks may behave differently depending on the environment (e.g., Windows, macOS, Linux).

## Future Enhancements
- Add support for country-specific data using other disease.sh endpoints (e.g., https://disease.sh/v3/covid-19/countries).
- Improve the GUI with better styling (e.g., fonts, colors, layout).
- Include a dropdown menu to select different data metrics or regions.
- Save data to a local CSV file for offline analysis.

## Acknowledgments
- **disease.sh**: For providing an open-source COVID-19 API.
- **Johns Hopkins University**: For inspiring COVID-19 tracking projects with their dataset.
- **Tkinter**: For enabling simple GUI development in Python.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (if included).

## Contact
For questions or issues, please contact the project maintainer or submit an issue on the repository (if hosted on GitHub).

---
*Last updated: May 13, 2025*