from email import message
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import requests
import json

app = QApplication([])
win = QWidget()
win.setWindowTitle('Наш чат')
win.resize(800, 500)

vert_main = QVBoxLayout()
hor_down = QHBoxLayout()
hor_up = QHBoxLayout()
main_chat = QPlainTextEdit()
main_chat.setReadOnly(True)

login = QLineEdit('sitect')
login.setPlaceholderText('Логин')
password = QLineEdit('2580')
password.setPlaceholderText('Пароль')
name = QLineEdit('123')
name.setPlaceholderText('Имя')
msg = QLineEdit()
msg.setPlaceholderText('Сообщение...')

cap = QDialog()
v_cap = QVBoxLayout()
but_cap = QPushButton('Ответить')
def ans_cap():
    if answs_cap == k['captcha']:
        cap.close()
def send():
    global cap, answs_cap
    data1 = {'login': login.text(), 'password': password.text(), 'name': name.text(), 'message': msg.text(), 'captcha': captcha.text()}
    request_send = requests.post('http://algo.enotit.space/chatroom/send.php', data=data1).text
    print(request_send)
    k = json.loads(request_send)
    if "captcha" in k.keys():
        cap.setWindowTitle('Captcha')
        cap.resize(300, 150)
        quest_cap = QLabel(k['captcha'])
        answs_cap = QLineEdit()
        v_cap.addWidget(quest_cap)
        v_cap.addWidget(answs_cap)
        v_cap.addWidget(but_cap)
        cap.setLayout(v_cap)
        cap.show()
    print(request_send)

def update():
    text = ''
    data1 = {'login': login.text(), 'password': password.text()}
    request_take = requests.get('http://algo.enotit.space/chatroom/take.php', params=data1).text
    print(request_take)
    result = json.loads(request_take) 
    for i in result['messages']:
        print(i)
    text.split(request_take)
    print(data1)

update_btn = QPushButton('Обновить')
update_btn.clicked.connect(update)
send_btn = QPushButton('Отправить')
send_btn.clicked.connect(send)

hor_up.addWidget(login, alignment=Qt.AlignTop)
hor_up.addWidget(password, alignment=Qt.AlignTop)
hor_up.addWidget(name, alignment=Qt.AlignTop)

hor_down.addWidget(update_btn, alignment=Qt.AlignBottom)
hor_down.addWidget(msg, alignment=Qt.AlignBottom)
hor_down.addWidget(send_btn, alignment=Qt.AlignBottom)

vert_main.addLayout(hor_up)
vert_main.addLayout(hor_down)
vert_main.addWidget(main_chat)

win.setLayout(vert_main)
win.show()
app.exec_()
