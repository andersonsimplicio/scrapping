var buttons = document.querySelectorAll(".rows img");

buttons.forEach(function(item, idx) {
    item.addEventListener('click', function(e) {
        let src = item.getAttribute('alt').replace(/\s/g, '');
        let csvName = getName(src);
        console.log(csvName);
        let right_col = document.querySelector(".right-col");
        let left_col = document.querySelector("#left-col");
        right_col.style.display = 'block';
        left_col.style.marginLeft = '-50px';
        chartIt(csvName);
    })
});

function getName(name) {
    var fileTest = "../csv/" + name + ".csv";
    return fileTest
};

async function chartIt(newFile) {
    console.log(newFile);
    const data = await getData(newFile);
    const ctx = document.getElementById('myChart').getContext('2d');

    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.xAxis,
            datasets: [{
                label: 'Comentários / Ano',
                data: data.yAxis,
                fill: false,
                backgroundColor: 'rgba(0, 0, 0, 0.8)',
                borderColor: 'rgba(0, 0, 0, 0.5)',
                pointBorderColor: "rgba(38, 185, 154, 0.7)",
                pointBackgroundColor: "rgba(38, 185, 154, 0.7)",
                pointHoverBackgroundColor: "#fff",
                pointHoverBorderColor: "#0f0",
                pointBorderWidth: 2,
                borderJoinStyle: 'miter',
                pointBackgroundColor: '#0f0',
                borderWidth: 3
            }]
        },
        options: {
            responsive: true,
            plugins: {
                datalabels: {
                    color: "black",
                    textAlign: "right",
                    font: {
                        weight: "bold",
                        family: "Times New Roman",
                        size: 18
                    },
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        // stacked: true,
                        fontColor: 'white',
                        fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                        fontSize: 15,
                        padding: 10,
                    }
                }],
                xAxes: [{
                    ticks: {
                        fontColor: 'white',
                        fontFamily: "'Helvetica Neue', 'Helvetica', 'Arial', sans-serif",
                        fontSize: 14,
                        padding: 5,
                    }
                }]
            },
            legend: {
                display: true,
                labels: {
                    fontColor: 'white',
                    fontSize: 18,
                    padding: 5
                }
            },
            title: {
                display: false,
                // text: 'Custom Chart Title',
                fontColor: 'white',
                fontSize: 20,
                top: 0,
            }
        }
    });
}


async function getData(param) {
    const xAxis = [];
    const yAxis = [];
    const response = await fetch(param);
    const data = await response.text();

    const table = data.split('\n').slice(1);
    table.forEach(row => {
        const cols = row.split(',');
        const year = cols[0];
        xAxis.push(year);
        const qtdComment = cols[1];
        yAxis.push(qtdComment);
    });
    return { xAxis, yAxis }
}