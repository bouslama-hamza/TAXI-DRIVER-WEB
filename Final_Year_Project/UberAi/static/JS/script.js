function rool_left(position , step_position){
    const image = document.getElementById("page_image");
    image.style.position = 'fixed';
    image.style.left = position+"px";
    step = position ; 
    test = setInterval(function () {
        step -= 15;
        image.style.left = step+"px";
        if(step == step_position){
            clearInterval(test);
        }
    },0.001);
    image.style.position = 'absolute';
}

function rool_right(position , step_position){
    const image = document.getElementById("page_image");
    image.style.position = 'fixed';
    image.style.left = position+"px";
    step = position ; 
    test = setInterval(function () {
        step += 15;
        image.style.left = step+"px";
        if(step == step_position){
            clearInterval(test);
        }
    },0.001);
    image.style.position = 'absolute';
}

function show(){
    const bar = document.getElementById("app_setting_info")
    bar.classList.toggle('active')
}

window.onscroll = function() {myFunction()};
var header = document.getElementById("app_content_header");
var sticky = header.offsetTop;


function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

const div = document.querySelector(".app_table_data")
const latest = document.querySelector(".value_number")
const confidence = document.getElementById("confidence")
const deconfidence = document.getElementById("marge")
const total_number = document.querySelector(".total_number")

var currenttimeUnix = (new Date()).getTime() 
const CallBackTimeInMS = 5000;

setInterval("getnewData()",1000)
function getnewData(){
    new_time = (new Date()).getTime() 
    if(new_time-currenttimeUnix<CallBackTimeInMS) return
    currenttimeUnix = new_time
    var request = new XMLHttpRequest()
    request.open('POST','',true)
    request.setRequestHeader("Access-Control-Allow-Origin", "*");
    request.setRequestHeader("Content-Type",'application/json')
    request.open('POST', `http://127.0.0.1:8000/dashboard/detection`)
    request.onload = () => {
        var data = request.responseText
        if(JSON.stringify(data)){
            new_data = JSON.parse(data)
            latest.innerHTML = new_data['latest']
            confidence.innerHTML = new_data['confidence']+"%"
            deconfidence.innerHTML = new_data['deconfidence']+"%"
            total_number.innerHTML = new_data['total'] + "P"
            div.innerHTML = "";
            for (const data of new_data["data"]) {
                var innerdiv = document.createElement("DIV");
                innerdiv.style.height = " 7.5%;"
                innerdiv.classList.add("app_table_content")
                var child1 = document.createElement("DIV")
                child1.setAttribute("padding-left"," 10px;")
                child1.classList.add("app_data")
                child1.innerText=data["date"]
                var child2 = document.createElement("DIV")
                child2.setAttribute("padding-left"," 15px;")
                child2.classList.add("app_data")
                child2.innerText=data["hour"]
                var child3 = document.createElement("DIV")
                child3.setAttribute("padding-left"," 20px;")
                child3.classList.add("app_data")
                child3.innerText=data["type"]
                var child4 = document.createElement("DIV")
                child4.setAttribute("padding-left"," 25px;")
                child4.classList.add("app_data")
                child4.innerText=data["confidence"]
                innerdiv.appendChild(child1)
                innerdiv.appendChild(child2)
                innerdiv.appendChild(child3)
                innerdiv.appendChild(child4)
                div.appendChild(innerdiv)
            }
        }}
    request.send()
}