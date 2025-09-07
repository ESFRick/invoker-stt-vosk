from vosk import Model,KaldiRecognizer
import pyaudio
import pyautogui


spells = ["снейп","код снейп","колд снейп","метеор","торнадо","сан страйк","сан","страйк","айс","айс вол","бласт","балласт","емп","ем","еп","олег","алякрити","алакрити","кретин","гост","гост волк","густ волк","фарш","форс спирит","форт спирит","фордж спирит","форж спирит","спирит"]

model = Model("path/to/model/") #Сюда путь до модели vosk(скрипт сделан под vosk-model-small-ru-0.22)
rec = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8096)
stream.start_stream


print("--------------------------------------------------------")
print("speak:")


def contains_text(text, array):
    return any(element in text for element in array)


while True:
    data = stream.read(4096, exception_on_overflow = False)
    if rec.AcceptWaveform(data):
        text = (rec.Result())[14:-3]
        print(text)
        if contains_text(text,spells) == True:

            if text in [spells[0],spells[1],spells[2]]: #cold snap
                for i in range(3):
                    pyautogui.press("q")
                pyautogui.press("r")
                continue


            if text == spells[3]: #meteor
                pyautogui.press("w")
                for i in range(2):
                    pyautogui.press("e")
                pyautogui.press("r")
                continue


            if text == spells[4]: #tornado
                pyautogui.press("q")
                for i in range(2):
                    pyautogui.press("w")
                pyautogui.press("r")
                continue


            if text in [spells[5], spells[6], spells[7]]: #sun strike
                for i in range(3):
                    pyautogui.press("e")
                pyautogui.press("r")
                continue


            if text in [spells[8], spells[9]]: #ice wall
                for i in range(2):
                    pyautogui.press("q")
                pyautogui.press("e")
                pyautogui.press("r")
                continue


            if text in [spells[10], spells[11]]: #blast
                pyautogui.press("q")
                pyautogui.press("w")
                pyautogui.press("e")
                pyautogui.press("r")
                continue


            if text in [spells[12], spells[13], spells[14]]: #e.m.p 
                for i in range(3):
                    pyautogui.press("w")
                pyautogui.press("r")
                continue


            if text in [spells[15], spells[16], spells[17], spells[18]]: #alacrity 
                for i in range(2):
                    pyautogui.press("w")
                pyautogui.press("e")
                pyautogui.press("r")
                continue


            if text in [spells[19], spells[20], spells[21]]: #ghost walk 
                for i in range(2):
                    pyautogui.press("q")
                pyautogui.press("w")
                pyautogui.press("r")
                continue


            if text in [spells[22], spells[23], spells[24], spells[25], spells[26], spells[27]]: #forge spirit
                pyautogui.press("q")
                for i in range(2):
                    pyautogui.press("e")
                pyautogui.press("r")
                continue