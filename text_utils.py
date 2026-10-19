import os
import unicodedata
def textNormalize(text):
    preprocessedText = []
    for char in text:
        charClassification = unicodedata.category(char)
        if charClassification == "Cf":
            continue
        preprocessedText.append(char)
    cleanText = "".join(preprocessedText)
    cleanText = " ".join(cleanText.split())
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
            resultList = []
            for fileName in os.listdir(folder_path):
                if fileName.endswith(".txt"):
                    pathName = os.path.join(folder_path, fileName)
                    resultList.append(document_Analyze(pathName))
            reportWrite(resultList, folder_path)
        else:
            print("Directory does not exist!")
    except NotADirectoryError:
        print("Invalid directory")
        
def reportWrite(resultList, folder_path):
    folder_path = ".\\report"
    try:
        if os.path.exists(folder_path):
            path_name = os.path.join(folder_path, "report.txt")
            try:
                with open(path_name, "w", encoding="utf-8") as file:
                    for result in resultList:
                        file.write("-------------Report-------------\n")
                        file.write(f'Filename: {result["filename"]}\n')
                        file.write(f'Words count: {result["wordcount"]}\n')
                        file.write(f'Lines count: {result["linecount"]}\n')
                        file.write(f'Characters count: {result["charcount"]}\n')
                        file.write("---------------------------------\n\n")
            except PermissionError:
                print("You do not have permission to read that file!")
    except NotADirectoryError:
        print("Invalid directory")
