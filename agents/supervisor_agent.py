from agents.agents import get_course_data, summary_agent, complexity_agent, mcq_agent, language_agent, \
    content_distribution_agent, polycopy_agent


def supervisor_agent(course_name, summary, complexity, mcq, language, content_distribution, polycopy, database):
    """Manage sub-agent calls."""
    responses = {}
    if summary:
        responses['Course Summary'] = summary_agent(course_name, database)
    if complexity:
        responses['Course Complexity'] = complexity_agent(course_name, database)
    if mcq:
        responses['Generated MCQ'] = mcq_agent(course_name, database)
    if language:
        responses['Course Language'] = language_agent(course_name, database)
    if content_distribution:
        responses['Content Distribution'] = content_distribution_agent(course_name, database)
    if polycopy:
        responses['Polycopy Availability'] = polycopy_agent(course_name, database)
    return responses

