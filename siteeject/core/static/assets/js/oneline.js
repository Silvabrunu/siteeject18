$('.form-head').click(function(){
  var  id = $(this).closest('.grop-from.signup').attr('id');
  var id_array = ['signup_responsivos', 'signup_web', 'signup_hospedagem'];
  var index = $.inArray(id, id_array);

  if(index >= 0) {
      $('.grop-from#'+id_array[index]).attr('id' , 'name');
      $(this).children('.icon-action').addClass('back');
  } else if($(this).closest('.grop-from').attr('id')=='success'){
        $('.grop-from').attr('id' , 'signup');
        $('input').val('');
  }
    
});

$('.form-action').click(function(){
 
    var form_id = $(this).closest('.grop-from.signup').attr('id');
    $('.icon-action').addClass('back');
  
    if($('.control-' + form_id).val() != ''){
      switch (form_id) {
          case 'name':
              form_id = "phone";
              break;
          case "phone":
              form_id = "email";
              break;
          case "email":
              form_id = "success";
              break;   
        case "success":
              form_id = "signup";
              break; 
      }
       $('.icon-action').addClass('back');
      
  }
  
  else{
    
     switch (form_id) {
          case 'name':
              form_id = "signup";
              $('.icon-action').removeClass('back');
              break;
          case "phone":
              form_id = "name";
              break;
          case "email":
              form_id = "phone";
              break;
         case "success":
              form_id = "signup";
              break; 
      }
     $('.icon-action').removeClass('back');
  }
 
  $('.grop-from').attr('id' , form_id);
  
});

$('input').keyup(function(){
   $('.grop-from').removeClass('error');
    $('.error-text').fadeOut();
    
    if($(this).val()!=''){
      $('.icon-action').removeClass('back');
    }
  else{
    $('.icon-action').addClass('back');
  }
  
  
})