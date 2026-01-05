import os

import config


def get_file_content(working_directory, file_path):
    try:
        abs_dir = os.path.abspath(working_directory)
        abs_file = os.path.normpath(os.path.join(abs_dir, file_path))
        if os.path.commonpath([abs_dir, abs_file]) != abs_dir:
            raise ValueError(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(abs_file):
            raise ValueError(f'File not found or is not a regular file: "{file_path}"')

        # Read from file
        with open(abs_file, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            # If file returns true - not empty. Signify truncation
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
