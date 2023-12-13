const myModal = new HystModal({
    linkAttributeName: "data-hystmodal",
    // настройки (не обязательно), см. API
});


$(document).ready(function() {
  $('#new_topic').click(function() {
    // Получение данных для отправки
    console.log("1")
    var new_topic=document.getElementById('id_new_topic')

      var sub_topic =document.getElementById('id_sub_topic')
        var system_role =document.getElementById('id_system_role_text')

     var data = {new_topic:new_topic.value,
       sub_topic:sub_topic.value,
         system_role:system_role.value
     };
    // Отправка ajax запроса
    $.ajax({
      type: 'POST',
      url: '/new_topic/', // URL для обработки запроса в Django
       data: data,
      success: function(response) {
          new_topic.value = '';
          system_role.value='';
          sub_topic.selectedIndex = -1
        var apdateSelect = document.getElementById('id_topic');

        console.log(response)

          var option = document.createElement('option');
        option.value = response["value"]; // Обращение к полям объекта topic
        option.text =  response["topic_name"]; // Обращение к полям объекта topic
         apdateSelect.appendChild(option);
            //$("#id_topic").val(option.value)
          apdateSelect.value = option.value;
//        apdateSelect.selectedIndex = reloadSelect.options.length - 1
      },
      error: function(error) {
        // Обработка ошибки
      }
    });
  });
});

 $(document).ready(function () {
    $('#id_topic').change(function () {
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
