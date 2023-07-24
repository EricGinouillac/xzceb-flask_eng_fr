from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    c = translator.englishToFrench (textToTranslate)
    return c

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    c = translator.frenchToEnglish (textToTranslate)
    return c

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    f =open ("templates/index.html", "r")
    c = f.read()
    f.close()
    return c

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
