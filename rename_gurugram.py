import os
import re
import subprocess

directory = '.'

# 1. First, rename files in git
files_in_dir = os.listdir(directory)
for filename in files_in_dir:
    if os.path.isfile(filename) and ('gurgaon' in filename.lower() or 'gurgao' in filename.lower()):
        new_filename = re.sub(r'gurgaon|gurgao', 'gurugram', filename, flags=re.IGNORECASE)
        if new_filename != filename:
            print(f"Renaming {filename} to {new_filename}")
            subprocess.run(['git', 'mv', filename, new_filename])

# 2. Now iterate through all text files to replace content
allowed_extensions = ['.csv', '.ipynb', '.html', '.md', '.txt']
for root, _, files in os.walk(directory):
    if '.git' in root or '.ipynb_checkpoints' in root:
        continue
    for filename in files:
        if not any(filename.endswith(ext) for ext in allowed_extensions):
            continue
            
        filepath = os.path.join(root, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # First handle lowercase references to dataset files
            new_content = re.sub(r'gurgaon_properties', 'gurugram_properties', content, flags=re.IGNORECASE)
            new_content = re.sub(r'gurgao_properties', 'gurugram_properties', new_content, flags=re.IGNORECASE)
            
            # Then handle generic text references
            new_content = re.sub(r'gurgaon', 'Gurugram', new_content, flags=re.IGNORECASE)
            new_content = re.sub(r'gurgao', 'Gurugram', new_content, flags=re.IGNORECASE)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated content in {filepath}")
        except Exception as e:
            print(f"Error reading/writing {filepath}: {e}")

print("Done updating contents.")
