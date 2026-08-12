import os
import re
import subprocess
import shutil

# Files to permanently delete from git and disk
files_to_delete = [
    'notes.ipynb', 'd', 'flats_cleaned.csv', 'house_cleaned.csv',
    'gurugram_properties.csv', 'gurugram_properties_cleaned_v1.csv',
    'gurugram_properties_cleaned_v2.csv', 'gurugram_properties_missing_value_imputation.csv',
    'gurugram_properties_outlier_treated.csv', 'gurugram_properties_post_feature_selection.csv'
]

raw_files = ['flats.csv', 'houses.csv', 'appartments.csv', 'latlong.csv']
processed_files = ['gurugram_properties_post_feature_selection_v2.csv']

# 1. Create Directories
dirs = ['data/raw', 'data/interim', 'data/processed', 'notebooks', 'reports']
for d in dirs:
    os.makedirs(d, exist_ok=True)

# 2. Delete unnecessary files
for f in files_to_delete:
    if os.path.exists(f):
        subprocess.run(['git', 'rm', '-f', f])
if os.path.exists('.ipynb_checkpoints'):
    subprocess.run(['git', 'rm', '-rf', '.ipynb_checkpoints'])
    shutil.rmtree('.ipynb_checkpoints', ignore_errors=True)

# 3. Move files
for f in raw_files:
    if os.path.exists(f):
        subprocess.run(['git', 'mv', f, f'data/raw/{f}'])

for f in processed_files:
    if os.path.exists(f):
        subprocess.run(['git', 'mv', f, f'data/processed/{f}'])

for f in os.listdir('.'):
    if f.endswith('.ipynb') and f not in files_to_delete and f != 'notes.ipynb':
        subprocess.run(['git', 'mv', f, f'notebooks/{f}'])

if os.path.exists('output_report.html'):
    subprocess.run(['git', 'mv', 'output_report.html', 'reports/output_report.html'])

# 4. Create .gitignore
gitignore_content = """__pycache__/
.ipynb_checkpoints/
data/interim/
"""
with open('.gitignore', 'w') as f:
    f.write(gitignore_content)
subprocess.run(['git', 'add', '.gitignore'])

# 5. Rewrite Code Paths in Notebooks
def update_path(match):
    filename = match.group(0)
    if filename in raw_files:
        return f"../data/raw/{filename}"
    elif filename in processed_files:
        return f"../data/processed/{filename}"
    else:
        # All other CSVs (which are now deleted but will be recreated) go to interim
        return f"../data/interim/{filename}"

notebooks_dir = 'notebooks'
if os.path.exists(notebooks_dir):
    for nb in os.listdir(notebooks_dir):
        if not nb.endswith('.ipynb'):
            continue
        filepath = os.path.join(notebooks_dir, nb)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Regex to find csv filenames like flats.csv, gurugram_properties...csv
        # We look for something ending in .csv that doesn't already have a slash before it
        # Actually, let's just specifically replace the exact filenames to be safe
        all_csvs = raw_files + processed_files + [f for f in files_to_delete if f.endswith('.csv')]
        
        new_content = content
        for csv_file in all_csvs:
            # We want to replace "flats.csv" with "../data/raw/flats.csv"
            # But only if it's not already "../data/raw/flats.csv"
            # Since this is the first time we are running this, we can just replace exact string matches
            new_content = re.sub(rf'(?<!/){re.escape(csv_file)}', update_path(re.match(f'.*', csv_file)), new_content)
            
        # Also need to fix output_report.html path in eda-pandas-profiling.ipynb
        new_content = re.sub(r'(?<!/)output_report\.html', '../reports/output_report.html', new_content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated paths in {filepath}")
            subprocess.run(['git', 'add', filepath])

print("Restructuring complete.")
