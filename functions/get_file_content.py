import os

import config


def get_file_content(working_directory, file_path):
    try:
        if os.path.commonpath([working_directory, file_path]) != working_directory:
            raise ValueError(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )
        if not os.path.isfile(file_path):
            raise ValueError(
                f'Error: File not found or is not a regular file: "{file_path}"'
            )

        # Read from file
        with open(file_path, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            # If file returns true - not empty. Signify truncation
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
            return file_content_string
    except Exception as e:
        return f"Error: {e}"
