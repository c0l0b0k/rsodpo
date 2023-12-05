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
      var url = '/get_tasks_for_topic/' + topicId + '/';

      $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
          var tasks = data.tasks;
          $('#id_choose_task').empty();

          // Добавляем пустой вариант
          $('#id_choose_task').append($('<option>', {
            value: '',
            text: '---------'
          }));

          // Заполняем варианты заданий
          $.each(tasks, function (index, task) {
            $('#id_choose_task').append($('<option>', {
              value: task.id,
              text: task.name
            }));
          });
        },
        error: function (error) {
          console.log(error);
        }
      });
    });

    $('#id_choose_task').change(function () {
      var taskId = $(this).val();
      if (taskId) {
        // Если выбрано задание, заполняем поле task
        var taskName = $('#id_choose_task option:selected').text();
        $('#id_task').val(taskName);
      } else {
        // Если выбран пустой вариант, очищаем поле task
        $('#id_task').val('');
      }
    });
  });
