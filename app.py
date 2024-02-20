from transformers import pipeline
import re
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, request, render_template


app = Flask(__name__,static_url_path='/static')   
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
def getlink(link):
    pattern='='
    spl=re.split(pattern,link)
    address=str(spl[1])
    gettext(address)

def gettext(address):
    data=[]
    script=YouTubeTranscriptApi.get_transcript(address)
    length=len(script)

    for i in range(length):
        for val in script[i].items():
            data.append(script[i]['text'])
            break
    cleanText(data)

def cleanText(data):
    global Summary
    textData = ' '.join([str(word) for word in data])
    Tlength = len(textData)
    overlap = 50
    max_length = 1022
    segments = [textData[i:i + 500] for i in range(0, Tlength, max_length - overlap)]
    summaries = [summarizer(segment, max_length=70, min_length=30, do_sample=False)[0]['summary_text'] for segment in segments]
    Summary = ' '.join(summaries)
    # Assign the result directly to the global variable
    Summary = str(Summary)
    return Summary


@app.route('/', methods=['GET', 'POST'])
def getLink():
    if request.method =='POST':
        YTLink = request.form['link']
        getlink(YTLink)
        return render_template('summary.html', summarytext = Summary)
	
    if request.method == 'GET':
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)