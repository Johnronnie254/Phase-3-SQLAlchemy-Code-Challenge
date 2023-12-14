
# SQLAlchemy Code Challenge: Restaurants

This project is part of the SQLAlchemy Code Challenge for the Phase 3. It involves building a restaurant review domain with three models: `Restaurant`, `Review`, and `Customer`. The relationships between these models are established using SQLAlchemy.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Setup](#database-setup)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:
   git clone <repository_url>

   
Navigate to the project directory:
cd restaurant_sqalchemy


Create and activate a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Usage
Ensure your virtual environment is activated:
source venv/bin/activate


Run the test script:
python3 test.py
Check the console output for the results.

Project Structure
models.py: Contains the SQLAlchemy models for Restaurant, Customer, and Review.
test.py: Test script to demonstrate the functionality of the SQLAlchemy models.
venv/: Virtual environment directory (create this if using a virtual environment).
README.md: Project documentation.

Database Setup
The project uses an SQLite database. The database is created in memory for testing purposes. You can modify the database configuration in the models.py file if needed.

Testing
Ensure that the project is set up correctly and dependencies are installed. Run the test script:
python3 test.py
Contributing
If you have suggestions or find issues, please feel free to open an issue or create a pull request.
License
MIT License
