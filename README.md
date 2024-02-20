# SummYT
A YouTube video summarizer using BART model

Improved the transcript size to be able to summarize larger videos by upgrading the model to BART-Large-CNN
Bart is a pre trained English model by Facebook/Meta that is fine tuned for text generation and comprehension tasks.

The app uses youtube api to get the video transcript and cleans the text data for reading by the model.
There are size limitations for the input tokens for the model which is solved by using a sliding window approach to maintain context clues as well as fit the token size.

The resulting generated summaries are then printed on the Summary.html page.

Front-end for the app is barebones html and css.
Flask framework is used (GET, POST methods) to communicate between the front end and back end.

Download the file and run the command 'Flask run'
Ensure flask is available in the system.
The models required can be downloaded from hugging-face.


#####
Accuracy of the generated summarization depends on the youtuber's style of content.
A more informative and linear approach generates understandable summarization, whereas a video with multiple topics all over the place do not generate a well made summarization.
Works better for news and informative channels.
