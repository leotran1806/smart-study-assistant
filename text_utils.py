import os
def textNormalize(text):
    text.strip()
    cleanText = " ".join(text.split())
    return cleanText

def countWords(text):
    return len(text.split())

def document_Analyze(path_name):
    word_count = 0
    lineCount = 0
    charCount = 0
    try:
        with open(path_name, "r", encoding="utf-8") as file:
            data = file.readline()
            lineCount += 1
            while data:
                clean_text = textNormalize(data)
                word_count += countWords(clean_text)
                charCount += len(clean_text)
                data = file.readline()
                if data != '':
                    lineCount += 1
    except FileNotFoundError:
        print("File does not exist")
    except PermissionError:
        print("You do not have permission to read that file!")
    result = {"filename": path_name,
              "wordcount": word_count,
              "charcount": charCount,
              "linecount": lineCount}
    return result

def directoryAnalyze(folder_path):
    try:
        if os.path.exists(folder_path):
            for fileName in os.listdir(folder_path):
                if fileName.endswith(".txt"):
                    pathName = os.path.join(folder_path, fileName)
                reportWrite(document_Analyze(pathName))
        else:
            print("Directory does not exist!")
    except NotADirectoryError:
        print("Invalid directory")
        
def reportWrite(result):
    print("-------------Report-------------")
    print(f'Filename: {result["filename"]}')
    print(f'Words count: {result["wordcount"]}')
    print(f'Lines count: {result["linecount"]}')
    print(f'Characters count: {result["charcount"]}')
    print("---------------------------------")
    print()
