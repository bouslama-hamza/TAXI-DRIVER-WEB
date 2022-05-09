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