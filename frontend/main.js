// string zipcode
function ZipcodeCheckbox(zipcode){
    if(document.getElementById(zipcode).checked){
        console.log(zipcode + " checked");
    }
    else{
        console.log(zipcode + " unchecked");
    }
}

// string dataset which can be covid or crime
function DataSetChange(dataset){
    if(dataset === "crime") {
        console.log("user chose crime");
    }
    else if(dataset === "covid"){
        console.log("user chose covid");
    }
}

function StartDateChanged(newDate){
	newDate = newDate.replaceAll('-', '/');
    console.log(newDate);
}

function EndDateChanged(newDate){
	newDate = newDate.replaceAll('-', '/');
    console.log(newDate);
}

function TogglePlaces(){
    if(document.getElementById("POIs").checked){
        console.log("show places")
    }
    else{
        console.log("hide places")
    }
}

function ToggleFoodVendors(){
    if(document.getElementById("food_places").checked){
        console.log("show food vendors")
    }
    else{
        console.log("hide food vendors")
    }
}
