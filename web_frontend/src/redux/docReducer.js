const DOC = 'DOC';

let initialState = {

    doc:
        {
            title: "My Title",
            body: " Скажи, а чайки тоже плачут,\n" +
                "                Когда их море предает? -\n" +
                "                Спросила девочка у мальчика,\n" +
                "                Когда весной кололся лед.\n" +
                "                \n" +
                "                Деревья на ветру качались,\n" +
                "                И он ответил на вопрос:\n" +
                "                - Чайки разбиваются о скалы,\n" +
                "                Когда их море предает.\n" +
                "                \n" +
                "                Летели годы, словно ветер,\n" +
                "                Летели, оставляя след.\n" +
                "                И вот, они уже не дети,\n" +
                "                Им стало восемнадцать лет."
        },
};


const docReducer = (state = initialState, action) => {
    if (action.type === DOC) {
        let xhr = new XMLHttpRequest();
        xhr.open('GET', 'http://localhost:8000/searcher/doc/' + action.uuid, false);
        xhr.send();
        state.doc = JSON.parse(xhr.responseText)['doc'];
    }

    return state
};


export default docReducer;