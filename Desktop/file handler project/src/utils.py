def batch_process_files(file_list):
    """
    Process multiple files in batch mode
    """
    results = []
    for filename in file_list:
        content, error = read_file(filename)
        if error:
            results.append(f"❌ {filename}: {error}")
            continue
        
        modified_content = modify_content(content)
        new_filename, write_error = write_file(filename, modified_content)
        
        if write_error:
            results.append(f"❌ {filename}: {write_error}")
        else:
            results.append(f"✅ {filename} → {new_filename}")
    
    return results

def file_info(filename):
    """
    Get detailed information about a file
    """
    try:
        stats = os.stat(filename)
        return {
            'size': stats.st_size,
            'modified': stats.st_mtime,
            'created': stats.st_ctime,
            'is_file': os.path.isfile(filename),
            'is_dir': os.path.isdir(filename)
        }
    except Exception as e:
        return f"Error getting file info: {str(e)}"

# Example usage of utility functions
if __name__ == "__main__":
    # Batch processing example
    files_to_process = ["file1.txt", "file2.txt", "file3.txt"]
    results = batch_process_files(files_to_process)
    for result in results:
        print(result)