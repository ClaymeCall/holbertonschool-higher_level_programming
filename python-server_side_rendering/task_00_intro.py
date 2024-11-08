#!/usr/bin/python3
import os


# Define expected keys as a constant
EXPECTED_KEYS = ["name", "event_title", "event_date", "event_location"]

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        raise ValueError("Template must be a string")

    if not isinstance(attendees, list):
        raise ValueError("Attendees must be a list")

    if template.strip() == "":
        raise ValueError("Template is empty")

    if not attendees:
        raise ValueError("Attendees list is empty")

    # Check each attendee for correct type and expected keys
    for i, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            raise ValueError(f"Attendee {i} is not a dictionary")
        missing_keys = EXPECTED_KEYS - attendee.keys()
        if missing_keys:
            raise ValueError(f"Attendee {i} is missing keys: {', '.join(missing_keys)}")


    for index, attendee in enumerate(attendees, start=1):
        content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        file_name = f"output_{index}.txt"
        with open(file_name, "w") as file:
            file.write(content)
        print(f"Invitation generated: {file_name}")
