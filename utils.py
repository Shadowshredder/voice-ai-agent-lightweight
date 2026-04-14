import os

OUTPUT_FOLDER = "output"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

# -------- INTENT DETECTION --------
def detect_intent(text):
    text = text.lower()

    if "create file" in text or "new file" in text:
        return "create_file"
    elif "write code" in text or "function" in text:
        return "write_code"
    elif "summarize" in text:
        return "summarize"
    else:
        return "chat"

# -------- ACTIONS --------
def create_file(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    with open(path, "w") as f:
        f.write("")
    return f"File '{filename}' created successfully."

def write_code(filename):
    code = """def retry(func, attempts=3):
    for i in range(attempts):
        try:
            return func()
        except:
            pass
    return None
"""
    path = os.path.join(OUTPUT_FOLDER, filename)
    with open(path, "w") as f:
        f.write(code)
    return f"Code written to '{filename}'."

def summarize(text):
    # simple summarization (first 2 lines)
    sentences = text.split(".")
    return ".".join(sentences[:2]) + "."

def chat(text):
    return f"You said: {text}"