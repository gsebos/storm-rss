const containers = document.getElementsByClassName('droppable');
const dragItems = document. getElementsByClassName('draggable');
let selected;
let django_operation;
let django_model;
let new_foreignKey;
let item_pk;

for( let dragItem of dragItems){
   dragItem.addEventListener("dragstart", function(e){
         selected = e.target;
         selected.classList.add('dragging')  // For tracking the drag
   });

   dragItem.addEventListener("dragend", function (e) {
    // Clean up the target container class when the drag ends
    for (let container of containers) {
      container.classList.remove("dnd-target");
    }
    selected.classList.remove('dragging');
  });
};

for(let container of containers){ 
    container.addEventListener("dragover",function(e){
        e.preventDefault();  
        e.stopPropagation();

    });
    // Handle css for the target container on entering with the cursor
    container.addEventListener("dragenter",function(e){
        e.preventDefault();  
        e.stopPropagation();

        e.currentTarget.classList.add('dnd-target');

    });
    // Handle css for the target container on leaving with the cursor
    container.addEventListener("dragleave",function(e){
        e.preventDefault();  
        e.stopPropagation();

           // Only trigger when the mouse leaves the container, not child elements 
        if (!container.contains(e.relatedTarget) ||  container.classList.contains('sidebar') ) {

            e.currentTarget.classList.remove("dnd-target");
        }

    });

    container.addEventListener("drop",function(e){
        e.preventDefault();
        e.stopPropagation();

        e.currentTarget.classList.remove("dnd-target");

        let selected_folder = e.currentTarget;
        selected_folder.appendChild(selected);

        selected.setAttribute('draggable', 'true');

        if(selected_folder.classList.contains('sidebar')){
            selected.classList.replace('subfolder','folder');
            selected.classList.remove('indent');
            django_operation = 'ForeignKey_to_blank';
        }

        if(selected_folder.classList.contains('folder') && !selected_folder.classList.contains('sidebar')){
            if(selected.classList.contains('folder')){
                selected.classList.replace('folder','subfolder');
            };
            selected.classList.add('indent');
            django_operation = 'Update_ForeignKey';

        }else if(selected_folder.classList.contains('subfolder')){
            if(!selected.classList.contains('folder')){
                selected.classList.add('indent');
                django_operation = 'Update_ForeignKey';
            };
        }


        let selected_folder_id = selected_folder.id;
        let selected_id = selected.id;

        django_model = selected_id.split('-')[0]
        new_foreignKey = selected_folder_id.split('-')[1]
        item_pk = selected_id.split('-')[1]

        console.log("Django Model:",django_model);
        console.log("Operation:",django_operation);
        console.log("New Foreign Key:",new_foreignKey);
        console.log("Django item pk:",item_pk);

        sendDataToDjango(django_model,django_operation,new_foreignKey,item_pk);

    });
};

function sendDataToDjango(django_model,django_operation,new_foreignKey,item_pk){
    fetch('/update-feed-location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Ensure CSRF token is included in requests
        },
        body: JSON.stringify({
            django_model: django_model,
            django_operation: django_operation,
            new_foreignKey: new_foreignKey,
            item_pk : item_pk
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Data sent to Django:', data);
        location.reload(true);
    })
    .catch(error => {
        console.error('Error sending data to Django:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}