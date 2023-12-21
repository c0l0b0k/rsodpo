 $(document).ready(function () {
    $('#id_topic').change(function () {
      var topicId = $(this).val();
   if (!topicId) {
      // Если topicId не определен или пуст, то просто очистите #id_subsection
      $('#id_subsection').empty();
     $('#id_subsection').append($('<option>', {
            value: '',
            text: '---------'
          }));
      return;
   }
      var topicId = $(this).val();
      var url = '/get_subsection_for_topic/' + topicId + '/';

      $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
          var topics = data.topics;
          $('#id_subsection').empty();

          // Добавляем пустой вариант
          $('#id_subsection').append($('<option>', {
            value: '',
            text: '---------'
          }));

          // Заполняем варианты заданий
          $.each(topics, function (index, topic) {
            $('#id_subsection').append($('<option>', {
              value:topic.id,
              text: topic.name
            }));
          });
        },
        error: function (error) {
          console.log(error);
        }
      });
    });

  });