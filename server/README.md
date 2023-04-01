## Instructions to setup the server

1. Add [Vosk Speech2Text](https://alphacephei.com/vosk/models/vosk-model-en-in-0.4.zip) model to 
```
server/models/
```
and rename the unzipped directory as **model**.

2. Install the dependencies by typing the following command in the terminal.
```
pip install -r requirements.txt
```
<b>Note: Run the terminal in the server directory.</b>

3. Install [FFMPEG](https://www.ffmpeg.org/download.html) for audio extraction from video and set the path in the environment variable of the system.

4. Install nltk dependencies using the following command in the terminal.
```
python dep.py
```

5. Server can be run on port: 5000 by
```
flask run
```
<b> Note : </b> -> Remember to run the server before starting client.

-> While selecting a media stream, choose a tab since audio can only be recorded through a tab (MediaRecorder API restrictions)

-> The HuggingFace Inference API may take some time to load the model (which will be corrected in the future) forcing punctuation outputs to                     showcase an error. In such a case, try running the **summarize** button again for from the client

