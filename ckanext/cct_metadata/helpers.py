import re

import ckan.plugins.toolkit as toolkit


def label_to_value(label):
    sanitised_string = (
        label.strip()
             .lower()
             .replace(" ", "_")
    )

    pattern = re.compile(r'\W')
    sanitised_string = re.sub(
        pattern, "",
        sanitised_string
    )

    return sanitised_string
