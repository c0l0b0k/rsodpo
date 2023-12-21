function submitInitialSolution() {
     if (document.getElementById("stud_solution").value == '') {
        // Выводим сообщение или выполняем нужные действия при пустом поле
        Swal.fire({
  icon: "error",
  title: "Введите решение",
  showConfirmButton: false,
  timer: 1200
});
        return; // Преждевременный выход из функции
    }
document.getElementById("solution").value = document.getElementById("stud_solution").value;
    document.getElementById("status_solution").value=2
 $('#main_form').submit();

    }
function  againSolution(){

    document.getElementById("status_solution").value=1
    $('#main_form').submit();
}
function  submitSolution(){
    if (document.getElementById("stud_solution").value == '') {
        // Выводим сообщение или выполняем нужные действия при пустом поле
        Swal.fire({
  icon: "error",
  title: "Введите решение",
  showConfirmButton: false,
  timer: 1200
});
        return; // Преждевременный выход из функции
    }
document.getElementById("solution").value = document.getElementById("stud_solution").value;
    document.getElementById("status_solution").value=3
 $('#main_form').submit();
}
// 1,2 - чтобы боковое меню не срабатывало