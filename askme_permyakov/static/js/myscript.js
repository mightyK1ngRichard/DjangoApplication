const btnRespond = document.getElementById('respond');
const respondField = document.getElementById('myElement');
const cancelRespond = document.getElementById('cancel-respond')
const btnSendRespond = document.getElementById('send-respond')

btnRespond.addEventListener('click', function () {
    btnRespond.disabled = true;
    respondField.hidden = false;
})

cancelRespond.addEventListener('click', function () {
    respondField.hidden = true;
    btnRespond.disabled = false;
})

btnSendRespond.addEventListener('click', function () {
    // TODO: сделать SQL INSERT
})