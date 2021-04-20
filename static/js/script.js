
const toggleBtn = document.getElementById('tgb1');
const mainNav = document.getElementById('mn1');


toggleBtn.addEventListener('click', () => {
    mainNav.classList.toggle('active');
});



const toggleModal = () =>{
    document.querySelector('.modal')
    .classList.toggle('show')
};

document.querySelector('.modal_btn')
    .addEventListener('click', toggleModal);


document.querySelector('#contact-form')
    .addEventListener('submit', (event) =>{
        event.preventDefault();
        toggleModal();
    });

    /*
document.getElementById('submit-btn')
    .addEventListener('submit', (event) =>{
        event.preventDefault();
        toggleModal();
    });

*/
