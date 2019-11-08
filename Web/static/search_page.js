button = document.getElementById("search-btn");
search_field = document.getElementById("search-field");


button.onclick = function () {

    let xhr = new XMLHttpRequest();


    xhr.open(
        "GET",
        "/getDocument?search_query=" + search_field.innerText
    );
    xhr.send();

    alert(xhr)



};




