const btnRespond = document.getElementById('respond');
const respondField = document.getElementById('myElement');
const cancelRespond = document.getElementById('cancel-respond');
const blockResponses = document.getElementById('block-responses');

blockResponses.hidden = false;

btnRespond.addEventListener('click', function () {
    blockResponses.hidden = true;
    btnRespond.disabled = true;
    respondField.hidden = false;
})

cancelRespond.addEventListener('click', function () {
    blockResponses.hidden = false;
    respondField.hidden = true;
    btnRespond.disabled = false;
})

const btnAnswerList1 = document.querySelectorAll('.btn_answer1');
const formAnswerList1 = document.querySelectorAll('.form_answer1');

btnAnswerList1.forEach(function (btnAnswer1) {
    btnAnswer1.addEventListener('click', function () {
        const respondId1 = btnAnswer1.dataset.respondId;
        const formAnswer1 = document.querySelector('.form_answer1[data-respond-id="' + respondId1 + '"]');

        btnAnswer1.hidden = true;
        formAnswer1.hidden = false;
    });
});

const answerBackList1 = document.querySelectorAll('.answer_back1');

answerBackList1.forEach(function (answerBack1) {
    answerBack1.addEventListener('click', function () {
        const respondId1 = answerBack1.dataset.respondId;
        const btnAnswer1 = document.querySelector('.btn_answer1[data-respond-id="' + respondId1 + '"]');
        const formAnswer1 = document.querySelector('.form_answer1[data-respond-id="' + respondId1 + '"]');

        btnAnswer1.hidden = false;
        formAnswer1.hidden = true;
    });
});

const btnAnswerList = document.querySelectorAll('.btn_answer2');
const formAnswerList = document.querySelectorAll('.form_answer2');

btnAnswerList.forEach(function (btnAnswer) {
    btnAnswer.addEventListener('click', function () {
        const answerId = btnAnswer.dataset.answerId;
        const formAnswer = document.querySelector('.form_answer2[data-answer-id="' + answerId + '"]');

        btnAnswer.hidden = true;
        formAnswer.hidden = false;
    });
});

const answerBackList = document.querySelectorAll('.answer_back2');

answerBackList.forEach(function (answerBack) {
    answerBack.addEventListener('click', function () {
        const answerId = answerBack.dataset.answerId;
        const btnAnswer = document.querySelector('.btn_answer2[data-answer-id="' + answerId + '"]');
        const formAnswer = document.querySelector('.form_answer2[data-answer-id="' + answerId + '"]');

        btnAnswer.hidden = false;
        formAnswer.hidden = true;
    });
});

