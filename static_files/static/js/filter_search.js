function filter_search() {
    var input, filter, name;
    input = document.getElementById('filter');
    filter = input.value.toUpperCase().trim();
    name = document.querySelectorAll('.name');
    for (i = 0; i < name.length; i++) {
        name_text = name[i].textContent.toUpperCase().trim()
        if(name_text.toUpperCase().indexOf(filter) > -1){
            name[i].closest('.block').style.display = "";
        }else{
            name[i].closest('.block').style.display = 'none'; 
        }
    }
}

function genre_filter_search() {
    var input, filter, name;
    input = document.getElementById('genre_filter');
    filter = input.value.toUpperCase().trim();
    name = document.querySelectorAll('.genre');
    for (i = 0; i < name.length; i++) {
        name_text = name[i].textContent.toUpperCase().trim()
        if(name_text.toUpperCase().indexOf(filter) > -1){
            name[i].closest('.genre_block').style.display = "";
        }else{
            name[i].closest('.genre_block').style.display = 'none'; 
        }
    }
}