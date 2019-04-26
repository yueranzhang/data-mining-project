from tkinter import *


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
        path_entry = Entry(self.tk)
        path_entry.place(x=300, y=300)

        # upload按钮
        upload_button = Button(self.tk, text='upload', bg='sky blue', command=self.input_window)
        upload_button.place(x=500, y=300)

        # show按钮
        show_button = Button(self.tk, text='show', bg='sky blue', command=self.show_window)
        show_button.place(x=500, y=350)

        # 输入最下方文本
        text = Text(self.tk, height=2)
        text.place(x=100, y=500)
        text.insert(END, 'This tool can help you to match cloths based on your input images. Input: upload image. '
                              'Output: output image')

    def start(self):
        self.tk.mainloop()

    def show_window(self):
        s_window = Toplevel()
        s_window.title('Result')

    def input_window(self):
        i_window = Toplevel()
        i_window.title('input path')


if __name__ == '__main__':
    NewGUI = GUI()
    NewGUI.start()
