## Project Setup Instructions

## Tools and Languages Used

- **Language**: Python 3.6.0
- **Web Framework**: Flask
- **HTML Template Engine**: Jinja2
- **JavaScript Library**: Google Charts
- **Database**: SQLite3 (Python)

## Setup Steps (Windows)

### Install Required Packages

1. Open a Command Prompt as an administrator.
2. Navigate to the directory where your Python scripts are located (e.g., "C:\Program Files\Python36\Scripts").
3. Install the necessary Python packages using `pip`:
   - `pip install virtualenv`: This installs the Virtual Environment tool.
   - `pip install flask`: This installs the Flask web framework.
   - `pip install dropbox`: This installs the Dropbox SDK or package.
   - `pip install Flask-Session`: This installs the Flask-Session extension.

### Create a Project Folder

4. Create a folder for your web app, for example, "C:\WebApp".

### Create a Virtual Environment

5. Navigate to your project folder using the Command Prompt: `cd "C:\WebApp"`.
6. Create a virtual environment within your project folder, named "VE" in this case: `virtualenv VE`.

### Activate the Virtual Environment

7. Activate the virtual environment by running the appropriate activation script. In your case, navigate to the "Scripts" directory of your virtual environment: `cd "C:\WebApp\VE\Scripts"`.
8. Activate the virtual environment by running the `activate` script.

### Copy Project Files

9. Copy the contents of your "SpaceAnalyzer" code folder into your virtual environment. You mentioned: "Copy the SpaceAnalyzer (code folder) to VE" - do this by placing the project files in "C:\WebApp\VE\SpaceAnalyzer".

### Run the Server

10. Navigate to your project folder within the virtual environment: `cd "C:\WebApp\VE\SpaceAnalyzer"`.
11. Run the Flask application by executing the main script, which is "main.py" in this case: `python main.py`.

### Access the Web Application

12. Open a web browser and visit "http://localhost:5000" to access the web application.
13. You will need to log in using a valid access token.
