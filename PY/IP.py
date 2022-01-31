import requests
from requests.structures import CaseInsensitiveDict
import webview
from tkinter import *


def geo(resp_dic=None, latitude=None, longitude=None):
    webview.create_window(resp_dic['ip'],
                          f'https://api.maptiler.com/maps/basic/?key=sTjsjRs9F3j7zqgA2aI6#12/{latitude}/{longitude}')
    webview.start()


def main():
    ip = "https://api.geoapify.com/v1/ipinfo?&apiKey=4e9a19bda1f94bed9b57f7ff04b82a6c"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(ip, headers=headers)
    resp_dic = resp.json()
    location = resp_dic['location']

    print(resp_dic['ip'])
    print(location['latitude'])
    print(location['longitude'])

    window = Tk()
    window.title("App")
    icon = PhotoImage(file='logo.png')
    window.iconphoto(True, icon)

    titLabel = Label(window, text="App", font=("Arial", 15))
    titLabel.place(relx=0.5, rely=0.0, anchor=N)

    latitude = location["latitude"]
    longitude = location["longitude"]

    butt = Button(window, text="Hello", command=None, height="2", width="8")
    butt.place(relx=0.0, rely=1.0, anchor=SW)

    butt = Button(window, text="Location", command=lambda: geo(resp_dic, latitude, longitude), height="2", width="8")
    butt.place(relx=1.0, rely=1.0, anchor=SE)

    window.mainloop()


if __name__ == '__main__':
    main()
