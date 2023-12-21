$(document).ready(function() {

        // Восстановление состояния при загрузке страницы
      var collapsedNodes = $('#collapsedNodesInput').val() ? $('#collapsedNodesInput').val().split(',') : [];
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
     $('.subsection').click(function() {

            var nodeId = $(this).attr('id').replace('subsection', '');

            // Обновление значения скрытого поля
            $('#selected_topic').val(nodeId);
         $('#sidebar_menu').submit();
        });

    });
