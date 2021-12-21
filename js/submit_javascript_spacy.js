
async function SubmitVars() {
// data to be sent to the POST request
var vpara = document.getElementById("para").value;


let _data = {
        features: vpara
  }

  // Google URL should be : https://api-4-mmorfk42na-nw.a.run.app/ents

  const response = await fetch('https://api-4-mmorfk42na-nw.a.run.app/ents', {
    method: "POST",
    body: JSON.stringify(_data),
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  const responseText = await response.text();
  console.log(responseText); 

  const obj = JSON.parse(responseText);
  let date = (obj.date);
  let gpe = (obj.country);
  let org = (obj.organization);
  let fac = (obj.facility);
  let person = (obj.people);
  let money = (obj.money);
  let weight_distance= (obj.weight_distance);
  let work_of_art = (obj.work_of_art);
  let ord = (obj.ordinal);
  let zed = (obj.zed);

  console.log(date,gpe,org,fac,person,money,weight_distance,work_of_art,ord,zed);

  var x1 = document.getElementById("date");  
  x1.style.color = "red"; 
  x1.innerHTML = date;

  var x2 = document.getElementById("gpe");  
  x2.style.color = "red"; 
  x2.innerHTML = gpe;

  var x3 = document.getElementById("org");  
  x3.style.color = "red"; 
  x3.innerHTML = org;

  var x4 = document.getElementById("fac");  
  x4.style.color = "red"; 
  x4.innerHTML = fac;

  var x5 = document.getElementById("person");  
  x5.style.color = "red"; 
  x5.innerHTML = person;

  var x6 = document.getElementById("money");  
  x6.style.color = "red"; 
  x6.innerHTML = money;

  var x7 = document.getElementById("weigh");  
  x7.style.color = "red"; 
  x7.innerHTML = weight_distance;

  var x8 = document.getElementById("work_of_art");  
  x8.style.color = "red"; 
  x8.innerHTML = work_of_art;

  var x9 = document.getElementById("ord");  
  x9.style.color = "red"; 
  x9.innerHTML = ord;

}

function eraseText() {
  document.getElementById("para").value = "";
  document.getElementById("btn_id").disabled = false;
}