"""Helper prompt builders for the different study modes."""


def explain_concept(topic):
    return (
        "Explain the concept of %s to a student who is new to it. "
        "Use simple language and give a short everyday example." % topic
    )


def make_quiz(topic, num_questions=5):
    return (
        "Create a %d question quiz about %s. "
        "Number each question, and put the answers in an answer key at the bottom."
        % (num_questions, topic)
    )


def summarize_notes(notes):
    return (
        "Summarize the following study notes into clear bullet points "
        "highlighting the key ideas:\n\n%s" % notes
    )
