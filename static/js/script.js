
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

    var mybutton = document.getElementById("myBtn");

    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }