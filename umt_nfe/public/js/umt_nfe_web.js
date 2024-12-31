frappe.ready(function() {
    // Initialize tooltips
    $('[data-toggle="tooltip"]').tooltip();

    // Add animation class to cards
    $('.card').addClass('animate-fade-in');

    // Smooth scroll for anchor links
    $('a[href*="#"]').on('click', function(e) {
        if (this.hash !== '') {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 70
            }, 500);
        }
    });

    // Search functionality
    $('#searchInput').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        $(".searchable").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    // Mobile menu toggle
    $('.navbar-toggler').on('click', function() {
        $('.navbar-collapse').toggleClass('show');
    });

    // Add active class to current nav item
    $('.nav-link').each(function() {
        if (window.location.pathname === $(this).attr('href')) {
            $(this).addClass('active');
        }
    });

    // Back to top button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#backToTop').fadeIn();
        } else {
            $('#backToTop').fadeOut();
        }
    });

    $('#backToTop').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 500);
        return false;
    });
});
