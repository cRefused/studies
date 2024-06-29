var msg_uncomplete = '<div class="error"><b>Не все поля заполнены</b></div>';

function fn_msg_error(eid, msg) {
  document.getElementById(eid).insertAdjacentHTML('afterbegin', msg);
}

function close_rcard(rcard_id){
  let elem = 'rnf_'+rcard_id;
  if(document.getElementById(elem)){
    document.getElementById(elem).remove();
  }
}

// ---------------------------------------------------------

// просмотр карточки
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

// редактирование карточки
function send_rcard(f) {
  $('.error').remove();
  var work_done = document.forms[f].elements['work_done'].value;
  var rcard_id = document.forms[f].elements['rcard_id'].value;
  var date_issue = document.forms[f].elements['date_issue'].value;
  var di_checkbox = document.forms[f].elements['di_checkbox'].checked;

  if(di_checkbox == false  && (work_done == '' || date_issue == ''))
  {
    fn_msg_error('rcard-frame', msg_uncomplete);
    return 1;
  }
  else if(di_checkbox == true)
  {
    date_issue = 0;
  }

  // заполняем данные формы
  var rcard = new FormData();
  rcard.append('work_done', work_done);
  rcard.append('rcard_id', rcard_id);
  rcard.append('date_issue', date_issue);
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
        date_issue = arr_result['date_issue'];
        work_done = arr_result['work_done'];
        href_font = arr_result['href_font'];

        document.getElementById('a'+rcard_id).className = href_font;
        document.getElementById('date_issue_'+rcard_id).innerHTML = date_issue;
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

// добавление новой карточки
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
    fn_msg_error('rcard-frame', msg_uncomplete);
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
