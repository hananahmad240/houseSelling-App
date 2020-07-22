// custom
const year = document.querySelector('.year');
const date = new Date();
year.innerHTML = date.getFullYear();

setTimeout(() => {
    $('#message').fadeOut('slow');
}, 3000);