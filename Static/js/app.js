$(document).ready( function(){
    $('.filter-button').click( function() {
        var toggleWidth = $(".filters-container").width() == "20vw" ? "0" : "20vw";
        $('.filters-container').animate({ width: toggleWidth });
    });
    $('.close-filters-container').click( function() {
        var toggleWidth = $(".filters-container").width() == "0" ? "20vw" : "0";
        $('.filters-container').animate({ width: toggleWidth });
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
});