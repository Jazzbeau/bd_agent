import os


def get_files_info(working_directory, directory="."):
    try:
        wd_path = os.path.abspath(working_directory)
        cd_path = os.path.normpath(os.path.join(wd_path, directory))

        valid_dir = os.path.commonpath([wd_path, cd_path]) == wd_path

        if not valid_dir:
            raise ValueError(
                f'Cannot list "{directory}" as it is outside the permitted working directory'
            )
        elif not os.path.isdir(cd_path):
            raise ValueError(f'"{directory}" is not a directory')

        dir_cont = []
        for file in os.listdir(cd_path):
            fp = os.path.join(cd_path, file)
            dir_status = os.path.isdir(fp)
            file_size = os.path.getsize(fp)
            dir_cont.append(f"- {file}: file_size={file_size}, is_dir={dir_status}")
        return str.join("\n", dir_cont)
    except Exception as e:
        return f"Error: {e}"
