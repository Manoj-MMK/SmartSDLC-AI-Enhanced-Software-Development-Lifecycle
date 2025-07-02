from flask import Flask, render_template, request
from utils import ai_handler

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods=["GET", "POST"])
def classify():
    result = None
    if request.method == "POST":
        text = request.form["req_text"]
        result = ai_handler.classify_text(text)
    return render_template("classify.html", result=result)

@app.route("/codegen", methods=["GET", "POST"])
def codegen():
    code = None
    if request.method == "POST":
        prompt = request.form["code_prompt"]
        code = ai_handler.generate_code(prompt)
    return render_template("codegen.html", code=code)

@app.route("/bugfix", methods=["GET", "POST"])
def bugfix():
    fixed = None
    if request.method == "POST":
        buggy_code = request.form["buggy_code"]
        fixed = ai_handler.fix_code(buggy_code)
    return render_template("bugfix.html", fixed=fixed)

@app.route("/testgen", methods=["GET", "POST"])
def testgen():
    tests = None
    if request.method == "POST":
        code = request.form["test_code"]
        tests = ai_handler.generate_tests(code)
    return render_template("testgen.html", tests=tests)

@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    summary = None
    if request.method == "POST":
        code = request.form["summary_code"]
        summary = ai_handler.summarize_code(code)
    return render_template("summarize.html", summary=summary)

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    reply = None
    if request.method == "POST":
        query = request.form["query"]
        reply = ai_handler.chat_response(query)
    return render_template("chatbot.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
