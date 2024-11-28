import openai

from utils.openai_utils import call_openai_api
from utils.simulated_db import course_database

# Function to get course data
def get_course_data(course_name):
    return course_database.get(course_name, None)

# Agents Implementation
def summary_agent(course_name, database):
    """Generate a course summary using OpenAI API."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    # Prepare the prompt
    prompt = f"""
    Given the following course data for '{course_name}':

    Nofist Data:
    {course_data['nofist_data']}
    
    Student Feedback:
    {course_data['student_feedback']}
    
    Generate a concise and informative summary of the course '{course_name}', highlighting the main topics, structure, and any important details.
    """
    # Call OpenAI API
    summary = call_openai_api(prompt)
    return summary if summary else "An error occurred while generating the summary."


def complexity_agent(course_name, database):
    """Assess course complexity using OpenAI API."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    # Prepare the prompt
    prompt = f"""
    Based on the following student feedback for the course '{course_name}':
    
    {course_data['student_feedback']}
    
    Rate the overall difficulty of the course on a scale of 1 to 10 (1 being very easy, 10 being extremely difficult). Provide a brief explanation for your rating, considering the course content, workload, and exam difficulty.
    """
    # Call OpenAI API
    complexity = call_openai_api(prompt)
    return complexity if complexity else "An error occurred while assessing complexity."


def mcq_agent(course_name, database):
    """Generate a multiple-choice question using OpenAI API."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    # Prepare the prompt
    prompt = f"""
    Using the following course information for '{course_name}':
    
    Nofist Data:
    {course_data['nofist_data']}
    
    Generate a challenging multiple-choice question related to the key topics of the course. Provide four options labeled A, B, C, and D, and indicate the correct answer with an explanation.
    """
    # Call OpenAI API
    mcq = call_openai_api(prompt, temperature=0.7)
    return mcq if mcq else "An error occurred while generating MCQ."


def language_agent(course_name, database):
    """Fetch course language."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    return f"The primary language of the course '{course_name}' is {course_data.get('language', 'not specified')}."


def content_distribution_agent(course_name, database):
    """Estimate content distribution using OpenAI API."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    # Prepare the prompt
    prompt = f"""
    Based on the following course data and student feedback for '{course_name}':
    
    Nofist Data:
    {course_data['nofist_data']}
    
    Student Feedback:
    {course_data['student_feedback']}
    
    Estimate the percentage distribution of content across Mathematics, Physics, Computer Science, Chemistry and Engineering Science in the course. Present the results in a clear format like:
    - Mathematics: x%
    - Physics: y%
    - Computer Science: z%
    - Chemistry: w%
    - Engineering Science: v%
    """
    # Call OpenAI API
    distribution = call_openai_api(prompt)
    return distribution if distribution else "An error occurred while analyzing content distribution."


def polycopy_agent(course_name, database):
    """Determine polycopy availability."""
    course_data = database.get(course_name)
    if not course_data:
        return "Course not found in the database."

    # Check 'nofist_data' for entries indicating a polycopy
    has_polycopy = any('Poly' in entry.get('Resource', '') for entry in course_data['nofist_data'])

    if has_polycopy:
        return f"Yes, the course '{course_name}' provides a polycopy."
    else:
        return f"No, the course '{course_name}' does not provide a polycopy."
