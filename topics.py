"""Helper prompt builders for the different study modes."""


def explain_concept(topic):
    return (
        "Explain the concept of %s to a student who is new to it. "
        "Use simple language and give a short everyday example." % topic
    )
