import streamlit as st
from agents.supervisor_agent import supervisor_agent
from utils.simulated_db import course_database

def main():
    st.title("Academic Course Assistant")

    # Input: Course Name
    course_name = st.text_input("Enter the course name (e.g., 'Calcul Haute Performance'):")

    # User options
    st.write("Select the information you would like to receive:")
    summary_option = st.checkbox("Summary of the course")
    complexity_option = st.checkbox("Overall level of complexity")
    mcq_option = st.checkbox("Generate a multiple-choice question (MCQ)")
    language_option = st.checkbox("Course language")
    content_distribution_option = st.checkbox("Content distribution (Mathematics, Physics, Computer Science)")
    polycopy_option = st.checkbox("Polycopy availability")

    # Submit button
    if st.button("Submit"):
        if course_name.strip() == "":
            st.error("Please enter a course name.")
        else:
            # Call the supervisor agent
            responses = supervisor_agent(
                course_name,
                summary_option,
                complexity_option,
                mcq_option,
                language_option,
                content_distribution_option,
                polycopy_option,
                course_database
            )

            # Display results
            for key, value in responses.items():
                st.subheader(key)
                st.write(value)

if __name__ == "__main__":
    main()

