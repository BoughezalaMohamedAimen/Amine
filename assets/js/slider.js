$(document).ready(function(){
  var slides=$('.custom-slide').length;
  var active=1;
  autoplay();
  function autoplay(){

    $('.active-slide').removeClass('active-slide');
    $('.active-caption').removeClass('active-caption');
    $('.active-button').removeClass('active-button');
    active=(active==slides) ? 1 : active+1;
    $('.custom-slide'+active).addClass('active-slide');
    setTimeout(function(){
      $('.active-slide').find('h1,h3').addClass('active-caption');
      $('.active-slide').find('.button').addClass('active-button');
    },500)
    setTimeout(function(){autoplay();},5000)

  }
});
