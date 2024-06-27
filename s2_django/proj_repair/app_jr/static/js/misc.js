// Показываем спиннер
function wSpinner()
{
  var bodyNode = document.body || document.getElementsByTagName('body')[0];
  var msg_blocked = '<div class="content-blocker" id="content-blocker"><div class="loader-spinner-icon"></div></div>';
  bodyNode.insertAdjacentHTML('afterbegin', msg_blocked);
}

// Спиннер по таймауту
function wSpinner_tmout()
{
  window.timerIdOver = setTimeout(() => {
    wSpinner()
  }, 1000);
}

// удалить css класс у элемента
function fn_remove_class(e, c){
  if(window.parent.document.getElementById(e).classList.contains(c)){
    window.parent.document.getElementById(e).classList.remove(c);
  }
}
