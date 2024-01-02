
  
/*=============== CHANGE BACKGROUND HEADER ===============*/
// function scrollHeader() {
//     const header = document.getElementById('header');
    
//     // Check if the scroll position is greater than or equal to 50 viewport height
//     if (window.scrollY >= 50) {
//         header.classList.add('scroll-header');
//     } else {
//         // If not, remove the 'scroll-header' class
//         header.classList.remove('scroll-header');
//     }
// }

// window.addEventListener('scroll', scrollHeader);


function scrollHeader() {
    const header = document.getElementById('header');

    // Check if the scroll position is greater than or equal to 50 viewport height
    if (window.scrollY >= 50) {
        header.classList.add('scroll-header');
    } else {
        // If not, remove the 'scroll-header' class
        header.classList.remove('scroll-header');
    }
}

function removeScrollHeaderOnUnload() {
    const header = document.getElementById('header');
    header.classList.remove('scroll-header');
}

window.addEventListener('scroll', scrollHeader);

// Add a listener to remove the scroll-header class when navigating away from the page
window.addEventListener('beforeunload', removeScrollHeaderOnUnload);


/*=============== SWIPER POPULAR ===============*/
var swiperpopular__container = new Swiper(".popular__container", {
    spaceBetween: 32,
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});


/*=============== VALUE ACCORDION ===============*/
const accordionItems = document.querySelectorAll('.value__accordion-item');
let lastScrollTop = 0;
let currentlyOpenItem = null;

window.addEventListener('scroll', () => {
    handleScroll();
});

accordionItems.forEach((item) => {
    const accordionHeader = item.querySelector('.value__accordion-header');

    accordionHeader.addEventListener('click', () => {
        toggleAccordion(item);
    });
});

function handleScroll() {
    const st = window.scrollY || document.documentElement.scrollTop;

    // Check if the scroll direction has changed
    const isScrollingDown = st > lastScrollTop;

    // Open the next item that comes into view
    accordionItems.forEach((item) => {
        const itemTop = item.getBoundingClientRect().top;

        if (itemTop < window.innerHeight / 2 && !item.classList.contains('accordion-open')) {
            openAccordion(item);
        }
    });

    // Close the currently open item when scrolling in the opposite direction
    if (!isScrollingDown && currentlyOpenItem) {
        closeAccordion(currentlyOpenItem);
    }

    lastScrollTop = st;
}

function openAccordion(item) {
    const accordionContent = item.querySelector('.value__accordion-content');
    
    // Close the currently open item
    if (currentlyOpenItem) {
        closeAccordion(currentlyOpenItem);
    }

    // Open the clicked item with a faster transition
    accordionContent.style.transition = 'height 0.15s ease-in-out';
    accordionContent.style.height = accordionContent.scrollHeight + 'px';

    item.classList.add('accordion-open');
    currentlyOpenItem = item;

    // Reset transition property after animation
    setTimeout(() => {
        accordionContent.style.transition = '';
    }, 150);
}

function closeAccordion(item) {
    const accordionContent = item.querySelector('.value__accordion-content');
    
    // Close the item with a faster transition
    accordionContent.style.transition = 'height 0.15s ease-in-out';
    accordionContent.style.height = 0;

    item.classList.remove('accordion-open');
    currentlyOpenItem = null;

    // Reset transition property after animation
    setTimeout(() => {
        accordionContent.style.transition = '';
    }, 150);
}

function toggleAccordion(item) {
    if (item.classList.contains('accordion-open')) {
        closeAccordion(item);
    } else {
        openAccordion(item);
    }
}


/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/


// window.addEventListener('scroll', scrollActive);
document.addEventListener("DOMContentLoaded", function () {
    // Function to update active link
    function updateActiveLink(clickedLink) {
        // Remove the "active-link" class from all navigation links
        document.querySelectorAll('.nav__menu a.nav__link').forEach(link => {
            link.classList.remove('active-link');
        });

        // Add the "active-link" class to the clicked navigation link
        clickedLink.classList.add('active-link');
    }

    // Event listener for click on navigation links
    document.querySelectorAll('.nav__menu a.nav__link').forEach(link => {
        link.addEventListener('click', function () {
            updateActiveLink(this);
        });
    });
});

/*=============== SHOW SCROLL UP ===============*/ 
function scrollUp() {
    const scrollUp = document.getElementById('scroll-up');

    if (window.scrollY >= 350) {
        scrollUp.classList.add('show-scroll');
    } else {
        scrollUp.classList.remove('show-scroll');
    }
}

window.addEventListener('scroll', scrollUp);

/*=============== DARK LIGHT THEME ===============*/ 
const themeButton = document.getElementById('theme-button');
const darkTheme = 'dark-theme';
const iconTheme = 'bx-sun';

const selectedTheme = localStorage.getItem('selected-theme');
const selectedIcon = localStorage.getItem('selected-icon');

const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx bx-moon' : 'bx bx-sun';

if (selectedTheme) {
    document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
    themeButton.classList[selectedIcon === 'bx bx-moon' ? 'add' : 'remove'](iconTheme);
}

themeButton.addEventListener('click', () => {
    document.body.classList.toggle(darkTheme);
    themeButton.classList.toggle(iconTheme);

    localStorage.setItem('selected-theme', getCurrentTheme());
    localStorage.setItem('selected-icon', getCurrentIcon());
});


/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,
    // reset: true
});

sr.reveal('.home__title, .popular__container, .register__container, .footer__container');
sr.reveal('.home__description, .footer__info', { delay: 500 });
sr.reveal('.home__search', { delay: 600 });
sr.reveal('.home__value', { delay: 700 });
sr.reveal('.home__images', { origin: 'left' });
sr.reveal('.value__content, .contact__images', { origin: 'right' });
sr.reveal('.value__images, .contact__content', { origin: 'bottom'});
sr.reveal(`.notfound__data`, {origin: 'top', delay: 400})
sr.reveal(`.notfound__img`, {origin: 'bottom', delay: 600})