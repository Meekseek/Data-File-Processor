# Data File Processor

A Python automation tool designed to parse unstructured text data, manipulate key-value data structures, and reformat output for persistent storage.

### 🎯 Objective
In cybersecurity and system administration, we often encounter log files or configuration dumps that need to be reorganized. This tool demonstrates:
* **File I/O:** Securely reading and writing files using Context Managers (`with open...`).
* **Data Structures:** Manipulating dictionaries and lists to handle data collisions.
* **Error Handling:** Robust `try/except` blocks to manage missing files or permission errors without crashing.

### ⚙️ How It Works
The script reads a file containing `Key: Value` pairs (like "Item: Color"). It then **inverts** the relationship to group items by their value.

**Input Format:**
```text
apple: red
cherry: red
banana: yellow
```
Output Format (Inverted):

Plaintext

red: apple, cherry
yellow: banana
🛠️ Usage
Run the script:

Bash

python processor.py
The script will automatically generate a sample input.txt if one is missing, process the data, and output the results to output.txt.

🚀 Future Improvements
Add support for JSON and CSV file formats.

Implement command-line arguments (CLI) to specify custom input/output paths.
