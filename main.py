from gtts import gTTS
import csv
import os
from pydub import AudioSegment


## open csv file which have the title and text-to-audio data 
with open('audio.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  next(csvFile, None)
  titles = []
  audios = []
  for lines in csvFile:
        titles.append(lines[0].strip())
        audios.append(lines[1].strip())

## debug 
# print(titles)
# print(audios)

## create text-to-audio and save in generated-audio file 
if(len(titles) == len(audios)): # if length not same recheck the csv file 
    for x in range(len(titles)):
        tts = gTTS(audios[x], lang="en", tld="us", slow=False)
        tts.save("./generated-audio/"+titles[x]+".mp3")

## concatenate the bell sound at the start to the generated audios above, save in the final folder 
path = "generated-audio"
dir_list = os.listdir(path)
#print(dir_list)

for file in dir_list:
    bell_sound = AudioSegment.from_mp3("announcement-bell.mp3")
    original_path = "./generated-audio/" + file
    original_sound = AudioSegment.from_mp3(original_path)
    final_sound = bell_sound.append(original_sound)
    final_sound.export("./final-audio/final_" + file, format="mp3")

print("Done. Can check files now in the final-audio folder!")
