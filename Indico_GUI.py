from tkinter import *
import cv2 as cv
import indicoio
from indicoio.custom import Collection
from PIL import Image,ImageTk
from shopping_link import *
from tkinter.filedialog import askopenfilename

class GUI():
    def __init__(self):
        self.tk = Tk()
        # title
        self.tk.title('Indico')
        # size
        self.tk.geometry('800x600')
        # img on the right
        self.logo = PhotoImage(file='image1.gif')
        textLabel = Label(self.tk, image=self.logo)
        textLabel.place(x=100, y=0)

        # entry lable
        input_label = Label(self.tk, text='Please input a file path', bg='sky blue', font=(44))
        input_label.place(x=110, y=300)

        # file entry
        self.path_entry = Entry(self.tk)
        self.path_entry.place(x=300, y=300)
        # upload button
        upload_button = Button(self.tk, text='upload', bg='sky blue', command = self.selectPath)
        upload_button.place(x=500, y=300)
        self.path = StringVar()


        # show1
        show_button_1 = Button(self.tk, text='cloth-pants', bg='sky blue', command=self.show_window_1)
        show_button_1.place(x=500, y=350)

        # show2
        show_button_2 = Button(self.tk, text='cloth-shoes', bg='sky blue', command=self.show_window_2)
        show_button_2.place(x=500, y=400)

        # text in the bttom
        text = Text(self.tk, height=2)
        text.place(x=100, y=500)
        text.insert(END, 'This tool can help you to match cloths based on your input images. Input: upload image. '
                         'Output: output image')




    def start(self):
        self.tk.mainloop()

    def show_window_1(self):
        # indico
        indicoio.config.api_key = 'bb2ce29a2086bceb98bc297f6a961656'
        img = cv.imread(self.path_entry.get())
        collection = Collection("clothes_collection_2")
        predict = collection.predict(img)
        outcome = max(predict, key=predict.get)
        outcome = outcome[5:]
        print(outcome)
        # result img
        result_im = Image.open("my_training_shirts/"+outcome+".jpg")
        self.result_img = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.geometry('600x400')
        s_window.title('Result')
        Label(s_window, text='your result is:').place(x=10,y=10)
        Label(s_window, image=self.result_img).place(x=10,y=30)
        Label(s_window, text='The link is:').place(x=200, y=10)
        dic = get_link()
        link = dic[outcome + '.jpg']
        Label(s_window, text=link).place(x=200, y=30)

    def show_window_2(self):
        # indico
        indicoio.config.api_key = 'bb2ce29a2086bceb98bc297f6a961656'
        img = cv.imread(self.path_entry.get())
        collection = Collection("clothes_collection_1")
        predict = collection.predict(img)
        outcome = max(predict, key=predict.get)
        outcome = outcome[5:]
        # result img
        result_im = Image.open("my_training_shirts/"+outcome+".jpg")
        self.result_img = ImageTk.PhotoImage(result_im)

        s_window = Toplevel()
        s_window.geometry('600x400')
        s_window.title('Result')
        Label(s_window, text='your result is:').place(x=10,y=10)
        Label(s_window, image=self.result_img).place(x=10,y=30)
        Label(s_window, text='The link is:').place(x=200, y=10)
        dic = get_link()
        link = dic[outcome+'.jpg']
        Label(s_window, text=link).place(x=200, y=30)

    def selectPath(self):
        path_ = askopenfilename()
        self.path.set(path_)
        self.path_entry.delete(0,'end')
        self.path_entry.insert(END,str(path_))



if __name__ == '__main__':
    NewGUI = GUI()
    NewGUI.start()
