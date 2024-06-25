function fn_msg_error(msg) {
  document.getElementById('main-frame').insertAdjacentHTML('afterbegin', msg);
}

function close_rcard(rcard_id){
  let elem = 'rnf_'+rcard_id;
  if(document.getElementById(elem)){
    document.getElementById(elem).remove();
  }
}

// ---------------------------------------------------------

function open_rcard(rcard_id) {
  var rcard = new FormData();
  rcard.append('rcard_id', rcard_id);
  rcard.append('fn', 'open_rcard');

  // готовим ajax запрос
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'fn/get_rcard', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4)
    {
      if (xhr.status == 200)
      {
          open_rcard_done(rcard_id, xhr.responseText);
      } else
      {
        // произошла ошибка
        fn_error(xhr.status);
        return;
      }
    }
  };
  xhr.send(rcard);
}

function open_rcard_done(rcard_id, text){
  let msg_container = '<div class="frame-blocker" id="rnf_'+rcard_id+'"><div class="frame-blocker-close" onClick="close_rcard(\''+rcard_id+'\')"></div>'+text+'</div>';
  document.getElementById('main').insertAdjacentHTML('afterbegin', msg_container);
}

function send_rcard(f) {
  var defect = document.forms[f].elements['defect'].value;
  var work_done = document.forms[f].elements['work_done'].value;
  var rcard_id = document.forms[f].elements['rcard_id'].value;

  // заполняем данные формы
  var rcard = new FormData();
  rcard.append('defect', defect);
  rcard.append('work_done', work_done);
  rcard.append('rcard_id', rcard_id);
  rcard.append('fn', 'write_rcard');

  // готовим ajax запрос
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'fn/get_rcard', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4)
    {
      if (xhr.status == 200)
      {
        arr_result = JSON.parse(xhr.responseText);
        rcard_id = arr_result['rcard_id'];
        defect = arr_result['defect'];
        work_done = arr_result['work_done'];

        document.getElementById('defect_'+rcard_id).innerHTML = defect;
        document.getElementById('work_done_'+rcard_id).innerHTML = work_done;

        close_rcard(rcard_id);
      } else
      {
        // произошла ошибка
        console.log(xhr.status);
        return;
      }
    }
  };
  xhr.send(rcard);
}

// --------------------------------------

function open_new_rcard() {
  var rcard = new FormData();
  rcard.append('fn', 'open_rcard');

  // готовим ajax запрос
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'fn/new_rcard', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4)
    {
      if (xhr.status == 200)
      {
          open_new_rcard_done(xhr.responseText);
      } else
      {
        // произошла ошибка
        fn_error(xhr.status);
        return;
      }
    }
  };
  xhr.send(rcard);
}
function open_new_rcard_done(text){
  let msg_container = '<div class="frame-blocker" id="rnf_0"><div class="frame-blocker-close" onClick="close_rcard(\'0\')"></div>'+text+'</div>';
  document.getElementById('main').insertAdjacentHTML('afterbegin', msg_container);
}

// добавление новой карточки
function send_new_rcard(f) {
  $('.error').remove();

  var msg_uncomplete = '<div class="error"><b>Не все поля заполнены</b></div>';
  var inv_num = document.forms[f].elements['inv_num'].value;
  var equipment_id = document.forms[f].elements['equipment_id'].value;
  var otdel = document.forms[f].elements['otdel'].value;
  var defect = document.forms[f].elements['defect'].value;
  var date_accept = document.forms[f].elements['date_accept'].value;

  if(inv_num == ''
  || equipment_id == ''
  || otdel == ''
  || defect == ''
  || date_accept == '')
  {
    fn_msg_error(msg_uncomplete);
    return 1;
  }

  // заполняем данные формы
  var rcard = new FormData();
  rcard.append('inv_num', inv_num);
  rcard.append('equipment_id', equipment_id);
  rcard.append('otdel', otdel);
  rcard.append('defect', defect);
  rcard.append('date_accept', date_accept);
  rcard.append('fn', 'write_rcard');

  // готовим ajax запрос
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'fn/new_rcard', true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4)
    {
      if (xhr.status == 200)
      {
        document.getElementById('list_rcard').insertAdjacentHTML('afterbegin', xhr.responseText);
        close_rcard(0);
      } else
      {
        // произошла ошибка
        console.log(xhr.status);
        return;
      }
    }
  };
  xhr.send(rcard);
}

// ---

function fn_error(text){
  console.log(text);
}
