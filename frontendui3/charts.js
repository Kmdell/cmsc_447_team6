// -----------------CHART FIVE START (NOT DONE)-----------------
let cFiveLabels = ["2020", "2021", "2022"];
let cFiveData = [];
let cFiveFinalData = [];

covidDiscTwo = fetch('http://127.0.0.1:5000/covid')
    .then(response => response.json())
    .then(data => { dData = data; })
    .then(() => {
        let totalDates = 0;
        let iter = 0;
        for(let date in dData){
            totalDates++;
            cFiveLabels[iter] = date;
            iter++;
        }

        let dates = []
        let numDates = Math.floor(totalDates / 12);
        iter = 0;

        for(let i = 0; i < 12; i++){
            dates[iter] = cFiveLabels[i * numDates];
            iter++;
        }

        console.log(dates[0]);

        iter = 0;
        let iterTwo = 0;
        let prevDates = [];
        let iterThree = 0;

        for(let i = 0; i < dates.length; i++){
            let total = 0;

            console.log(dates[i].toString());

            for(let date in dData){

                if(date === dates[i]){
                    prevDates[6] = date;

                    for(let j = 0; j < prevDates.length; j++){
                        for(let zipcodes in dData[prevDates[j]]){
                            console.log("Here");
                            total += dData[prevDates[j]][zipcodes]['total'];
                        }
                    }

                    cFiveFinalData[iterThree] = total / 7;

                    break;
                }

                if(iter === 6){
                    prevDates[iterTwo] = date;
                    iterTwo++;

                    if(iterTwo === 6) iterTwo = 0
                }
                else{
                    prevDates[iter] = date;
                    iter++;
                }
            }

            prevDates = [];
            iter = 0;
            iterTwo = 0;
            iterThree++;
        }

        console.log(cFiveFinalData.length);


        ChartFive.data.datasets[0].data = cFiveFinalData;
        ChartFive.data.labels = dates;

        ChartFive.update();
    });

var ChartFive = new Chart("chart_five", {
    type: "line",
    data: {
        labels: cFiveLabels,
        datasets: [{
            data: cFiveData
        }]
    },
    options: {
        title: {
            display: true,
            text: "Covid 7-day Moving Average"
        }
    }
});
// -----------------CHART FIVE END-----------------




// -----------------CHART FOUR START-----------------
let cFourLabels = ["2020", "2021", "2022"];
let cFourData = [];
let cFourColors = ["#2568da", "#d7283c", "#3dda25"];

crimeDicTwo = fetch('http://127.0.0.1:5000/crime')
    .then(response => response.json())
    .then(data => { dData = data; })
    .then(() => {
        let total2020 = 0;
        let total2021 = 0;
        let total2022 = 0;

        for(let date in dData){
            let crimeCount = 0;

            for(let item in dData[date]){
                crimeCount++;
            }

            if(date.indexOf("2020") >= 0){
                total2020 += crimeCount;
            }
            else if(date.indexOf("2021") >= 0){
                total2021 += crimeCount;
            }
            else if(date.indexOf("2022") >= 0){
                total2022 += crimeCount;
            }
        }

        cFourData = [total2020, total2021, total2022];

        ChartFour.data.datasets[0].data = cFourData;

        ChartFour.update();
    });

var ChartFour = new Chart("chart_four", {
    type: "pie",
    data: {
        labels: cFourLabels,
        datasets: [{
            data: cFourData,
            backgroundColor: cFourColors
        }]
    },
    options: {
        title: {
            display: true,
            text: "Total Crimes Each Year"
        }
    }
});
// -----------------CHART FOUR END-----------------




// -----------------CHART THREE START-----------------
let cThreeData = [];
let cThreeLabels = ['t', 't', 't', 't', 't'];
covidDic = fetch('http://127.0.0.1:5000/covid')
    .then(response => response.json())
    .then(data => { dData = data; })
    .then(() => {
        let date = "2022/11/03";

        let iter = 0;
        for(let zipcode in dData[date]){
            cThreeData[iter] = dData[date][zipcode]['total'];
            iter++;
        }

        let sortedData = cThreeData.sort((a, b) => b - a);

        cThreeData = []
        cThreeData[0] = sortedData[0];
        cThreeData[1] = sortedData[1];
        cThreeData[2] = sortedData[2];
        cThreeData[3] = sortedData[3];
        cThreeData[4] = sortedData[4];

        for(let zipcode in dData[date]){
            if(dData[date][zipcode]['total'] === cThreeData[0]){
                cThreeLabels[0] = zipcode;
            }
            else if(dData[date][zipcode]['total'] === cThreeData[1]){
                cThreeLabels[1] = zipcode;
            }
            else if(dData[date][zipcode]['total'] === cThreeData[2]){
                cThreeLabels[2] = zipcode;
            }
            else if(dData[date][zipcode]['total'] === cThreeData[3]){
                cThreeLabels[3] = zipcode;
            }
            else if(dData[date][zipcode]['total'] === cThreeData[4]){
                cThreeLabels[4] = zipcode;
            }
        }

        ChartThree.data.datasets[0].data = cThreeData;
        ChartThree.data.labels = cThreeLabels;

        ChartThree.update();
    });

var ChartThree = new Chart("chart_three", {
    type: "bar",
    data: {
        labels: cThreeLabels,
        datasets: [{
            data: cThreeData,
        }]
    },
    options: {
        title: {
            display: true,
            text: "Zipcodes With the Most Covid Cases"
        }
    }
});
// -----------------CHART THREE END-----------------





// -----------------CHART TWO START-----------------
let cTwoLabels = ["Burglary", "Larceny", "Agg. Assault", "Robbery", "Auto Theft", "Rape", "Homicide"]
let cTwoData;

crimeDic = fetch('http://127.0.0.1:5000/crime')
    .then(response => response.json())
    .then(data => { dData = data; })
    .then(() => {
        let totalBurglary = 0;
        let totalLarceny = 0;
        let totalAggAssault = 0;
        let totalRobbery = 0;
        let totalAutoTheft = 0;
        let totalRape = 0;
        let totalHomicide = 0;

        for(let date in dData){
            for(let item in dData[date]){
                if(dData[date][item]['type'] === "BURGLARY"){
                    totalBurglary++;
                }

                if(dData[date][item]['type'] === "LARCENY"){
                    totalLarceny++;
                }

                if(dData[date][item]['type'] === "AGG. ASSAULT"){
                    totalAggAssault++;
                }

                if(dData[date][item]['type'] === "ROBBERY"){
                    totalRobbery++;
                }

                if(dData[date][item]['type'] === "AUTO THEFT"){
                    totalAutoTheft++;
                }

                if(dData[date][item]['type'] === "RAPE"){
                    totalRape++;
                }

                if(dData[date][item]['type'] === "HOMICIDE"){
                    totalHomicide++;
                }
            }
        }

        cTwoData = [totalBurglary, totalLarceny, totalAggAssault, totalRobbery, totalAutoTheft, totalRape, totalHomicide]

        ChartTwo.data.datasets[0].data = cTwoData;

        ChartTwo.update();
    });

var ChartTwo = new Chart("chart_two", {
    type: "bar",
    data: {
        labels: cTwoLabels,
        datasets: [{
            data: cTwoData
        }]
    },
    options: {
        title: {
            display: true,
            text: "Crime Distribution From 04/2020 - 11/2022"
        },
        legend: {
            display: false
        },
    }
});
// -----------------CHART TWO END-----------------




// -----------------CHART ONE START-----------------
const cOneLabels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const cOneColors = ["#6231ce", "#278fd8", "#31ce62", "#b0e11e", "#d93f26", "#1468eb", "#e3ce1c", "#43d02f", "#da25be", "#de2148", "#1fbce0", "#db24c6"];
let cOneData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12]

covidDic = fetch('http://127.0.0.1:5000/covid')
    .then(response => response.json())
    .then(data => { dData = data; })
    .then(() => {
        console.log(dData);

        let total = 0;

        for(let key in dData['2021/01/31']){
            total += dData['2021/01/31'][key]['total']
        }
        cOneData[0] = total;
        total = 0;

        for(let key in dData['2021/02/28']){
            total += dData['2021/02/28'][key]['total']
        }
        cOneData[1] = total;
        total = 0;

        for(let key in dData['2021/03/31']){
            total += dData['2021/03/31'][key]['total']
        }
        cOneData[2] = total;
        total = 0;

        for(let key in dData['2021/04/30']){
            total += dData['2021/04/30'][key]['total']
        }
        cOneData[3] = total;
        total = 0;

        for(let key in dData['2021/05/31']){
            total += dData['2021/05/31'][key]['total']
        }
        cOneData[4] = total;
        total = 0;

        for(let key in dData['2021/06/30']){
            total += dData['2021/06/30'][key]['total']
        }
        cOneData[5] = total;
        total = 0;

        for(let key in dData['2021/07/31']){
            total += dData['2021/07/31'][key]['total']
        }
        cOneData[6] = total;
        total = 0;

        for(let key in dData['2021/08/31']){
            total += dData['2021/08/31'][key]['total']
        }
        cOneData[7] = total;
        total = 0;

        for(let key in dData['2021/09/30']){
            total += dData['2021/09/30'][key]['total']
        }
        cOneData[8] = total;
        total = 0;

        for(let key in dData['2021/10/31']){
            total += dData['2021/10/31'][key]['total']
        }
        cOneData[9] = total;
        total = 0;

        for(let key in dData['2021/11/30']){
            total += dData['2021/11/30'][key]['total']
        }
        cOneData[10] = total;
        total = 0;

        for(let key in dData['2021/12/31']){
            total += dData['2021/12/31'][key]['total']
        }
        cOneData[11] = total;

        ChartOne.update();
    });

var ChartOne = new Chart("chart_one", {
    type: "line",
    data: {
        labels: cOneLabels,
        datasets: [{
            data: cOneData,
            backgroundColor: cOneColors
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: "Covid Cases Over 2021"
        }
    }
});
// -----------------CHART ONE END-----------------





