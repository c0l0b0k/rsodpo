function submitForm() {
    // Создаем форму
    if (document.getElementById("mark").value == '') {
        // Выводим сообщение или выполняем нужные действия при пустом поле
        Swal.fire({
  icon: "error",
  title: "Пожалуйста, поставьте оценку",
  showConfirmButton: false,
  timer: 1200
});
        return; // Преждевременный выход из функции
    }
    var path="/lab_view/"+document.getElementById("solution").value+"/";
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", path); // Замените "/your-form-endpoint/" на реальный URL для обработки формы в Django

    // Создаем скрытые поля для каждого ввода и добавляем их в форму
    var field1 = document.createElement("input");
    field1.setAttribute("type", "hidden");
    field1.setAttribute("name", "recommend_text");
    field1.value = document.getElementById("chat-container").innerHTML;
    form.appendChild(field1);


    var field2 = document.createElement("textarea");
    field2.setAttribute("type", "hidden");
    field2.setAttribute("name", "recommend_teacher");
    field2.value= document.getElementById("recommend_teacher").value;
    form.appendChild(field2);

    var field3 = document.createElement("input");
    field3.setAttribute("type", "hidden");
    field3.setAttribute("name", "mark");
    field3.setAttribute("value", document.getElementById("mark").value);
    form.appendChild(field3);

    // Добавляем форму в тело документа и отправляем
    document.querySelector('.main').appendChild(form);
    form.submit();

}
