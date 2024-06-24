import os
import json
import pandas as pd

def find_form_files(root_path):
    form_files = []
    for subdir, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith('.form'):
                form_files.append(os.path.join(subdir, file))
    return form_files

def extract_ids_from_forms(form_files):
    form_ids = {}
    for file in form_files:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            form_id = data.get('id', '')
            form_ids[file] = form_id
    return form_ids

def read_excel_ids(excel_path):
    df = pd.read_excel(excel_path)
    return set(df['ID Formulario'])

def find_invalid_forms(form_ids, valid_ids):
    invalid_forms = []
    for path, form_id in form_ids.items():
        if form_id not in valid_ids:
            invalid_forms.append((path, form_id))
    return invalid_forms

def save_invalid_forms_to_excel(invalid_forms, output_path):
    df = pd.DataFrame(invalid_forms, columns=['File Location', 'Form ID'])
    df.to_excel(output_path, index=False)

# Paths
excel_path = 'C:\FORMULARIOS_BASURA\output.xlsx'
root_folder_path = 'C:\\ORTOGRAFIA_MACARENIA\\MacareniaBPMNdevelopkevin'
output_excel = 'invalid_forms.xlsx'

# Process
valid_ids = read_excel_ids(excel_path)
form_files = find_form_files(root_folder_path)
form_ids = extract_ids_from_forms(form_files)
invalid_forms = find_invalid_forms(form_ids, valid_ids)
save_invalid_forms_to_excel(invalid_forms, output_excel)

print("Proceso completado. Los formularios no válidos han sido guardados en:", output_excel)
