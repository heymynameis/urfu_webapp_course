import streamlit as st
from transformers import pipeline
from io import StringIO

pipe = pipeline("question-answering", model="AndrewChar/model-QA-5-epoch-RU")
title_questions = 'Выберите файл txt вопросов'
title_true_answers = 'Выберите файл txt верных ответов'
title_answers = 'Выберите файл txt ответов студента'

def answer_count(questions, true_answers, answers, minratio = 75):
    from thefuzz import fuzz
    correct_answers = 0
    answer_count = len(answers)
    for q, a, ta in zip(questions, answers, true_answers):
        if fuzz.ratio(pipe(q,a)['answer'].lower(), ta) >= 75:
            correct_answers += 1
    return answer_count, correct_answers

def read_file_lines_str(title):
    uploaded_file = st.file_uploader(label=title)
    str_out = ''
    if uploaded_file:
        stringio = StringIO(uploaded_file.getvalue().decode('utf8'))
        str_out = stringio.read()
    return str_out.split('\n')

st.title('Автоматическая проверка ответов')
st.write("Прикрепите файлы для анализа, каждый ответ/вопрос с новой строки")

questions = read_file_lines_str(title_questions)
true_answers = read_file_lines_str(title_true_answers)
answers = read_file_lines_str(title_answers)
min_ratio = st.text_input('Введите допустимый процент схожести ответа студента с верным ответом')

if min_ratio and questions and true_answers and answers:
    min_ratio = int(min_ratio)
    result = st.button('Проанализировать файл ответов')
    if result:
        answer_count, correct_answers = answer_count(questions, true_answers, answers, min_ratio)
        st.write("Верных/всего ответов: ", correct_answers, "/", answer_count)
        st.write("Процент верных ответов: ", round(100*correct_answers/answer_count))
else: st.write("Выберите все файлы и укажите допустимый процент для продолжения")