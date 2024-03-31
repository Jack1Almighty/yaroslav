
/*
// Обработчик события для перехода на другие страницы
$('a').click(function(event) {
    event.preventDefault(); // Предотвращаем переход по ссылке

    var url = $(this).attr('href'); // Получаем URL из атрибута href ссылки

    // Загрузка содержимого страницы через AJAX
    $.ajax({
        url: url,
        type: 'GET',
        success: function(data) {
            // Обновление содержимого основной области страницы
            $('#main-content').html(data);
        },
        error: function(xhr, status, error) {
            // Обработка ошибок
            console.error(error);
        }
    });
});
*/