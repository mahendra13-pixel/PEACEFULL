// ============================================
// BASE JS - Peaceful-Hostel
// Runs on every page via base.html
// ============================================


// Mobile Navigation Toggle
const mobileToggle = document.getElementById('mobileToggle');
const mobileNav = document.getElementById('mobileNav');
const closeMobile = document.getElementById('closeMobile');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        mobileNav.classList.add('active');
        document.body.style.overflow = 'hidden';
    });
}

if (closeMobile) {
    closeMobile.addEventListener('click', () => {
        mobileNav.classList.remove('active');
        document.body.style.overflow = '';
    });
}

// Close mobile nav when clicking outside
document.addEventListener('click', (e) => {
    if (mobileNav && mobileNav.classList.contains('active')) {
        if (!mobileNav.contains(e.target) && !mobileToggle.contains(e.target)) {
            mobileNav.classList.remove('active');
            document.body.style.overflow = '';
        }
    }
});


// Navbar Scroll Shadow Effect
const header = document.querySelector('.site-header');

window.addEventListener('scroll', () => {
    if (header) {
        if (window.pageYOffset > 100) {
            header.style.boxShadow = 'var(--shadow-md)';
        } else {
            header.style.boxShadow = 'var(--shadow-sm)';
        }
    }
});


// Smooth Scroll for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href !== '') {
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});


// Page Load Animation
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});


console.log('Base functionality loaded - Peaceful-Hostel');