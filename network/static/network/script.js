function like(id) {
  like_button = document.querySelector(`.like-button-${id}`)
  likes = document.querySelector(`.likes-number-${id}`);
  likes_number = parseInt(document.querySelector(`.likes-number-${id}`).innerHTML);
  updated_likes = parseInt(likes_number + 1);
  fetch('/like/' + id, {
    method: 'PATCH',
    headers : { 
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken') 
     },
    body: JSON.stringify({
        likes: likes_number
    })
  })
  .then(response => response.json())
  .then(json => {
    likes.innerHTML = `${json.like}`
  })
}


function edit(id) {
    // CONTAINER + TEXT
    let container = document.querySelector(`#edit-box-${id}`);
    let text = container.querySelector(".card-text");
    let btn_div = container.querySelector("#btn-div")
    var text_value = text.innerHTML;
    text.innerHTML = ``;
    
    // TEXTAREA
    var textarea =  document.createElement("textarea");
    textarea.rows = 7;
    textarea.className = "appear";
    textarea.style.width = "100%";
    textarea.value = text_value;
    textarea.tagName = "update";
    text.appendChild(textarea);
    textarea.style.animationPlayState = "running";

    // EDIT BUTTON
    const edit_button = document.querySelector(`#edit-btn-${id}`);
    edit_button.remove();

    // SAVE BUTTON
    save_button = document.createElement("button");
    save_button.className = "btn btn-success";
    save_button.innerHTML = "Save";
    btn_div.appendChild(save_button)

    save_button.addEventListener('click', function () {
      // UPDATE
      fetch('edit/' + id, {
        method: 'POST',
        headers : { 
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken') 
         },
        body: JSON.stringify({
        description: textarea.value,
      })
    })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);

      // Save input value
      input_value = textarea.value;
      console.log(input_value)

      // Restore post
      text.innerHTML = `${input_value}`
      // Restore edit button
      save_button.remove()
      btn_div.appendChild(edit_button)
    });
  });  
}

// GET CSRF_TOKEN
// FUNCITON COPIED
function getCookie(name) {
  if (!document.cookie) {
    return null;
  }
  const token = document.cookie.split(';')
  .map(c => c.trim())
  .filter(c => c.startsWith(name + '='));
  if (token.length === 0) {
    return null;
  }
  return decodeURIComponent(token[0].split('=')[1]);
}