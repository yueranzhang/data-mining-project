from tkinter import *
import cv2 as cv
import indicoio
from indicoio.custom import Collection
from PIL import Image,ImageTk

class GUI():
    def __init__(self):
        self.tk = Tk()  # 实例化
        # 标题
        self.tk.title('clothing matching system')
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
        upload_button = Button(self.tk, text='upload', bg='sky blue')
        upload_button.place(x=500, y=300)

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
        # indico
        indicoio.config.api_key = 'bb2ce29a2086bceb98bc297f6a961656'
        img = cv.imread("/Users/yueranzhang/Desktop/"+self.path_entry.get())
        collection = Collection("clothes_collection_2")
        predict = collection.predict(img)
        outcome = max(predict, key=predict.get)
        outcome = outcome[5:]
        # 输出结果的图片
        result_im = Image.open("my_training_shirts/"+outcome+".jpg")
        self.result_img = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.title('Result')
        Label(s_window, text='your result is:').place(x=10,y=10)
        Label(s_window, image=self.result_img).place(x=10,y=30)

    def show_window_2(self):
        # indico
        indicoio.config.api_key = 'bb2ce29a2086bceb98bc297f6a961656'
        img = cv.imread("/Users/yueranzhang/Desktop/"+self.path_entry.get())
        collection = Collection("clothes_collection_1")
        predict = collection.predict(img)
        outcome = max(predict, key=predict.get)
        outcome = outcome[5:]
        # 输出结果的图片
        result_im = Image.open("my_training_shirts/"+outcome+".jpg")
        self.result_img = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.title('Result')
        Label(s_window, text='your result is:').place(x=10,y=10)
        Label(s_window, image=self.result_img).place(x=10,y=30)



if __name__ == '__main__':
    NewGUI = GUI()
    NewGUI.start()
