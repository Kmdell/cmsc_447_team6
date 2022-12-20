let xyValues = [
    {x:22, y:4},
    {x:25, y:1},
    {x:31, y:9},
    {x:47, y:7},
    {x:67, y:2}
];

let zipcodesNum = [21201, 21202, 21203, 21204, 21205];
let zipcodes = ["21201", "21202", "21203", "21204", "21205"];
let covidDataByZip = [100, 120, 300, 50, 370];
let pieChartColors = ["#6231ce", "#278fd8", "#31ce62", "#b0e11e", "#d93f26"];

var ChartThree = new Chart("chart_three", {
    type: "pie",
    data: {
        labels: zipcodes,
        datasets: [{
            data: covidDataByZip,
            backgroundColor: pieChartColors
        }]
    },
    options: {
        title: {
            display: true,
            text: "Covid Cases by Zipcode"
        }
    }
});

// covid vs crime chart
var ChartTwo = new Chart("chart_two", {
    type: "line",
    data: {
        labels: zipcodesNum,
        datasets: [{
            pointRadius: 4,
            pointBackgroundColor: "rgba(255, 0, 0, 1)",
            borderColor: "red",

            data: [12, 15, 18, 29, 30, 100, 150]
        },{
            pointRadius: 4,
            pointBackgroundColor: "rgba(0, 0, 255, 1)",
            borderColor: "blue",

            data: [4, 90, 78, 190, 56, 45, 88]
        }]
    },
    options: {
        title: {
            display: true,
            text: "Covid vs. Crime"
        },
        legend: {
            display: false
        },
        yAxisID: {
            text: "test"
        }
    }
});

var Chart = new Chart("chart_one", {
    type: "scatter",
    data: {
        datasets: [{
            pointRadius: 4,
            pointBackgroundColor: "rgba(0,0,255,1)",
            data: xyValues
        }]
    },
    options: {
        legend: {
            display: false
        }
    }
});

/*,{
            pointRadius: 4,
            pointBackgroundColor: "rgba(0,0,255,1)",
            data: [4, 90, 78, 190, 56, 45, 88]
        }]*/