(function($) {
    $(function() {

        $('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240
      edge: 'right', // Choose the horizontal origin
      closeOnClick: true // Closes side-nav on <a> clicks, useful for Angular/Meteor
    });
        $('.parallax').parallax();
        $('.scrollspy').scrollSpy();
        $('.modal-trigger').leanModal();
    }); // end of document ready
})(jQuery); // end of jQuery name space
