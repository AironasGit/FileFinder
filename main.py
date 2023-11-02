import os

def filter_by_extensions(found_files, file_extensions):
    if len(file_extensions) < 1:
        return found_files
    _found_files = []
    for found_file in found_files:
        for file_extension in file_extensions:
           if found_file.split('.')[-1] == file_extension:
               _found_files.append(found_file)
    return _found_files

def filter_by_substrings(found_files, substrings):
    if len(substrings) < 1:
        return found_files
    _found_files = []
    for found_file in found_files:
        for substring in substrings:
            if substring in found_file.split('/')[-1]:
                _found_files.append(found_file)
                break
    return _found_files

def search_files(root_directory, file_extensions, substrings):
    if not os.path.exists(root_directory):
        raise Exception(f"Not a valid root directory: {root_directory}")
    found_files = []
    total_size = 0
    
    # Find all files
    for (root,dirs,files) in os.walk(root_directory): 
        for file in files:
            found_file = f"{root}/{file}".replace('\\', '/')
            found_files.append(found_file)

    # Filter the files
    found_files = filter_by_extensions(found_files, file_extensions)
    found_files = filter_by_substrings(found_files, substrings)

    for found_file in found_files:
        total_size += os.path.getsize(found_file)

    return found_files, total_size

def write_results(location, name, found_files, total_size):
    if not os.path.exists(location):
        raise Exception(f"Not a valid result file directory: {location}")
    file = open(f"{location}/{name}", 'w', encoding="utf-8")
    file.write(f"Files found: {len(found_files)} | Total size of the files (bytes): {total_size}\n")
    file.write('--------------------------------------------------------------\n')
    for i in range(len(found_files)):
        file.write(f"{found_files[i]}\n")
    file.close()

def main():
    # Search Parameters
    root_directory = 'C:/'
    file_extensions = [
        'png',
        'PNG'
    ]
    substrings = [
    ]
    # Result File Parameters
    result_file_location = 'C:/Users/Aironas/Downloads'
    result_file_name = 'test.txt'
    
    found_files, total_size = search_files(root_directory, file_extensions, substrings)
    write_results(result_file_location, result_file_name, found_files, total_size)
    
if __name__ == "__main__":
    main()