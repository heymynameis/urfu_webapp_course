from webaiapp import answer_count, pipe
def test_import():
    assert str(pipe).split()[0] == '<transformers.pipelines.question_answering.QuestionAnsweringPipeline'
def test_answer_count():
    questions = ["Какой вход усилителя используют для обратной связи?", "Какое сопротивление проявляется при переменном токе?"]
    answers = [
        """У операционного усилителя два входа - инвертирующий и неинвертирующий. 
        Инвертирующий чаще всего используют для обратной связи.""", 
        """"Существуют два вида сопротивления в зависимости от типа тока - активное и реактивное. 
        При переменном проявляется реактивное сопротивление."""]
    true_answers = ["инвертирующий", "реактивное"]
    assert answer_count(questions, true_answers, answers) == (2, 2)
    assert answer_count(questions, true_answers, answers, 100) == (2, 2)
