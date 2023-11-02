import os

def search_files(root_directory, file_types, file_name_contains):
    if not os.path.exists(root_directory):
        raise Exception(f"Not a valid root directory: {root_directory}")
    traversed_directories = []
    found_files = []
    total_size = 0
    
    if len(file_types) < 1:
        for (root,dirs,files) in os.walk(root_directory): 
            for file in files:
                traversed_directories.append(root)
                found_file = f"{root}/{file}".replace('\\', '/')
                found_files.append(found_file)
                total_size += os.path.getsize(found_file)
    else:
        for (root,dirs,files) in os.walk(root_directory): 
            for file in files:
                traversed_directories.append(root)
                for file_type in file_types:
                    if file.split('.')[-1] == file_type:
                        for substring in file_name_contains:
                            if substring in file:
                                found_file = f"{root}/{file}".replace('\\', '/')
                                found_files.append(found_file)
                                total_size += os.path.getsize(found_file)
                                break

    traversed_directories = sorted(set(traversed_directories)) # Removing duplicates
    return traversed_directories, found_files, total_size

def write_results(location, name, traversed_directories, found_files, total_size):
    if not os.path.exists(location):
        raise Exception(f"Not a valid result file directory: {location}")
    file = open(f"{location}/{name}", 'w', encoding="utf-8")
    file.write(f"Files found: {len(found_files)} | Directories traversed: {len(traversed_directories)} | Total size of the files (bytes): {total_size}\n")
    file.write('--------------------------------------------------------------------------------\n')
    for i in range(len(found_files)):
        file.write(f"{found_files[i]}\n")
    file.close()

def main():
    # Search Parameters
    root_directory = 'C:/'
    file_types = [
        'png',
        'PNG'
    ]
    file_name_contains = [
        'test'
    ]
    # Result File Parameters
    result_file_location = 'C:/Users/Aironas/Downloads'
    result_file_name = 'test.txt'
    
    traversed_directories, found_files, total_size = search_files(root_directory, file_types, file_name_contains)
    write_results(result_file_location, result_file_name, traversed_directories, found_files, total_size)
    
if __name__ == "__main__":
    main()