import os

def get_files_info(working_directory, directory=None):
    try:
        full_directory = os.path.abspath(working_directory + "/" + directory)
        work_directory = os.path.abspath(working_directory)
        if not full_directory.startswith(work_directory):
            print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        elif os.path.isfile(full_directory) or not os.path.isdir(full_directory):
            print(f'Error: "{full_directory}" is not a directory')
        else:
            for file in os.listdir(full_directory):
                this_file = full_directory + "/" + file
                if os.path.isfile(this_file):
                    print(f"- {file}: file_size={os.path.getsize(this_file)} bytes, is_dir=False")
                elif os.path.isdir(this_file):
                    print(f"- {file}: file_size={os.path.getsize(this_file)} bytes, is_dir=True")

    except Exception as e:
        print(f"Error: {e}")

