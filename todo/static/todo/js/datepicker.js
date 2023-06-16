// window.onload = ()=>{
//     let btn = document.querySelector('#btn_calendar')
//     let datepicker = document.querySelector('#deadline')
//
//     btn.addEventListener('click', () =>{
//     datepicker.classList.remove('invisible')
//     datepicker.click()
// })
// }
$(document).ready(()=>{

    $('#deadline').datepicker({
        showOn: "button",
        buttonText: '<i class="fa-solid fa-calendar-days fa-2xl" style="color: #e0107f;"></i>',
        dateFormat:'yy-mm-dd'
    })


})