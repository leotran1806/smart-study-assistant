import os
def normalize_text(text):
    cleanText = " ".join(text.split())
    return cleanText

def words_count_for_normalized_text(text):
    return len(text.split())

def document_analyze(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
            normalized_text = normalize_text(data)
            result = {"filename": file_path,
                "wordcount": words_count_for_normalized_text(normalized_text),
                "charcount": len(normalized_text),
            }
            return result
    except FileNotFoundError:
        print(f"File does not exist: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None
    

def directory_analyze(folder_path):
    try:
        if os.path.exists(folder_path):
            analyzed_data_list = []
            for file_name in os.listdir(folder_path):
                if file_name.endswith(".txt"):
                    file_path = os.path.join(folder_path, file_name)
                    analyzed_data = document_analyze(file_path)
                    if analyzed_data is not None:
                        analyzed_data_list.append(analyzed_data)
            write_report(analyzed_data_list)
        else:
            print("Directory does not exist!")
    except NotADirectoryError:
        print("{folder_path} is not a directory!")
        
def write_report(result_list):
    folder_path = "./report"
    os.makedirs(folder_path, exist_ok= True)
    if os.path.exists(folder_path):
        path_name = os.path.join(folder_path, "report.txt")
        try:
            with open(path_name, "w", encoding="utf-8") as file:
                print("Writing report...")
                for result in result_list:
                    file.write("-------------Report-------------\n")
                    file.write(f'Filename: {result["filename"]}\n')
                    file.write(f'Words count: {result["wordcount"]}\n')
                    file.write(f'Characters count: {result["charcount"]}\n')
                    file.write("---------------------------------\n\n")
                print("Writing complete")
        except PermissionError:
            print(f"You do not have permission to write to: {path_name} ")
