from utils.watsonx_wrapper import call_watsonx

def classify_text(text):
    prompt = f"Classify these requirements into SDLC phases:\n{text}"
    response = call_watsonx(prompt)
    return {"AI Classification": response.split('\n')}

def generate_code(prompt):
    return call_watsonx(f"Generate Python code for:\n{prompt}")

def fix_code(code):
    return call_watsonx(f"Fix bugs in this code:\n{code}")

def generate_tests(code):
    return call_watsonx(f"Write unit tests for:\n{code}")

def summarize_code(code):
    return call_watsonx(f"Summarize this code:\n{code}")

def chat_response(query):
    return call_watsonx(f"Answer this SDLC question: {query}")
