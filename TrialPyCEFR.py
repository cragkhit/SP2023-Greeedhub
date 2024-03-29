
# import subprocess
# import json
# import csv
# from collections import defaultdict
# from pathlib import Path
# import os

# # Define the directories
# pycefr_dir = 'C:\\Users\\rujip\\Desktop\\SP2023-Greeedhub\\pycefr'  # Path to the PyCEFR scripts
# json_data_dir = os.path.join(pycefr_dir, 'DATA_JSON')  # Where JSON data is stored
# output_dir = 'C:\\Users\\rujip\\Desktop\\SP2023-Greeedhub\\CompetencyScore'  # Output directory for CSV and JSON files

# # Ensure output directory exists
# Path(output_dir).mkdir(parents=True, exist_ok=True)

# # Define error log file path
# error_log_file = os.path.join(output_dir, 'error_log.txt')

# def clone_pycefr_repository():
#     """
#     Clones the PyCEFR repository from GitHub.
#     """
#     if not Path(pycefr_dir).exists():
#         try:
#             subprocess.run(['git', 'clone', 'https://github.com/anapgh/pycefr.git', pycefr_dir], check=True)
#             print("PyCEFR repository cloned successfully.")
#         except subprocess.CalledProcessError as e:
#             print(f"Error cloning PyCEFR repository: {e}")
#     else:
#         print("PyCEFR repository already exists.")

# def run_pycefr_analysis():
#     """
#     Runs the PyCEFR analysis by executing its scripts and generating JSON data.
#     Attempts to continue execution even if an error occurs in subprocess calls.
#     """
#     original_dir = os.getcwd()
#     os.chdir(pycefr_dir)
    
#     scripts = [
#         ('python', 'dict.py'),
#         ('python', 'pycerfl.py', 'directory', '../PythonFiles')
#     ]
    
#     with open(error_log_file, 'a') as error_log:
#         for script_command in scripts:
#             try:
#                 print(f"Executing command: {' '.join(script_command)}")
#                 subprocess.run(script_command, check=True)
#             except subprocess.CalledProcessError as e:
#                 error_msg = f"Error running {script_command[1]}: {e}."
#                 print(error_msg)
#                 error_log.write(error_msg + '\n')
#             except UnicodeEncodeError as ue_error:
#                 error_msg = f"UnicodeEncodeError: {ue_error}."
#                 print(error_msg)
#                 error_log.write(error_msg + '\n')
#                 error_log.write(f"Occurred in {script_command[1]}\n")
    
#     os.chdir(original_dir)

# def process_json_files():
#     """
#     Processes JSON files generated by PyCEFR to extract competency levels and 
#     generate summary CSV and JSON files.
#     """
#     for json_file in Path(json_data_dir).glob('*.json'):
#         process_json_file(json_file)

# def process_json_file(json_file):
#     """
#     Processes a single JSON file generated by PyCEFR to extract competency levels and 
#     generate summary CSV and JSON files.
#     """
#     with open(json_file) as f:
#         data = json.load(f)

#     commit_hash = json_file.stem
#     all_files_data = data.get(commit_hash, {})
    
#     after_sum, before_sum = defaultdict(int), defaultdict(int)
    
#     for file_name, file_content in all_files_data.items():
#         parts = file_name.split('_')
#         if len(parts) < 7:  # Adjusted for time format inclusion
#             print(f"Unexpected filename structure: {file_name}")
#             continue
        
#         project_name = parts[1]  # Extract project name
#         author_id, author_date_format, time_format, status = parts[2], parts[3], parts[4], parts[5]
        
#         for level, score in file_content['Levels'].items():
#             if 'after' in status:
#                 after_sum[level] += score
#             elif 'before' in status:
#                 before_sum[level] += score
    
#     diff = {level: after_sum[level] - before_sum.get(level, 0) for level in set(after_sum) | set(before_sum)}
    
#     generate_summary_files(commit_hash, project_name, author_id, author_date_format, time_format, after_sum, before_sum, diff)

# def generate_summary_files(commit_hash, project_name, author_id, author_date_format, time_format, after_sum, before_sum, diff):
#     """
#     Generates CSV and JSON summary files for competency levels, including time format.
#     """
#     output_csv_dir = os.path.join(output_dir, 'CSV', project_name, author_id)
#     output_json_dir = os.path.join(output_dir, 'JSON', project_name, author_id)
#     Path(output_csv_dir).mkdir(parents=True, exist_ok=True)
#     Path(output_json_dir).mkdir(parents=True, exist_ok=True)

#     summary_base = f"{commit_hash}_summary_{author_date_format}_{time_format}"
#     csv_path = os.path.join(output_csv_dir, f"{summary_base}.csv")
#     json_path = os.path.join(output_json_dir, f"{summary_base}.json")

#     with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:  # Specify encoding as 'utf-8-sig'
#         writer = csv.writer(csvfile)
#         writer.writerow(['CommitHash', 'ProjectName', 'AuthorID', 'AuthorDateFormat', 'TimeFormat', 'Level', 'After', 'Before', 'Difference'])
#         for level in sorted(set(after_sum.keys()).union(before_sum.keys())):
#             writer.writerow([
#                 commit_hash, project_name, author_id, author_date_format, time_format,
#                 level, after_sum.get(level, 0), before_sum.get(level, 0), diff.get(level, 0)
#             ])

#     with open(json_path, 'w') as jsonfile:
#         json.dump({
#             'CommitHash': commit_hash,
#             'ProjectName': project_name,
#             'AuthorID': author_id,
#             'AuthorDateFormat': author_date_format,
#             'TimeFormat': time_format,
#             'Levels': {
#                 'After': dict(after_sum),
#                 'Before': dict(before_sum),
#                 'Difference': dict(diff)
#             }
#         }, jsonfile, indent=4)

# def main():
#     # Step 1: Clone PyCEFR repository
#     clone_pycefr_repository()

#     # Step 2: Run PyCEFR analysis
#     run_pycefr_analysis()
    
#     # Step 3: Process the JSON files to generate summaries
#     process_json_files()

#     print("Analysis and summary generation completed.")

# if __name__ == "__main__":
#     main()

# Code for TrialPyCEFR.py
import subprocess
import json
import csv
from collections import defaultdict
from pathlib import Path
import os

# Define the directories
pycefr_dir = 'C:\\Users\\rujip\\Desktop\\SP2023-Greeedhub\\pycefr'  # Path to the PyCEFR scripts
json_data_dir = os.path.join(pycefr_dir, 'DATA_JSON')  # Where JSON data is stored
output_dir = 'C:\\Users\\rujip\\Desktop\\SP2023-Greeedhub\\CompetencyScore'  # Output directory for CSV and JSON files

# Ensure output directory exists
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Define error log file path
error_log_file = os.path.join(output_dir, 'error_log.txt')

def clone_pycefr_repository():
    """
    Clones the PyCEFR repository from GitHub.
    """
    if not Path(pycefr_dir).exists():
        try:
            subprocess.run(['git', 'clone', 'https://github.com/anapgh/pycefr.git', pycefr_dir], check=True)
            print("PyCEFR repository cloned successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning PyCEFR repository: {e}")
    else:
        print("PyCEFR repository already exists.")

def run_pycefr_analysis():
    """
    Runs the PyCEFR analysis by executing its scripts and generating JSON data.
    Attempts to continue execution even if an error occurs in subprocess calls.
    """
    original_dir = os.getcwd()
    os.chdir(pycefr_dir)
    
    scripts = [
        ('python', 'dict.py'),
        ('python', 'pycerfl.py', 'directory', '../PythonFiles')
    ]
    
    with open(error_log_file, 'a') as error_log:
        for script_command in scripts:
            try:
                print(f"Executing command: {' '.join(script_command)}")
                subprocess.run(script_command, check=True)
            except subprocess.CalledProcessError as e:
                error_msg = f"Error running {script_command[1]}: {e}."
                print(error_msg)
                error_log.write(error_msg + '\n')
            except UnicodeEncodeError as ue_error:
                error_msg = f"UnicodeEncodeError: {ue_error}."
                print(error_msg)
                error_log.write(error_msg + '\n')
                error_log.write(f"Occurred in {script_command[1]}\n")
    
    os.chdir(original_dir)

def process_json_files():
    """
    Processes JSON files generated by PyCEFR to extract competency levels and 
    generate summary CSV and JSON files.
    """
    for json_file in Path(json_data_dir).glob('*.json'):
        process_json_file(json_file)

def process_json_file(json_file):
    """
    Processes a single JSON file generated by PyCEFR to extract competency levels and 
    generate summary CSV and JSON files.
    """
    with open(json_file) as f:
        data = json.load(f)

    commit_hash = json_file.stem
    all_files_data = data.get(commit_hash, {})
    
    after_sum, before_sum = defaultdict(int), defaultdict(int)
    
    for file_name, file_content in all_files_data.items():
        parts = file_name.split('_')
        if len(parts) < 7:  # Adjusted for time format inclusion
            print(f"Unexpected filename structure: {file_name}")
            continue
        
        project_name = parts[1]  # Extract project name
        author_id, author_date_format, time_format, status = parts[2], parts[3], parts[4], parts[5]
        
        for level, score in file_content['Levels'].items():
            if 'after' in status:
                after_sum[level] += score
            elif 'before' in status:
                before_sum[level] += score
    
    diff = {level: after_sum[level] - before_sum.get(level, 0) for level in set(after_sum) | set(before_sum)}
    
    generate_summary_files(commit_hash, project_name, author_id, author_date_format, time_format, after_sum, before_sum, diff)

def generate_summary_files(commit_hash, project_name, author_id, author_date_format, time_format, after_sum, before_sum, diff):
    """
    Generates CSV and JSON summary files for competency levels, including time format.
    """
    output_csv_dir = os.path.join(output_dir, 'CSV', project_name, author_id)
    output_json_dir = os.path.join(output_dir, 'JSON', project_name, author_id)
    Path(output_csv_dir).mkdir(parents=True, exist_ok=True)
    Path(output_json_dir).mkdir(parents=True, exist_ok=True)

    summary_base = f"{commit_hash}_summary_{author_date_format}_{time_format}"
    csv_path = os.path.join(output_csv_dir, f"{summary_base}.csv")
    json_path = os.path.join(output_json_dir, f"{summary_base}.json")

    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:  # Specify encoding as 'utf-8-sig'
        writer = csv.writer(csvfile)
        writer.writerow(['CommitHash', 'ProjectName', 'AuthorID', 'AuthorDateFormat', 'TimeFormat', 'Level', 'After', 'Before', 'Difference'])
        for level in sorted(set(after_sum.keys()).union(before_sum.keys())):
            writer.writerow([
                commit_hash, project_name, author_id, author_date_format, time_format,
                level, after_sum.get(level, 0), before_sum.get(level, 0), diff.get(level, 0)
            ])

    with open(json_path, 'w') as jsonfile:
        json.dump({
            'CommitHash': commit_hash,
            'ProjectName': project_name,
            'AuthorID': author_id,
            'AuthorDateFormat': author_date_format,
            'TimeFormat': time_format,
            'Levels': {
                'After': dict(after_sum),
                'Before': dict(before_sum),
                'Difference': dict(diff)
            }
        }, jsonfile, indent=4)

def main():
    # Step 1: Clone PyCEFR repository
    clone_pycefr_repository()

    # Step 2: Run PyCEFR analysis
    run_pycefr_analysis()
    
    # Step 3: Process the JSON files to generate summaries
    process_json_files()

    print("Analysis and summary generation completed.")

if __name__ == "__main__":
    main()
