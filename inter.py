# Work in progress
from moviepy.editor import AudioFileClip
from PyQt4.QtWidgets import QFileDialog
import speech_recognition as sr

def open_audio_file(self):
    file_name = QFileDialog.getOpenFileName()
    if file_name[0][-3:] == 'mp4':
        self.transcribe_button.setEnabled(True)
        self.mp4_file_name = file_name[0]
        self.message_label.setText("")
        self.selected_video_label.setText(file_name[0])
    else:
        self.message_label.setText("Please select an .mp4 file")

    self.trascribed_button.clicked.connect(self.process_and_transcribe_audio)

def process_and_transcribe_audio(self):
    self.transcribe_button.setEnabled(False)
    self.convert_mp4_to_wav()
    self.transcribe_audio(self.audio_file)

def __init__(self):
    self.mp4_file_name = ''
    self.output_file = ''
    self.audio_file = 'speech.wav'

def convert_mp4_to_wav(self):
    audio_clip = AudioFileClip(self.mp4_file_name)
    audio_clip.write_audiofile(self.audio_file)


def transcribe_audio(self, audio_file):
    r = sr.Recognizer()
    total_duration = self.get_audio_duration(audio_file) / 10
    total_duration = math.ceil(total_duration)

    if len(self.output_file_name.toPlainText()) > 0:
        self.output_file = self.output_file_name.toPlainText()
    else:
        self.output_file = 'my_speech.txt'

    for i in range(0, total_duration):
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source, offset=i*10, duration=10)
            self.progress_bar.setValue(i)
        f.open(self.output_file, 'a')
        f.write(r.recognize_google(audio))
        f.write(" ")
    f.close()
    self.progress_bar.setValue(100)
    self.transcribe_button.setEnabled(True)
    self.message_label.setText("")
    self.update_text_output()