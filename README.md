# Test Automation Project

This project is designed for test automation using Selenium. It tests a specially created training website.

## Project Structure


- `Configurations/`: Directory containing configuration files.
  - `config.ini`: Configuration file.
  - `readProperty.py`: Script for reading properties from the configuration file.
  - `TestData.py`: Test data.
- `Logs/`: Directory for logs.
- `Pages/`: Directory containing classes for interacting with elements on pages.
  - `BasePage.py`: Base page class.
  - `HomePage.py`: Home page class.
  - `LoginPage.py`: Login page class.
  - `MenPage.py`: Men's section page class.
- `Reports/`: Directory for reports.
- `Screenshots/`: Directory for screenshots.
  - `testLoginPage.png`: Example screenshot of the login page.
- `Tests/`: Directory containing test scenarios.
  - `conftest.py`: pytest configuration file with a fixture to initialize the browser.
  - `test_end2end.py`: End-to-end test script.
  - `test_home.py`: Home page test script.
  - `test_login.py`: Login page test script.
  - `test_login_2.py`: Alternative login page test script.
- `Utilities/`: Directory for utility scripts.
  - `LoggerInfo.py`: Logging utility.
- `LICENSE`: License file
- `requirements.txt`: Project dependencies.
- `README.md`: README file.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   
2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

## Usage

1. Run the tests:
   ```bash
   pytest

2. Testing
To run all tests, use the command:
   ```bash
   pytest
3. You can run a specific test by specifying the path to the test file:
   ```bash
   pytest path/to/test_file.py


## Authors

kh1tko

## License

This project is licensed under the MIT License.