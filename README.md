# Football Data Scraper

A Python script that scrapes and processes football match data from [Understat](https://understat.com/), specifically focusing on shot data for a given game ID.

Inspired by [McKay Johns](https://www.youtube.com/watch?v=IsR5FrjNmro)

## Features

- Fetches shot data from Understat using a game ID.
- Extracts JSON data embedded in the webpage's scripts.
- Processes and organizes the data into a Pandas DataFrame.

## Setup

### Using Dev Container

This project is configured to use a Dev Container for a consistent development environment. To use the Dev Container:

1. **Install Docker**:
   - Ensure you have [Docker](https://www.docker.com/get-started) installed and running on your machine.

2. **Install Visual Studio Code**:
   - Install [Visual Studio Code](https://code.visualstudio.com/).
   - Install the **Remote - Containers** extension from the Visual Studio Code marketplace.

3. **Open the Project in the Dev Container**:
   - Open the project folder in Visual Studio Code.
   - You should see a prompt offering to reopen the project in a Dev Container. If not, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette and search for "Remote-Containers: Reopen in Container".
   - VS Code will build the container and set up the development environment as defined in the `.devcontainer` configuration.

4. **Develop in the Container**:
   - Once the Dev Container is ready, you can run and debug the script as if you were in your local environment, but with the dependencies and environment isolated within the container.

### Manual Setup (Without Dev Container)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/microwavetoasteroven/understat_scraper.git
   cd understat_scraper

2. **Create and Activate a Virtual Environment**:
    It's recommended to use a virtual environment to manage dependencies. 
    Run the following commands to create and activate a venv:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Run the Script**:
    ```bash
    python src/main.py