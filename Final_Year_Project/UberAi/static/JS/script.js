// const image = document.getElementById("login_page_image");


// image.style.position = 'fixed';
// image.style.left = '1300px';

// step = 1300 ; 
// test = setInterval(function () {
//     step -= 5;
//     image.style.left = step+"px";
//     if(step == 700){
//         clearInterval(test);
//     }
// },0.001);

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
}