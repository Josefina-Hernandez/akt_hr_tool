import openpyxl as xl
import pandas as pd
import numpy as np
import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter import simpledialog


# เลือกโฟลเดอร์ของไฟล์เวลา
def get_folder_path():
    ROOT = tk.Tk()

    ROOT.withdraw()
    folder_path = simpledialog.askstring(title="Test",
                                         prompt="Please input folder path of the OT Sheet files")
    return folder_path


folder_path = get_folder_path()

# อ่านไฟล์จากโฟลเดอร์ที่เลือก
os.chdir(folder_path)  # เอาโปรแกรมมาอยู่ในโฟลเดอร์ที่จะทำงาน

all_file = os.listdir(folder_path)

os.getcwd()  # Checkว่าอยู่ถูกที่ไหม


def result_df(i_file):
    # เลือกไฟล์ตาม i_file
    xls = pd.ExcelFile(all_file[i_file])
    # สร้างsheet_countของไฟล์นั้นๆ
    sheet_count = len(xls.sheet_names)
    # IndicatorสำหรับLoopชีท
    i = 0
    # Set for holding sheet

    member = []
    hour = []

    while i < sheet_count:
    #for i in range(0, sheet_count):
        dataframe = pd.read_excel(xls, i)
        #ここでdataframeは空白か？フォーマット間違えるか？を判断したほうがいい

        # รหัสพนักงานรอบเดียว
        m = dataframe.iloc[1][2]
        print('-------------------->',all_file[i_file], i, m) #デバッグのために追加する行
        # TimeHolder for each one
        h = 0
        # Dataเวลาเริ่มจากRow 6
        x = 6
        # TimeHolder for sum
        h_collected = []
        i_kojin = 0
        while i_kojin < 34:
            #try:　ここでformatが正しくないsheetや、変なsheetまたは空白sheetがあればエラーが起こる、try...except..という組合の使用を推薦
            h = (dataframe.iloc[x][14])
            #except IndexError:
                #continue

            #ここでhの値を判断したほうがいい：数字または"nan"か？、YES->そのまま、NO->数字"0"に変更
            h_collected.append(h)
            x += 1
            i_kojin += 1
            try: #ＶＢ言語のon error goto...と等しい、gotoする場所は次の"except"の中の内容である
                h_sum = round(np.nansum(h_collected), 2)
            except:
                print(h_collected)  #h_collectedというlistの中の各値を確認（スペースがある？数字じゃないセルが存在する？）
                raise ValueError #プログラムを停止させる

        member.append(m)
        hour.append(h_sum)

        i += 1
    month = (dataframe.iloc[2][2])
    df = pd.DataFrame()
    df[month] = member
    df['Total_Hour'] = hour
    return df


final = result_df(0)
i = 1
while i <= (len(all_file)) - 1:
    final = pd.concat([final, result_df(i)], axis=1)
    i += 1


ROOT = tk.Tk()

ROOT.withdraw()
path = simpledialog.askstring(title="Test",
                              prompt="Please select folder destination")
name = simpledialog.askstring(title="Test",
                              prompt="Please select file name")
final.to_csv(os.path.join(path, name + '.csv'))