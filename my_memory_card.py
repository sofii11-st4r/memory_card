from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint

class Question():
    #contiene la pregunta, una respuesta correcta y tres incorrectas
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('El idioma nacional de Brasil', 'Portugués', 'Brasilero', 'Español', 'Italiano'))
questions_list.append(Question('¿Qué color no aparece en la bandera de Estados Unidos?', 'Verde', 'Rojo', 'Blanco', 'Azul'))
questions_list.append(Question('Una residencia tradicional de los yakutos', 'Urasa', 'Yurta', 'Iglú', 'Choza'))

app = QApplication([])
btn_OK = QPushButton('Responder') 
lb_Question = QLabel('¡La pregunta más difícil del mundo!') 


RadioGroupBox = QGroupBox("Opciones de respuesta")


rbtn_1 = QRadioButton('Opción 1')
rbtn_2 = QRadioButton('Opción 2')
rbtn_3 = QRadioButton('Opción 3')
rbtn_4 = QRadioButton('Opción 4')


RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Resultado de prueba")
lb_Result = QLabel('¿Es correcto o no?') 
lb_Correct = QLabel('¡Aquí estará la respuesta!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # este botón debería ser grande
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # espaciando el contenido
# ----------------------------------------------------------
# Los widgets y bocetos han sido creados. Luego, las funciones: 
# ----------------------------------------------------------


def show_result():
    ''' mostrar panel de respuesta '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Siguiente pregunta')


def show_question():
    ''' mostrar panel de pregunta '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Responder')
    RadioGroup.setExclusive(False) # remover límites para poder reiniciar la selección del botón de radio
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # regresa los límites para que solo un botón de radio pueda ser seleccionado 

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers) #barajea la lista de botones, ahora un boton aleatorio es el primero
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    #mostrar el resultado, colocar el texto que fue pasado en la etiqueta resultado
    lb_Result.setText(res)
    show_result()
def check_answer():
    # revisar si la opción de respuesta seleccionada es correcta
    if answers[0].isChecked():
        #respuesta correcta
        show_correct("Correcto")
        window.score += 1
        print("Estadísticas \n -Preguntas totales:", window.total, "\n-Preguntas correctas: ")
        print("Calificación: ", (window.score / window.total * 100), "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrecto")
            print("Calificación: ", (window.score / window.total * 100), "%")

def next_question():
    #Realizar la siguiente pregunta
    window.total += 1
    print("Estadísticas \n -Preguntas totales:", window.total, "\n-Preguntas correctas: ")
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == "Responder":
        check_answer()
    else:
        next_question()

def test():
    ''' una función temporal que hace que sea posible presionar un botón para llamar y alternar show_result() o show_question() '''
    if 'Responder' == btn_OK.text():
        show_result()
    else:
        show_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Tarjeta de memoria')
window.cur_question = -1
btn_OK.clicked.connect(click_OK) # comprueba que el panel de respuesta aparezca cuando se presione el botón
window.score = 0
window.total = 0
next_question()
window.resize(400,300)
window.show()
app.exec()
