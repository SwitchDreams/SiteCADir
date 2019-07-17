
var data = getData();
console.log(data);

var ctx = document.getElementById('Grafico1').getContext('2d');
ctx.canvas.width = 100;
ctx.canvas.height = 100;
//console.log(ctx);

var dataGrap = Object.values(data);
var labelsGrap = Object.keys(data);
console.log(dataGrap);
console.log(labelsGrap);


var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: labelsGrap,
        datasets: [{
            label: '# of Votes',
            data: dataGrap,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        //maintainAspectRatio: false,
        aspectRatio : 2,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

//myChart.canvas.parentNode.style.height = '200px';
//muChart.canvas.parentNode.style.width = '200px';