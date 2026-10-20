import os
def normalize_text(text):
    cleanText = " ".join(text.split())
    print(cleanText)
    return cleanText

def words_count_for_normalized_text(text):
    return len(text.split())

def document_Analyze(path_name):
    try:
        with open(path_name, "r", encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"File does not exist: {path_name}")
        return None
    except PermissionError:
        print(f"Permission denied: {path_name}")
        return None
    normalized_text = normalize_text(data)
    result = {"filename": path_name,
              "wordcount": words_count_for_normalized_text(normalized_text),
              "charcount": len(normalized_text),
              }
    return result

def analyze_directory(folder_path):
    try:
        if os.path.exists(folder_path):
            resultList = []
            for fileName in os.listdir(folder_path):
                if fileName.endswith(".txt"):
                    pathName = os.path.join(folder_path, fileName)
                    result = document_Analyze(pathName)
                    if result is not None:
                        resultList.append(result)
            write_report(resultList)
        else:
            print("Directory does not exist!")
    except NotADirectoryError:
        print("Invalid directory")
        
def write_report(resultList):
    folder_path = "./report"
    os.makedirs(folder_path, exist_ok= True)
    if os.path.exists(folder_path):
        path_name = os.path.join(folder_path, "report.txt")
        try:
            with open(path_name, "w", encoding="utf-8") as file:
                print("Writing report...")
                for result in resultList:
                    file.write("-------------Report-------------\n")
                    file.write(f'Filename: {result["filename"]}\n')
                    file.write(f'Words count: {result["wordcount"]}\n')
                    file.write(f'Characters count: {result["charcount"]}\n')
                    file.write("---------------------------------\n\n")
                print("Writing complete")
        except PermissionError:
            print(f"You do not have permission to write to: {path_name} ")
