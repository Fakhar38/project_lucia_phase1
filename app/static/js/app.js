$(document).ready( function(){
    $('.filter-button').click( function() {
        var toggleWidth = $(".filters-container").width() == "13.5vw" ? "0" : "13.5vw";
        $('.filters-container').animate({ width: toggleWidth });
        $('.filters-page').css({ display: "block" }); 
    });
    $('.close-filters-container').click( function() {
        var toggleWidth = $(".filters-container").width() == "0" ? "13.5vw" : "0";
        $('.filters-container').animate({ width: toggleWidth });
        $('.filters-page').css({ display: "none" }); 
    });
    $('.profile-picture-div ').click( function() {
        var toggleWidthPage = $(".login-page-container").width() == "50vw" ? "0" : "50vw";
        $('.login-page-container').animate({ width: toggleWidthPage });
        $('.login-page').css({ display: "block" });    
    });
    $('.close-login-page-container').click( function() {
        var toggleWidthPage = $(".login-page-container").width() == "0" ? "50vw" : "0";
        $('.login-page-container').animate({ width: toggleWidthPage });
        $('.login-page').css({ display: "none" });    
    });
    $('.home-page-image-gallery-container').click( function() {
        $('.login-page-container').animate({ width: "0" });
        $('.login-page').css({ display: "none" });    
    });
    $('.fa-clone').click( function() {
        $('.mobile-login-container').css({ display: "none" });    
        $('.mobile-container').css({ display: "block" });    
    });
    $('.profile-picture-div-mob').click( function() {
        $('.mobile-login-container').css({ display: "block" });    
        $('.mobile-container').css({ display: "none" });    
    });
});