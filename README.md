# Survey App - Using Flask

The Survey App is a simple web application built with Flask that allows users to participate in surveys and record their responses. It includes features like presenting one question at a time, ensuring users answer each question before proceeding, and displaying the survey results at the end.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Presentation of surveys one question at a time.
- Users must answer each question before proceeding to the next one.
- Supports multiple types of surveys.
- Stores user responses and displays the survey results at the end.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask (installed as a project dependency)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/samiesmilz/survey-app.git
   ```

2. Change into the project directory:

   ```bash
   cd survey-app
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application by running the following command:

   ```bash
   flask run
   ```

2. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to access the Survey App.

3. Follow the on-screen instructions to participate in a survey.

4. Answer each question and proceed to the next one.

5. At the end of the survey, the application will display a "Thank you for your valuable feedback" message.

## Contributing

Contributions are welcome! If you would like to improve this project or fix issues, please follow these steps:

1. Fork the repository.

2. Create a new branch with a descriptive name:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add your message here"
   ```

4. Push your branch to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a pull request in the original repository.

6. Your pull request will be reviewed, and once accepted, your changes will be merged.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
