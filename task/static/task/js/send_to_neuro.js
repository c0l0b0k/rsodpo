$(document).ready(function() {
  $('#sent_neuro').click(function() {
    // Получение данных для отправки
    var task = document.getElementById('id_task').value
    var solution = document.getElementById('id_program_code').value



    var model=document.getElementById('id_model')
    model = model.options[model.selectedIndex].text

    var topic=document.getElementById('id_topic')
    topic = topic.value


    var data = {
      task:task,
      solution:solution,
      topic:topic,
       model:model,
    };

    // Отправка ajax запроса
    $.ajax({
      type: 'POST',
      url: '/sent_neuro/', // URL для обработки запроса в Django
      data: data,
      success: function(response) {
        console.log(response)
        var answer = document.getElementById('neuro_answer')
//        const textNode = document.createTextNode(response["answer"])
        answer.textContent = response["answer"]
        // Обработка успешного ответа от сервера
      },
      error: function(error) {
        // Обработка ошибки
      }
    });
  });
});


$(document).ready(function() {
  $('#add_request').click(function() {
    // Получение данных для отправки

    var task = document.getElementById('id_task').value
    var task_id=document.getElementById('id_choose_task').value
    var difficulty= document.getElementById('id_difficulty').value
    var solution =document.getElementById('id_program_code').value
    var topic=document.getElementById('id_topic')
    topic = topic.value




    var data = {
      difficulty:difficulty,
      topic:topic,
      task_id:task_id,
      task:task,
      solution:solution
    };

    // Отправка ajax запроса
    $.ajax({
      type: 'POST',
      url: '/add_request/', // URL для обработки запроса в Django
      data: data,
      success: function(response) {
          var temp1=document.getElementById('id_task').value="";
        var temp1=document.getElementById('id_program_code').value=""
         var temp1=document.getElementById('id_difficulty').value=""
        $('#id_task').val('');
      },
      error: function(error) {
        // Обработка ошибки
      }
    });
  });
});

$(document).ready(function() {
  $('#start_fon_task').click(function() {

        console.log("sds")

    // Отправка ajax запроса
    $.ajax({
      type: 'POST',
      url: '/start_fon_task/', // URL для обработки запроса в Django
      success: function(response) {

      },
      error: function(error) {
        // Обработка ошибки
          alert("ошибка")
      }
    });
  });
});