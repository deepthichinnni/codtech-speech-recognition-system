import speech_recognition as sr

# create recognizer
recognizer = sr.Recognizer()

# use microphone
with sr.Microphone() as source:
    print("Speak something...")

    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)

    print("You said:")
    print(text)

    # save output text
    with open("output.txt", "w") as file:
        file.write(text)

except Exception as e:
    print("Error recognizing speech:", e)