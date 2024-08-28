---

# Professor & Course Rating Platform

## Overview

Welcome to the Professor & Course Rating Platform! This web application allows students to rate their professors and courses, providing valuable insights to new students who are selecting their classes. By sharing your experiences, you can help others make informed decisions about which courses to take and which professors to learn from.

## Features

- **Rate Professors**: Provide ratings and reviews for professors based on their teaching style, clarity, availability, and overall effectiveness.
- **Rate Courses**: Evaluate courses based on their difficulty, workload, content relevance, and overall value.
- **Search & Filter**: Easily search for specific professors or courses and filter results based on ratings, departments, and more.
- **User Profiles**: Create a profile to manage your ratings and track the courses you've taken.
- **Community Feedback**: View aggregate ratings and read detailed reviews from other students to help guide your course selection.

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL (for database)
- Docker (optional, for containerized deployment)

### Steps to Run Locally

1. **Clone the Repository**

   ```bash
   git clone https://github.com/oseni99/RateMyTC
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements/base.txt
   ```

4. **Set Up the Database**

   - Ensure PostgreSQL is running and create a database for the project.
   - Update the `.env` file with your database credentials.

5. **Run Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and go to `http://localhost:8000` to start using the platform.

### Docker Setup

1. **Build and Run the Docker Containers**

   ```bash
   docker-compose up --build
   ```

2. **Access the Application**

   Go to `http://localhost:8000` to use the platform.

## Usage

- **Sign Up**: Create an account to start rating and reviewing.
- **Rate Professors/Courses**: Provide your ratings and write reviews for the professors and courses you've taken.
- **Explore**: Browse ratings and reviews to help choose your future courses and professors.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to contribute to the project.

## License

This project is licensed under the MIT License. 

---

### Summary:

This README provides a quick overview of the project, installation instructions, usage guide, and contribution information. It should be enough to get new users and developers started with the platform.
