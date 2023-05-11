const btnRespond = document.getElementById('respond');
const respondField = document.getElementById('myElement');
const cancelRespond = document.getElementById('cancel-respond');
const btnSendRespond = document.getElementById('send-respond');
const inputField = document.getElementById('my-textarea');
const blockResponses = document.getElementById('block-responses');
blockResponses.hidden = false;

btnRespond.addEventListener('click', function () {
    blockResponses.hidden = true;
    btnRespond.disabled = true;
    respondField.hidden = false;
})

// cancelRespond.addEventListener('click', function () {
//     blockResponses.hidden = false;
//     respondField.hidden = true;
//     btnRespond.disabled = false;
// })

// btnSendRespond.addEventListener('click', function () {
//     blockResponses.hidden = false;
//     respondField.hidden = true;
//     btnRespond.disabled = false;
// })