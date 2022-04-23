const image = document.getElementById("login_page_image");

image.style.position = 'fixed';
image.style.left = '1300px';

step = 1300 ; 
test = setInterval(function () {
    step -= 5;
    image.style.left = step+"px";
    if(step == 700){
        clearInterval(test);
    }
},0.001);