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
        self.textLabel = Label(self.tk, image=self.logo)
        self.textLabel.place(x=100, y=0)

        # 输入lable
        self.input_label = Label(self.tk, text='Please input a file path', bg='sky blue', font=(44))
        self.input_label.place(x=110, y=300)

        # 文件路径entry
        self.path_entry = Entry(self.tk)
        self.path_entry.place(x=300, y=300)

        # upload按钮
        self.upload_button = Button(self.tk, text='upload', bg='sky blue', command=self.input_window)
        self.upload_button.place(x=500, y=300)

        # show按钮
        self.show_button = Button(self.tk, text='show', bg='sky blue', command=self.show_window)
        self.show_button.place(x=500, y=350)

        # 输入最下方文本
        self.text = Text(self.tk, height=2)
        self.text.place(x=100, y=500)
        self.text.insert(END, 'This tool can help you to match cloths based on your input images. Input: upload image. '
                              'Output: output image')

    def start(self):
        self.tk.mainloop()

    def show_window(self):
        self.s_window = Toplevel()
        self.s_window.title('Result')

    def input_window(self):
        self.i_window = Toplevel()
        self.i_window.title('input path')


if __name__ == '__main__':
    NewGUI = GUI()
    NewGUI.start()
