// A url dessa API recebe os seguintes parâmetros:
// json = true -> para receber os dados em json
// ano = 2019 -> ano dos feriados
// ibge = 5300108 -> código ibge da cidade, no caso esse é o de brasília
// token = ZHJlYW1zc3dpdGNoQGdtYWlsLmNvbSZoYXNoPTExODE3Mjk0OQ -> token de acesso a api (não sei onde colocar qnd dermos o deploy)
const api_url = 'https://api.calendario.com.br/?json=true&ano=2019&ibge=5300108&token=ZHJlYW1zc3dpdGNoQGdtYWlsLmNvbSZoYXNoPTExODE3Mjk0OQ';

async function get_hollidays(api_url) {
    const response = await fetch(api_url);
    const data = await response.json();
    return data;
}

function format_date(date) {
    var ano, mes, dia;
    var formated_date;

    dia = date.substr(0,2);
    mes = date.substr(3,2);
    ano = date.substr(6,4);

    formated_date = ano + '/' + mes + '/' + dia;
    return formated_date;
}

async function get_eventos(eventos_bd) {

    const response = await fetch(api_url);
    const hollidays = await response.json();

    var Eventos = [];
    Eventos = eventos_bd;
    console.log(hollidays.length)
    for (var i = 0; i < hollidays.length; i++) {
        var obj = {
            title: hollidays[i].name,
            allDay: true,
            start: format_date(hollidays[i].date),
            backgroundColor: '#3c5a8c',
            borderColor: '#3c5a8c',
            textColor: 'white',
        }
        console.log('hello');
        Eventos.push(obj);
    }
    //console.log(Eventos);
    return Eventos;
}