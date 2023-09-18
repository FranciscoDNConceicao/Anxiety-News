import tkinter as tk
import pandas
from tkinter import font


def SentimentBad():
    global indexPosition
    NewsDataframe.loc[indexPosition, 'TRUE_SENTIMENT'] = "Negative"
    indexPosition = NewsDataframe[NewsDataframe['TRUE_SENTIMENT'] == 'Neutral'].index[0]
    labelTitle.configure(text=NewsDataframe.iloc[indexPosition][0])
    labelDesc.configure(text=NewsDataframe.iloc[indexPosition][4])
    print(indexPosition)


def SentimentGood():
    global indexPosition
    NewsDataframe.loc[indexPosition, 'TRUE_SENTIMENT'] = "Positive"
    indexPosition = NewsDataframe[NewsDataframe['TRUE_SENTIMENT'] == 'Neutral'].index[0]
    labelTitle.configure(text=NewsDataframe.iloc[indexPosition][0])
    labelDesc.configure(text=NewsDataframe.iloc[indexPosition][4])
    print(indexPosition)


NewsDataframe = pandas.read_csv(r"Data/train.csv")
NewsDataframe = NewsDataframe[NewsDataframe['TRUE_SENTIMENT'] == "Neutral"]

indexPosition = NewsDataframe[NewsDataframe['TRUE_SENTIMENT'] == 'Neutral'].index[0]
print(indexPosition)

window = tk.Tk()
window.geometry("1000x400")
window.configure(background="#292F33")

print(NewsDataframe.iloc[indexPosition][1])

titleFont = font.Font(family="Calibri", size=20, weight="bold")
descFont = font.Font(family="Calibri", size=15)
buttonFont = font.Font(family="Calibri", size=15, weight="bold")

labelTitle = tk.Label(window,
                      text=NewsDataframe.iloc[indexPosition][1],
                      fg="white",
                      bg="#292F33",
                      font=titleFont,
                      width=70,
                      wraplength=900
                      )
labelTitle.place(x=0, y=100)

print(NewsDataframe.iloc[indexPosition][3])
labelDesc = tk.Label(window,
                     text=NewsDataframe.iloc[indexPosition][3],
                     fg="white",
                     bg="#292F33",
                     font=descFont,
                     width=100,
                     wraplength=900
                     )
labelDesc.place(x=0, y=200)

buttonGood = tk.Button(
    window,
    text="Good",
    command=SentimentGood,
    bg="green",
    fg="white",
    width=15,
    height=2,
    font=buttonFont
)
buttonGood.place(x=300, y=300)
buttonBad = tk.Button(
    window,
    text="Bad",
    command=SentimentBad,
    bg="red",
    width=15,
    height=2,
    fg="white",
    font=buttonFont
)
buttonBad.place(x=600, y=300)
print(indexPosition)
window.mainloop()
print(NewsDataframe.head())
NewsDataframe.to_csv(r"Data/train.csv", index=False)
