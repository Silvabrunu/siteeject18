$('.form-headsist').click(function(){
  
    if($(this).closest('.grop-fromsist').attr('id')=='signup'){
        $('.grop-fromsist').attr('id' , 'name');
        $('.icon-action').addClass('back');
    }  
    else if($(this).closest('.grop-fromsist').attr('id')=='success'){
          $('.grop-fromsist').attr('id' , 'signup');
          $('input').val('');
    }
    
});





$('.form-actionsist').click(function(){
 
    var form_id = $('.grop-fromsist').attr('id');
      $('.icon-action').addClass('back');
  
    if($('#control-' + form_id).val() != ''){
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
 
  $('.grop-fromsist').attr('id' , form_id);
  
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