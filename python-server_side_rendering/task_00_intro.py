import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        logging.error(f"Invalid template type: expected str but got {type(template).__name__}")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid attendees input: expected a list of dictionaries")
        return

    # Handle empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or 'N/A' if missing/None
        filled_template = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            filled_template = filled_template.replace(f"{{{key}}}", str(value) if value else "N/A")

        # Write to output file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(filled_template)
            logging.info(f"File created: {output_filename}")
        except Exception as e:
            logging.error(f"Failed to write {output_filename}: {e}")
