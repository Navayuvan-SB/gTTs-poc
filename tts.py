from gtts import gTTS

gTTS('how are you doing').save('english.mp3')
gTTS('तुम्ही कसे आहात', lang='mr').save('marathi.mp3')
gTTS('آپ کیسے ہیں', lang='ur').save('urdu.mp3')
gTTS('आप कैसे हैं', lang='hi').save('hindi.mp3')
