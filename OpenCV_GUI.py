from tkinter import *

import cv2 as cv
from PIL import Image, ImageTk
from shopping_link import *
from tkinter.filedialog import askopenfilename

import compare_img


class GUI():
    def __init__(self):
        self.tk = Tk()
        # 标题
        self.tk.title('OpenCV')
        # 大小
        self.tk.geometry('800x600')
        # 右侧图片
        self.logo = PhotoImage(file='image1.gif')
        textLabel = Label(self.tk, image=self.logo)
        textLabel.place(x=100, y=0)

        # 输入lable
        input_label = Label(self.tk, text='Please input a file path', bg='sky blue', font=(44))
        input_label.place(x=110, y=300)

        # 文件路径entry
        self.path_entry = Entry(self.tk)
        self.path_entry.place(x=300, y=300)
        # upload按钮
        upload_button = Button(self.tk, text='upload', bg='sky blue', command = self.selectPath)
        upload_button.place(x=500, y=300)
        self.path = StringVar()

        # show1按钮
        show_button_1 = Button(self.tk, text='cloth-pants', bg='sky blue', command=self.show_window_1)
        show_button_1.place(x=500, y=350)

        # show2按钮
        show_button_2 = Button(self.tk, text='cloth-shoes', bg='sky blue', command=self.show_window_2)
        show_button_2.place(x=500, y=400)

        # 输入最下方文本
        text = Text(self.tk, height=2)
        text.place(x=100, y=500)
        text.insert(END, 'This tool can help you to match cloths based on your input images. Input: upload image. '
                         'Output: output image')

    def start(self):
        self.tk.mainloop()

    def show_window_1(self):
        img = self.path_entry.get()
        best_cloth = compare_img.main(img)
        f = open("clothes_match_labeled_data.txt", "r", encoding="utf-8")
        for line in f:
            if best_cloth in line:
                predict = line.split(':[')[-1].split(',')[0]
                if predict[-2] == ']':
                    predict = predict[:-2]
                break
        # 输出结果的图片
        result_im = Image.open("my_training_shirts/" + predict + ".jpg")
        self.result_img_pants = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.title('Result')
        s_window.geometry('600x400')
        Label(s_window, text='your result is:').place(x=10, y=10)
        Label(s_window, image=self.result_img_pants).place(x=10, y=30)
        Label(s_window, text='The link is:').place(x=200, y=10)
        dic = get_link()
        link = dic[predict + '.jpg']
        Label(s_window, text=link).place(x=200, y=30)

    def show_window_2(self):
        img = self.path_entry.get()
        best_cloth = compare_img.main(img)
        f = open("clothes_match_labeled_data_2.txt", "r", encoding="utf-8")
        for line in f:
            if best_cloth in line:
                predict = line.split(': [')[-1].split(',')[0]
                if predict[-2] == ']':
                    predict = predict[:-2]
                break
        # 输出结果的图片
        result_im = Image.open("my_training_shirts/" + predict + ".jpg")
        self.result_img_shoes = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.title('Result')
        s_window.geometry('600x400')
        Label(s_window, text='your result is:').place(x=10, y=10)
        Label(s_window, image=self.result_img_shoes).place(x=10, y=30)
        Label(s_window, text='The link is:').place(x=200, y=10)
        dic = get_link()
        link = dic[predict + '.jpg']
        Label(s_window, text=link).place(x=200, y=30)

    def selectPath(self):
        path_ = askopenfilename()
        self.path.set(path_)
        self.path_entry.delete(0,'end')
        self.path_entry.insert(END,str(path_))
        


if __name__ == '__main__':
    NewGUI = GUI()
    NewGUI.start()
