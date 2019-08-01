$(document).ready(function(){

  /********************delete items*************************/
  $('.delete').click(function(e){
        e.preventDefault();
    if (confirm("Etes vous bien sur de vouloir suprimmer ")) {
        window.location.href = $(this).attr('href')
      } 
  })
})
