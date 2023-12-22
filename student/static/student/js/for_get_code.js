
function getSolutionCode(solution_id) {
    $.ajax({
        url: `/get_solution_code/${solution_id}/`,  // Укажите URL вашего представления
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            // Обработка успешного ответа
            var programCode = response.program_code;
            document.getElementById('program_code').value=programCode;
            // Добавьте ваш код для обработки программного кода
        },
        error: function(error) {
            // Обработка ошибки
            console.error('Ошибка при получении программного кода:', error);
        }
    });
}

function myFunction(parameter) {
    // Ваш JavaScript-код здесь, используя параметр

    getSolutionCode(parameter);
    // Или вызов функции, которую вы хотите выполнить с параметром
}
