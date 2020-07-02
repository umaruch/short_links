function get_short_url(){
    //Функция для отправки url, введенного пользователем и получения укороченной ссылки

    //получение введенной пользователей стандартной ссылки
    var long_url = document.getElementById("inlineFormInput").value;

    //Создание объекта http-запроса
    var request = new XMLHttpRequest();
    
    request.open('POST', "/new", true);
    request.setRequestHeader('Content-Type','application/json');

    request.addEventListener('readystatechange',()=>{
        if (request.status == 200 && request.readyState == 4){
            //Если данные успешно получены, красиво оформляем их и выдаем пользователю
            let obj = JSON.parse(request.responseText);
            let url = document.location.href+obj.url;
            let a = document.getElementById('link');
            a.innerText = url;
            a.href = url;
            document.getElementById("success-div").style.display = 'block';
            document.getElementById("error-div").style.display = 'none'
        }
        
        else {
            //Если данные успешно затерялись на почте, даем пользователю знать
            document.getElementById("success-div").style.display = 'none';
            document.getElementById("error-div").style.display = 'block'
        }
    });
    //Отправка запроса на сокращение url
    request.send(JSON.stringify({'url': long_url}));
}