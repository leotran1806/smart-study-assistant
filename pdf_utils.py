import pypdf
import os
def extract_text_from_pdf(file_path):
    try:
        analyzed_file = []
        reader = pypdf.PdfReader(file_path)
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text(extraction_mode="layout")
            analyzed_file.append({"page": page_num + 1, "text": text})
        return analyzed_file
    except PermissionError:
        print(f"Permission denied: {file_path}")
        
def directory_analyze(folder_path):
    try:
        if os.path.exists(folder_path):
            analyzed_data_list = []
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".pdf"):
                    file_path = os.path.join(folder_path, file_name)
                    analyzed_data = extract_text_from_pdf(file_path)
                    analyzed_data_list.append({"filename": file_name, "data": analyzed_data})
            return analyzed_data_list
        else:
            print("Directory does not exist!")
    except NotADirectoryError:
        print("{folder_path} is not a directory!")

    
    