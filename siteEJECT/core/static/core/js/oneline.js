var selectedService;

// $('.form-head').click(function(){

//     if($(this).closest('.grop-from').attr('id')=='signup'){
//         $('.grop-from').attr('id' , 'name');
//         $('.icon-action').addClass('back');
//     }  
//     else if($(this).closest('.grop-from').attr('id')=='success'){
//           $('.grop-from').attr('id' , 'signup');
//           $('input').val('');
//     }

// });

// $('.grop-from.signup').click(function(){
//     selectedService = $(this);

//     if($(this).closest('.grop-from').attr('id')=='signup'){
//         $('.grop-from').attr('id' , 'name');
//         $('.icon-action').addClass('back');
//     }  
//     else if($(this).closest('.grop-from').attr('id')=='success'){
//           $('.grop-from').attr('id' , 'signup');
//           $('input').val('');
//     }

// });





// $('.form-action').click(function(){

//     var form_class = $('.grop-from').attr('id');
//       $('.icon-action').addClass('back');

//     if($('#control-' + form_class).val() != ''){
//       switch (form_class) {
//           case 'name':
//               form_class = "phone";
//               break;
//           case "phone":
//               form_class = "email";
//               break;
//           case "email":
//               form_class = "success";
//               break;   
//         case "success":
//               form_class = "signup";
//               break; 
//       }
//        $('.icon-action').addClass('back');

//   }

//   else{

//      switch (form_class) {
//           case 'name':
//               form_class = "signup";
//               $('.icon-action').removeClass('back');
//               break;
//           case "phone":
//               form_class = "name";
//               break;
//           case "email":
//               form_class = "phone";
//               break;
//          case "success":
//               form_class = "signup";
//               break; 
//       }
//      $('.icon-action').removeClass('back');
//   }

//   $('.grop-from').attr('id' , form_class);

// });

$('.grop-from').click(function(){
  selectedService = $(this)
  var form_class = selectedService.attr('class').substr(10);
  var field = selectedService.children('.form-body').children('.form-controls').children('.control-'+form_class);
  selectedService.removeClass(form_class);
  selectedService.children('.form-action').children('.icon-action').addClass('back');

  if(field.val() != ''){
    switch (form_class) {
      case 'name':
      form_class = "phone";
      break;

      case "phone":
      form_class = "email";
      break;

      case "email":
      form_class = "success";
      selectedService.submit();
      break;   

      case "success":
      form_class = "signup";
      break;

      default:
      form_class = "name";
    }
    selectedService.children('.form-action').children('.icon-action').addClass('back');

  } else {
    selectedService.children('.form-action').children('.icon-action.back').on('click', function() {
      switch (form_class) {
        case 'name':
        form_class = "signup";
        selectedService.children('.form-action').children('.icon-action').removeClass('back');
        break;
        case "phone":
        form_class = "name";
        break;
        case "email":
        form_class = "phone";
        break;
        case "success":
        form_class = "signup";
        break; 
      }

      selectedService.children('.form-action').children('.icon-action').removeClass('back');
    });
      
  }

selectedService.addClass(form_class);

});

$('input').keyup(function() {
  $('.grop-from').removeClass('error');
  $('.error-text').fadeOut();

  if($(this).val()!=''){
    $('.icon-action').removeClass('back');
  } else {
    $('.icon-action').addClass('back');
  }
});