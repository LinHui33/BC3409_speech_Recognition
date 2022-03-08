
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import speech_recognition as sr


# In[ ]:


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print("File Received")
        filename = secure_filename(file.filename)
        file.save("static/" + filename)
        print("pass")
        a = sr.AudioFile("static/" + filename)
        with a as source:
            a = sr.Recognizer().record(source)
        s = sr.Recognizer().recognize_google(a)
        print(s)
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()

