
async function SubmitVars() {
// data to be sent to the POST request
var vpara = document.getElementById("para").value;


let _data = {
        features: vpara
  }

  const response = await fetch('https://api-4-mmorfk42na-nw.a.run.app/ents', {
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  const responseText = await response.text();
  console.log(responseText); 

  const obj = JSON.parse(responseText);
  let date = (obj.date);
  let country = (obj.country);
  console.log(date);
  console.log(country);
  console.log(buildings);


  var x = document.getElementById("demo1");  
  x.style.color = "red"; 
  x.innerHTML = date;

  var y = document.getElementById("demo2");  
  y.style.color = "red"; 
  y.innerHTML = country;

  var y = document.getElementById("demo3");  
  y.style.color = "red"; 
  y.innerHTML = buildings;

}