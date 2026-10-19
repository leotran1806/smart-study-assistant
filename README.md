# Project: Smart Study Assistant
**A Python project that aims to help students search and understand their study documents using Retrieval-Augmented Generation (RAG).**

## 1. Project Goals:
The long-term goal is to build an application that allows users to:
- Upload study documents.
- Extract and process document text.
- Retrieve relevant passages based on a question.
- Generate answers grounded in the documents.
- Display source references to help users verify answers.

## 2. Current Progress:
**Status: Initial development**

[x] ~~Set up the Python project structure.~~

[x] ~~Create a Python virtual environment.~~

[] Implement text preprocessing utilities.

[] Extract text from PDF files.

[] Build semantic search.

[] Implement the RAG pipeline.

[] Build a user interface.

[] Evaluate answer quality and source citations.

## 3.Project Structure
```text
smart-study-assistant/
├── documents/          # Sample study documents
├── main.py             # Program entry point
├── text_utils.py       # Text processing utilities
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```
## 4. Requirements (Update frequently):
- Python
- pip
- Git

## 5. Setup and Installation

- Step 1. Clone the repository
```text
git clone <https://github.com/leotran1806/smart-study-assistant.git>
cd smart-study-assistant
```
If you are already working inside the project directory, skip this step.

- Step 2. Create a virtual environment
```text
python -m venv venv
```
- Step 3. Activate the virtual environment

On Windows PowerShell:
```text
.venv\Scripts\Activate.ps1
```
- Step 4. Install dependencies
```text
python -m pip install -r requirements.txt
```
- Step 5. Run the application
```text
python main.py
```

## 6. Testing documents:
Only basic documents are published. The other advanced ones are stored in local device.