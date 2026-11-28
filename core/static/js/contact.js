// ============================================
// CONTACT PAGE SPECIFIC JAVASCRIPT
// ============================================

document.addEventListener("DOMContentLoaded", function () {

    // ===============================
    // Hide Django Messages After 5s
    // ===============================
    const ho = document.getElementById("ho");
    setTimeout(function () {
        if (ho) {
            ho.style.display = 'none';
        }
    }, 5000);



    // ===============================
    // FAQ Accordion
    // ===============================
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');

        if (question) {
            question.addEventListener('click', () => {

                faqItems.forEach(otherItem => {
                    if (otherItem !== item && otherItem.classList.contains('active')) {
                        otherItem.classList.remove('active');
                    }
                });

                item.classList.toggle('active');
            });
        }
    });

});

console.log('Contact page functionality loaded - Peaceful-Hostel');