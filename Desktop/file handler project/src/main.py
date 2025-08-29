import os

def read_file(filename):
    """
    Read a file and return its content with error handling
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content, None
    except FileNotFoundError:
        return None, f"Error: File '{filename}' not found."
    except PermissionError:
        return None, f"Error: Permission denied to read '{filename}'."
    except UnicodeDecodeError:
        return None, f"Error: Unable to decode file '{filename}'. It might be a binary file."
    except Exception as e:
        return None, f"Unexpected error: {str(e)}"

def modify_content(content):
    """
    Modify the file content (example: convert to uppercase and add line numbers)
    """
    if content is None:
        return None
    
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Example modification: add line numbers and convert to uppercase
        modified_line = f"{i:03d}: {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def write_file(filename, content):
    """
    Write content to a new file with error handling
    """
    try:
        # Create a modified filename
        base_name, ext = os.path.splitext(filename)
        new_filename = f"{base_name}_modified{ext}"
        
        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return new_filename, None
    except PermissionError:
        return None, f"Error: Permission denied to write '{new_filename}'."
    except Exception as e:
        return None, f"Unexpected error while writing: {str(e)}"

def main():
    """
    Main function to handle user interaction and file operations
    """
    print("📁 File Read & Write Challenge")
    print("=" * 40)
    
    while True:
        # Ask user for filename
        filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
        
        if filename.lower() == 'quit':
            print("Goodbye! 👋")
            break
        
        if not filename:
            print("Please enter a valid filename.")
            continue
        
        # Read the file
        content, error = read_file(filename)
        
        if error:
            print(f"❌ {error}")
            continue
        
        print(f"✅ Successfully read '{filename}'")
        
        # Modify the content
        modified_content = modify_content(content)
        
        if modified_content is None:
            print("❌ No content to modify.")
            continue
        
        # Write the modified content to a new file
        new_filename, write_error = write_file(filename, modified_content)
        
        if write_error:
            print(f"❌ {write_error}")
            continue
        
        print(f"✅ Successfully created modified file: '{new_filename}'")
        
        # Show preview of the modified content
        print("\n📋 Preview of modified content (first 5 lines):")
        print("-" * 40)
        preview_lines = modified_content.split('\n')[:5]
        for line in preview_lines:
            print(line)
        
        # Ask if user wants to see more options
        show_options = input("\nWould you like to see file statistics? (y/n): ").lower()
        if show_options == 'y':
            original_lines = len(content.split('\n'))
            modified_lines = len(modified_content.split('\n'))
            original_chars = len(content)
            modified_chars = len(modified_content)
            
            print(f"\n📊 Statistics:")
            print(f"Original file: {original_lines} lines, {original_chars} characters")
            print(f"Modified file: {modified_lines} lines, {modified_chars} characters")
            print(f"File size increased by: {modified_chars - original_chars} characters")

def create_sample_file():
    """
    Create a sample file for testing if needed
    """
    sample_content = """Hello and welcome to the file handling challenge!
This is a sample text file created for testing purposes.
Python file operations are essential for many applications.
Error handling makes our programs more robust and user-friendly.
Remember to always close your files properly!"""
    
    with open("sample.txt", "w") as file:
        file.write(sample_content)
    print("✅ Created sample.txt for testing")

if __name__ == "__main__":
    # Create a sample file if it doesn't exist
    if not os.path.exists("sample.txt"):
        create_sample_file()
        print("💡 A sample file 'sample.txt' has been created for testing.")
    
    # Run the main program
    main()