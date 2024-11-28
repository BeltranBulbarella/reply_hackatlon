# Academic Course Assistant - README

Welcome to the **Academic Course Assistant**, an AI-powered tool designed to provide comprehensive information about university courses. This assistant utilizes OpenAI's language models to generate course summaries, assess complexity, create multiple-choice questions, and more, based on provided course data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Using the Application](#using-the-application)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Notes and Considerations](#notes-and-considerations)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

The Academic Course Assistant is a Streamlit web application that interacts with OpenAI's GPT models to provide detailed information about university courses. By leveraging a simulated database of course data and student feedback, the assistant can:

- Generate concise course summaries.
- Assess the overall complexity of a course.
- Create challenging multiple-choice questions (MCQs) related to course topics.
- Provide information about the language in which the course is taught.
- Estimate the content distribution across different subjects (e.g., Mathematics, Physics, Computer Science).
- Indicate whether a course provides a polycopy (course booklet).

---

## Features

- **User-Friendly Interface:** An interactive web app built with Streamlit.
- **AI-Powered Responses:** Utilizes OpenAI's GPT models for natural language processing.
- **Customizable Data:** Easily extend or modify the course database.
- **Modular Architecture:** Clean separation of concerns with agents handling specific tasks.
- **Scalable Design:** Capable of adding more courses and features as needed.

---

## Prerequisites

- **Python 3.7 or higher**
- **OpenAI Python Library**
- **Streamlit Library**

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/academic-course-assistant.git
   cd academic-course-assistant
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, install the required libraries directly:

   ```bash
   pip install openai streamlit
   ```

4. **Set Your OpenAI API Key**

   Obtain your API key from the [OpenAI dashboard](https://platform.openai.com/account/api-keys) and set it as an environment variable.

   - **On Unix/Linux/macOS:**

     ```bash
     export OPENAI_API_KEY='your-api-key-here'
     ```

   - **On Windows (Command Prompt):**

     ```cmd
     set OPENAI_API_KEY=your-api-key-here
     ```

   - **On Windows (PowerShell):**

     ```powershell
     $env:OPENAI_API_KEY="your-api-key-here"
     ```

   Alternatively, you can create a `.env` file in the project root:

   ```bash
   echo OPENAI_API_KEY='your-api-key-here' > .env
   ```

   And modify the code to load the `.env` file:

   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

---

## Usage

### Running the Application

1. **Navigate to the Project Directory**

   ```bash
   cd academic-course-assistant
   ```

2. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

3. **Access the Application**

   After running the above command, Streamlit will provide a local URL (e.g., `http://localhost:8501`) where you can access the web application through your web browser.

### Using the Application

1. **Enter the Course Name**

   - In the text input field, enter the name of the course you're interested in. For example:

     ```
     Calcul Haute Performance
     ```

2. **Select the Desired Information**

   - Check the boxes for the information you want to retrieve:

     - Summary of the course
     - Overall level of complexity
     - Generate a multiple-choice question (MCQ)
     - Course language
     - Content distribution
     - Polycopy availability

3. **Submit the Request**

   - Click the **Submit** button to process your request.

4. **View the Results**

   - The assistant will display the requested information below the submit button, organized by headings.

---

## Project Structure

```
academic-course-assistant/
├── app.py
├── requirements.txt
├── README.md
└── .env (optional)
```

- **app.py:** The main application script containing all the code.
- **requirements.txt:** Lists the Python dependencies.
- **README.md:** This readme file.
- **.env:** Optional file to store environment variables.

---

## Customization

### Adding or Modifying Courses

- **Updating `course_database`:**

  - In `app.py`, locate the `course_database` variable.
  - Add new courses or modify existing ones using the provided structure.

    ```python
    course_database = {
        'Course Name': {
            'nofist_data': [ ... ],
            'student_feedback': [ ... ]
        },
        # Add more courses here...
    }
    ```

### Changing the OpenAI Model

- **Modify the Model Used:**

  - In the `call_openai_api` function, you can change the `model` parameter.

    ```python
    def call_openai_api(prompt, model="gpt-3.5-turbo", temperature=0):
        # ...
    ```

  - If you have access to GPT-4, you can set `model="gpt-4"`.

### Adjusting the Temperature

- **Control the Creativity of Responses:**

  - The `temperature` parameter controls the randomness of the output.

    - Higher values (e.g., `temperature=0.7`) produce more creative responses.
    - Lower values (e.g., `temperature=0`) produce more deterministic responses.

---

## Notes and Considerations

- **API Usage and Costs:**

  - Be aware of your OpenAI API usage limits and potential costs.
  - Monitor your API usage through the OpenAI dashboard.

- **Data Privacy:**

  - Ensure that any real student data complies with privacy regulations.
  - The provided data is simulated for demonstration purposes.

- **Error Handling:**

  - The application includes basic error handling.
  - You may enhance it by adding more detailed exception handling and user feedback.

- **Security:**

  - **Never** commit your API key or any sensitive information to version control.
  - Ensure your `.gitignore` file excludes the `.env` file if you use one.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- **OpenAI:** For providing the powerful language models used in this application.
- **Streamlit:** For offering an easy-to-use framework for building web applications.
- **Contributors:** Thanks to everyone who contributed to the development of this project.

---

**Disclaimer:** This application is intended for educational and demonstration purposes. The course data and student feedback are simulated and may not reflect actual courses or opinions.
