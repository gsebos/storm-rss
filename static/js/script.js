const containers = document.getElementsByClassName('droppable');
const dragItems = document. getElementsByClassName('draggable');
let selected;
let django_operation;
let django_model;
let new_foreignKey;
let item_pk;

console.log(containers);

for( let dragItem of dragItems){
   dragItem.addEventListener("dragstart", function(e){
         selected = e.target;
   });
};

for(let container of containers){ 
    container.addEventListener("dragover",function(e){

        e.preventDefault();  
        e.stopPropagation();
    });
    container.addEventListener("drop",function(e){

        e.preventDefault();
        e.stopPropagation();

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
        }

        if(selected.classList.contains('folder') || selected.classList.contains('subfolder')){
            django_model = 'Folder';
            }
        else{
                django_model = 'Feed';
            }

        let selected_folder_id = selected_folder.id;
        let selected_id = selected.id;

        let new_foreignKey = parseInt(selected_id.slice(selected_id.indexOf('-') + 1), 10);
        let item_pk = parseInt(selected_folder_id.slice(selected_folder_id.indexOf('-') + 1), 10);

        console.log(django_model);
        console.log(django_operation);
        console.log(new_foreignKey);
        console.log(item_pk);

    });
};