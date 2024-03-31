$(document).ready(function(){

  $('.select-all-checkbox, .filter-checkbox').prop('checked', true);

  if($('.filter-checkbox.category:checked').length === $('.filter-checkbox.category').length){
    $('#select-all-categories').prop('checked', true);
  }

  if($('.filter-checkbox.difficulty:checked').length === $('.filter-checkbox.difficulty').length){
    $('#select-all-difficulties').prop('checked', true);
  }

  $('.select-all-checkbox, .filter-checkbox').change(function(){
    if($(this).hasClass('select-all-checkbox')){
      if($(this).hasClass('select-all-categories')){
        $('.filter-checkbox.category').prop('checked', $(this).is(':checked'));
      } else {
        $('.filter-checkbox.difficulty').prop('checked', $(this).is(':checked'));
      }
    }

    var categoriesToShow = [];
    var difficultiesToShow = [];

    $('.filter-checkbox.category:checked').each(function(){
      categoriesToShow.push($(this).data('category'));
    });

    $('.filter-checkbox.difficulty:checked').each(function(){
      difficultiesToShow.push($(this).data('difficulty'));
    });

    $('.task').hide();

    categoriesToShow.forEach(function(category){
      difficultiesToShow.forEach(function(difficulty){
        $('.task[data-category="' + category + '"][data-difficulty="' + difficulty + '"]').show();
      });
    });

    if($('.filter-checkbox.difficulty:checked').length === $('.filter-checkbox.difficulty').length){
      $('#select-all-difficulties').prop('checked', true);
    } else {
      $('#select-all-difficulties').prop('checked', false);
    }


    if($('.filter-checkbox.category:checked').length === $('.filter-checkbox.category').length){
      $('#select-all-categories').prop('checked', true);
    } else {
      $('#select-all-categories').prop('checked', false);
    }
  });
});