# App diario-de-bordo

A aplicação é a diario:
* back-end em django seguindo arquitetura MVC
* integra pedidos assincronos AJAX, usando `fetch(pedido).then(resposta => fag_algo(resposta));`:
    * o cliente faz, num (`fetch()`) o pedido de um recurso ao servidor
    * quando é recebida a resposta, então (`then()`) é feito algo com essa resposta


# Video explicativo da App

[![explicacao](https://user-images.githubusercontent.com/42048382/164761509-d87071c9-37d4-48bd-8624-d95d360e8946.png)](https://youtu.be/kPJp3N2976I)


# Por fazer

### Credenciais
* [@login_required](https://docs.djangoproject.com/en/4.0/topics/auth/default/)

### Segurança contra malware

* incluir CSRF token nos fetch (ver detalhes [aqui](https://docs.djangoproject.com/en/4.0/ref/csrf/#ajax) para garantir que não há riscos
    * usar o [@csrf_protect](https://docs.djangoproject.com/en/4.0/ref/csrf/#module-django.views.decorators.csrf) antes de cada view que queremos protegida
    * usar ensure_csrf_cookie() na view para garantir q insere cookie.

```js
 function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


// E depois usa-se nos fetch assim: 

const request = new Request(
    /* URL */,
    {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin' // Do not send CSRF token to another domain.
    }
);
fetch(request).then(function(response) {
    // ...
});

// outro exemplo:

fetch(url, {
    credentials: 'include',
    method: 'POST',
    mode: 'same-origin',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: {}
   })
  }
  ```
