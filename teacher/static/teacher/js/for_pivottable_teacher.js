
$(document).ready(function() {
        // При загрузке страницы проверяем, есть ли сохраненное значение в localStorage
        var selectedLetter = $('#selectedLetterNameInput').val();
        if (selectedLetter) {
            // Находим кнопку с соответствующим значением и меняем ей цвет
            $('.alphabet-button-name[data-letter="' + selectedLetter + '"]').removeClass('btn-outline-primary').addClass('btn-success');
        }
        var selectedLetter = $('#selectedLetterSurNameInput').val();
        if (selectedLetter) {
            // Находим кнопку с соответствующим значением и меняем ей цвет
            $('.alphabet-button-surname[data-letter="' + selectedLetter + '"]').removeClass('btn-outline-primary').addClass('btn-success');
        }
        // Обработка нажатия на кнопку
        $('.alphabet-button-name').click(function() {
            var letter = $(this).data('letter');

            // Устанавливаем скрытое поле с выбранной буквой
            $('#selectedLetterNameInput').val(letter);

            // Сохраняем значение в localStorage
            localStorage.setItem('selectedLetterName', letter);

            // Изменяем цвет нажатой кнопки
            $(this).removeClass('btn-outline-primary').addClass('btn-success');

            // Делаем submit формы
            $('#filter_and_topic').submit();
        });
        $('.alphabet-button-surname').click(function() {
            var letter = $(this).data('letter');

            // Устанавливаем скрытое поле с выбранной буквой
            $('#selectedLetterSurNameInput').val(letter);

            // Сохраняем значение в localStorage
            localStorage.setItem('selectedLetterSurName', letter);

            // Изменяем цвет нажатой кнопки
            $(this).removeClass('btn-outline-primary').addClass('btn-success');

            // Делаем submit формы
            $('#filter_and_topic').submit();
        });
    });
 $(document).ready(function() {
        // Восстановление состояния при загрузке страницы
      var collapsedNodes = $('#collapsedNodesInput').val() ? $('#collapsedNodesInput').val().split(',') : [];
//        collapsedNodes.forEach(function(nodeId) {
//
//            var targetId = '#dashboard-collapse' + nodeId;
//            var targetCollapse = new bootstrap.Collapse(document.querySelector(targetId));
//
//             // Инвертировать состояние collapse
//            targetCollapse.toggle();
//        });


        // Обработка раскрытия/скрытия узла
        $('#topicsList .btn-toggle').click(function() {
            var nodeId = $(this).data('bs-target').replace('#dashboard-collapse', '');

            if ($(this).hasClass('collapsed')) {
                // Узел был скрыт
                 collapsedNodes = collapsedNodes.filter(function(item) {
                    return item !== nodeId;
                });

            } else {
                // Узел был раскрыт
                collapsedNodes.push(nodeId);
            }

            // Обновление значения скрытого поля
            $('#collapsedNodesInput').val(collapsedNodes.join(','));
        });
    });
