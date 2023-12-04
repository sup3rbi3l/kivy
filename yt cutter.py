from PySimpleGUI import PySimpleGUI as sg
from pydub import AudioSegment
from pytube import YouTube
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename



sg.theme('Dark Brown 1')

def onlyInt(value):
    try:
        valor = int(value)
    except Exception:
        print('value error')
        valor = ''

    return valor

def downloadVideo(link, boolean):
    run = True
    # url input from user
    try:
        yt = YouTube(link)
    except Exception:
        run = False
        print("coloque um link do yt")
    if run:
        if boolean == False:
            # extract only audio
            video = yt.streams.get_highest_resolution()

            return video.download()
        
        elif boolean:
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download()
            base, ext = os.path.splitext(out_file)
            new_file = f'{base}.mp3'
            os.rename(out_file, new_file)

def audioCutter(file, start, end, boolean):

    # reading the file
    try:
        audio = AudioSegment.from_file(file, format="mp4")
    except Exception:
        audio = AudioSegment.from_file(file, format="mp3")
    # time in milliseconds
    start = start*1000
    end = end*1000

    # cutted audio with start and end time
    cutted = audio[start: end]

    # audio export to mp3
    cutted.export("cuttedAudio.mp3", format="mp3")

    if boolean:
        os.remove(file)

def windowHome():
    layoutHome = [
        [sg.Push(), sg.Button('YT link downloader', size=(80, 2), pad=(0, (10, 0))), sg.Push()],
        [sg.Push(), sg.Button('YT downloader and cutter',pad=(0, (10, 0)), size=(80, 2)), sg.Push()],
        [sg.Push(), sg.Button('mp3 file cutter', pad=(0, (10, 0)), size=(80, 2)), sg.Push()]
    ]
    windowHomeL = sg.Window('Downloader Home', layoutHome, size=(300, 250))

    while True:
        events, values = windowHomeL.read()
        if events == sg.WINDOW_CLOSED:
            windowHomeL.close()
            return 3
        if events == 'YT link downloader':
            windowHomeL.close()
            return 0
        elif events == 'YT downloader and cutter':
            windowHomeL.close()
            return 1

        elif events == 'mp3 file cutter':
            windowHomeL.close()
            return 2
    windowHomeL = 0

def YTLinkdDownloader():
    layoutYTLinkdDownloader = [
        [sg.Push(), sg.Button('voltar'), sg.Text('YT link Downloader', font=('Helvetica bold', 30)), sg.Push()],
        [sg.Push(), sg.Input(key='link', size=(50, 2),font=('Helvetica bold', 15)), sg.Push()],
        [sg.Push(), sg.Button('Mp3', font=('Helvetica bold', 15), pad=(54, 15, 10), size=(10)),
         sg.Button('Mp4', font=('Helvetica bold', 15), pad=(70, 15, 0), size=(10)), sg.Push()],
    ]
    windowYT = sg.Window('YT link Downloader',layoutYTLinkdDownloader, size=(500, 300))
    while True:
        eventos, valores = windowYT.read()
        if eventos == sg.WINDOW_CLOSED:
            windowYT.close()
            del windowYT
            break
        if eventos == 'Mp3':
            downloadVideo(valores['link'], True)
        if eventos == 'Mp4':
            downloadVideo(valores['link'], False)

        if eventos == 'voltar':
            windowYT.close()
            del windowYT
            break
    windowYT = 0

# janela downloader and cutter

def downloaderCutter():
    layoutDownloadCutter = [
        [sg.Push(), sg.Button('voltar'), sg.Text('YT downloader and cutter', font=('Helvetica bold', 25)), sg.Push()],
        [sg.Push(), sg.Input(key='link', size=(50, 2),font=('Helvetica bold', 15)), sg.Push()],
        [sg.Push(), sg.Input(key='inicio', font=('Helvetica bold', 13), pad=(70, 15, 10), size=(10)), sg.Input(key='fim', font=('Helvetica bold', 13), pad=(70, 15, 0), size=(10)), sg.Push()],
        [sg.Push(), sg.Text('Inicio', font=('Helvetica bold', 15), pad=(97, 0, 0), size=(10)),
         sg.Text('Fim', font=('Helvetica bold', 15), pad=(25, 0, 0), size=(10)), sg.Push()],
        [sg.Push(), sg.Button('cortar', font=('Helvetica bold', 20)), sg.Push()]
    ]
    windowYTCut = sg.Window('Downloader Cutter',layoutDownloadCutter, size=(500, 300))

    while True:
        eventos, valores = windowYTCut.read()
        if eventos == sg.WINDOW_CLOSED:
            windowYTCut.close()
            del windowYTCut
            break
        if eventos == 'cortar':
            link = (valores['link'])
            start = onlyInt((valores['inicio']))
            end = onlyInt((valores['fim']))
            if type(start) == int and type(end) == int:
                file = downloadVideo(link, False)
                audioCutter(file, start, end, True)
        if eventos == 'voltar':
            windowYTCut.close()
            del windowYTCut
            break
    windowYTCut = 0


def Cutter():

    layoutCutter = [
        [sg.Push(), sg.Button('voltar'), sg.Text('Audio cutter', font=('Helvetica bold', 25)), sg.Push()],
        [sg.Push(), sg.Input(key='file', default_text='', size=(25, 2),font=('Helvetica bold', 15)), sg.Button('↓'), sg.Push()],
        [sg.Push(), sg.Input(key='inicio', font=('Helvetica bold', 13), pad=(70, 15, 10), size=(10)), sg.Input(key='fim', font=('Helvetica bold', 13), pad=(70, 15, 0), size=(10)), sg.Push()],
        [sg.Push(), sg.Text('Inicio', font=('Helvetica bold', 15), pad=(97, 0, 0), size=(10)),sg.Text('Fim', font=('Helvetica bold', 15), pad=(25, 0, 0), size=(10)), sg.Push()],
        [sg.Push(), sg.Button('cortar', font=('Helvetica bold', 20)), sg.Push()]
    ]
    windowCut = sg.Window('Audio cutter', layoutCutter)

    while True:
        eventos, valores = windowCut.read()
        
        if eventos == sg.WINDOW_CLOSED:
            windowCut.close()
            del windowCut
            break
        if eventos == 'cortar':

            start = onlyInt((valores['inicio']))
            end = onlyInt((valores['fim']))
            if type(start) == int and type(end) == int:
                audioCutter(file, start, end, False)
        if eventos == 'voltar':
            windowCut.close()
            del windowCut
            break
        if eventos == '↓':
            file = askopenfilename()
            windowCut['file'].update(value=file)
    windowCut = 0


while True:

    windowContent = windowHome()
    if windowContent == 0:
        YTLinkdDownloader()
    elif windowContent == 1:
        downloaderCutter()
    elif windowContent == 2:
        Cutter()
    elif windowContent == 3:
        break
    