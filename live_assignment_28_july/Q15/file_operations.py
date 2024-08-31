def read_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found."

def write_file(file_path, data):
    
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        return "Data written successfully."
    except Exception as e:
        return f"Error writing data: {str(e)}"

def append_to_file(file_path, data):
    
    try:
        with open(file_path, 'a') as file:
            file.write(data)
        return "Data appended successfully."
    except Exception as e:
        return f"Error app

ending data: {str(e)}"

