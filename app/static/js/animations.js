/**
 * Animation Utilities
 * Reusable animation functions for page elements
 */

// Intersection Observer for scroll animations
document.addEventListener('DOMContentLoaded', function () {
    // Elements to animate on scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    animatedElements.forEach(el => observer.observe(el));

    // Flash message auto-dismiss
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(() => msg.remove(), 300);
        }, 5000);
    });
});

// Smooth scroll to element
function scrollToElement(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Page transition effect
function pageTransition(url) {
    document.body.classList.add('page-exit');
    setTimeout(() => {
        window.location.href = url;
    }, 300);
}

// Number counter animation
function animateCounter(element, target, duration = 1000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.round(current).toLocaleString('en-IN');
    }, 16);
}

// Stagger animation for multiple elements
function staggerAnimation(elements, className, delay = 100) {
    elements.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add(className);
        }, index * delay);
    });
}
