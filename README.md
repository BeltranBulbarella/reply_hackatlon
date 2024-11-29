# Academic and Career Assistant - README

Welcome to the **Academic and Career Assistant**, an AI-powered tool designed to provide comprehensive information about university courses and offer personalized career guidance. This assistant utilizes OpenAI's language models to generate course summaries, assess complexity, create multiple-choice questions, and more, based on provided course data. It also helps users explore professional fields, find job or internship opportunities, and generate resumes based on their educational path and interests.

## Demo


https://github.com/user-attachments/assets/b3a7fb0f-8df7-4203-b989-8f6db002f585



https://github.com/user-attachments/assets/c804f0af-6ac8-4a7a-ae2e-c9357e76d9ed




## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Using the Application](#using-the-application)
    - [Academic Assistance](#academic-assistance)
    - [Career Guidance](#career-guidance)
- [Project Structure](#project-structure)
- [Customization](#customization)
  - [Adding or Modifying Courses](#adding-or-modifying-courses)
  - [Adding or Modifying Career Data](#adding-or-modifying-career-data)
  - [Changing the OpenAI Model](#changing-the-openai-model)
  - [Adjusting the Temperature](#adjusting-the-temperature)
- [Notes and Considerations](#notes-and-considerations)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

The **Academic and Career Assistant** is a Streamlit web application that interacts with OpenAI's GPT models to provide detailed information about university courses and personalized career guidance.

### Academic Assistance

By leveraging a simulated database of course data and student feedback, the assistant can:

- Generate concise course summaries.
- Assess the overall complexity of a course.
- Create challenging multiple-choice questions (MCQs) related to course topics.
- Provide information about the language in which the course is taught.
- Estimate the content distribution across different subjects (e.g., Mathematics, Physics, Computer Science).
- Indicate whether a course provides a polycopy (course booklet).

### Career Guidance

Based on the user's educational path, interests, and professional experience, the assistant can:

- Generate a list of suitable professional fields.
- Retrieve job or internship opportunities in those fields.
- Provide brief summaries of job roles.
- Retrieve LinkedIn profiles of alumni in similar roles.
- Provide salary information for the selected jobs.
- Generate sample resumes tailored to the user's background and chosen field.

---

## Features

- **User-Friendly Interface:** An interactive web app built with Streamlit.
- **AI-Powered Responses:** Utilizes OpenAI's GPT models for natural language processing.
- **Customizable Data:** Easily extend or modify the course and career databases.
- **Modular Architecture:** Clean separation of concerns with agents handling specific tasks.
- **Scalable Design:** Capable of adding more courses, career data, and features as needed.

---

## Prerequisites

- **Python 3.7 or higher**
- **OpenAI Python Library**
- **Streamlit Library**

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/academic-career-assistant.git
   cd academic-career-assistant
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
   cd academic-career-assistant
   ```

2. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

3. **Access the Application**

   After running the above command, Streamlit will provide a local URL (e.g., `http://localhost:8501`) where you can access the web application through your web browser.

### Using the Application

Upon accessing the application, you will have the option to select between **Academic Assistance** and **Career Guidance** from the sidebar.

#### Academic Assistance

1. **Select "Academic Assistance"** from the sidebar.

2. **Enter the Course Name**

   - In the text input field, enter the name of the course you're interested in. For example:

     ```
     Calcul Haute Performance
     ```

3. **Select the Desired Information**

   - Check the boxes for the information you want to retrieve:

     - Summary of the course
     - Overall level of complexity
     - Generate a multiple-choice question (MCQ)
     - Course language
     - Content distribution
     - Polycopy availability

4. **Submit the Request**

   - Click the **Submit** button to process your request.

5. **View the Results**

   - The assistant will display the requested information below the submit button, organized by headings.

#### Career Guidance

1. **Select "Career Guidance"** from the sidebar.

2. **Provide Your Information**

   - **Educational Path:** Describe your educational background.

     _Example: "Master's degree in Computer Science with a focus on machine learning."_

   - **Interests:** List your interests.

     _Example: "Data science, artificial intelligence, software development."_

   - **Professional Experience:** Describe your professional experience.

     _Example: "Internship at XYZ Corp as a software developer."_

3. **Generate Professional Fields**

   - Click the **"Generate Professional Fields"** button.

   - The assistant will generate a list of suitable professional fields based on your inputs.

4. **Select Job or Internship**

   - Choose whether you're searching for a **Job** or **Internship**.

5. **Find Opportunities**

   - Click the **"Find Opportunities"** button.

   - The assistant will retrieve job or internship opportunities, provide job summaries, LinkedIn profiles, salary information, and display the data in a table.

6. **Generate Resumes (Optional)**

   - If you wish to generate sample resumes, check the **"Generate Resumes"** checkbox.

   - Select the professional field you're interested in from the dropdown.

   - Click the **"Generate Resumes"** button to receive sample resumes tailored to your background and chosen field.

---

## Project Structure

```
academic-career-assistant/
├── app.py
├── agents/
│   ├── academic_agents.py
│   ├── career_agents.py
├── ui/
│   ├── academic_course_assistant.py
│   ├── career_guidance.py
├── utils/
│   ├── openai_utils.py
│   ├── simulated_db.py
├── requirements.txt
├── README.md
└── .env (optional)
```

- **app.py:** The main application script that runs the Streamlit app.
- **agents/:** Contains the agent scripts for academic assistance and career guidance.
- **ui/:** Contains the user interface components for each assistant.
- **utils/:** Contains utility scripts, including OpenAI API utilities and simulated databases.
- **requirements.txt:** Lists the Python dependencies.
- **README.md:** This readme file.
- **.env:** Optional file to store environment variables.

---

## Customization

### Adding or Modifying Courses

- **Updating `course_database`:**

  - In `utils/simulated_db.py`, locate the `course_database` variable.
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

### Adding or Modifying Career Data

- **Updating Simulated Databases:**

  - **Job Database (`job_database`):** Located in `utils/simulated_db.py`.

    ```python
    job_database = [
        {
            "company": "Company Name",
            "job_title": "Job Title",
            "professional_field": "Professional Field"
        },
        # Add more job listings here...
    ]
    ```

  - **Company Partnerships (`company_partnerships`):**

    ```python
    company_partnerships = [
        "Company A",
        "Company B",
        # Add more companies here...
    ]
    ```

  - **Alumni Profiles (`alumni_profiles`):**

    ```python
    alumni_profiles = [
        {
            "name": "Alumni Name",
            "job_title": "Job Title",
            "company": "Company Name",
            "linkedin_url": "https://linkedin.com/in/username",
            "electives": ["Elective 1", "Elective 2"]
        },
        # Add more profiles here...
    ]
    ```

  - **Salary Database (`salary_database`):**

    ```python
    salary_database = {
        "Job Title": {
            "average_salary": "$XX,XXX"
        },
        # Add more salary data here...
    }
    ```

### Changing the OpenAI Model

- **Modify the Model Used:**

  - In `utils/openai_utils.py`, you can change the `model` parameter in the `call_openai_api` function.

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

  - Ensure that any real student or professional data complies with privacy regulations.
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

**Disclaimer:** This application is intended for educational and demonstration purposes. The course data, student feedback, and career data are simulated and may not reflect actual courses, opinions, or job opportunities.

---

I've updated the README to include the new **Career Guidance** functionality, providing comprehensive instructions and information about the application's features, usage, and structure. If you have any further questions or need additional modifications, please let me know!
