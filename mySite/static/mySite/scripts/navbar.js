const nav = document.querySelector('#NavBar');
const logo = document.querySelector('#logo');
var click = 0;
function logo_large() {
    logo.style.width = '200px';
    logo.style.transitionDuration = "500ms";
}

function logo_medium() {
    logo.style.width = '120px';
    logo.style.transitionDuration = "500ms";
}

function logo_small() {
    logo.style.width = '60px';
    logo.style.transitionDuration = "500ms";
}

function navScrollPos(){
    let dy = document.documentElement.scrollTop;
    let w = window.innerWidth;

    if (dy > 200 ) {
        // Add background color only on the home pg navbar since it's transparent at first
        nav.classList.add('nav-color');
        logo_small();

        if(w > 990) {
            nav.style.height = '80px';
        } else {
            nav.style.height = '';
        }
    } else {
        // Remove the navbar background color on home when it's back on top to make it transparent again.
        if(click % 2 === 0) {
            nav.classList.remove('nav-color');
            if(w < 568){
                logo_medium()
            }else{
                logo_large()
            }
        }
        if(w > 990) {
            nav.style.height = '';
        }
    }
}
// Change navbar color and size depending on url path and scroll height
document.addEventListener('scroll', navScrollPos);

// Check navbar background color is correct and Logo size is correct when called
function ww_check(){
    let dy = document.documentElement.scrollTop;
    let w = window.innerWidth;

    if (w < 990 && dy > 200){
        nav.classList.add('nav-color');
        nav.style.height = '';
        if(w < 568){
            logo_medium()
        }else{
            logo_large()
        }

    }else{
        nav.classList.remove('nav-color');
        logo_large()
    }
    navScrollPos();
}

// Adding resize listener to the path_ww_check function
window.addEventListener('resize', ww_check);

window.addEventListener('load', () => {
    ww_check();
    // Give collapsed navbar a background when it is clicked to open the navbar.
    // and remove the background color when it is clicked to close the nav bar.
    // But only do this on the home page where the navbar is transparent to begin with.

    document.querySelector('#MenuBtn').onclick = () => {
        let dy = document.documentElement.scrollTop;
        let w = window.innerWidth;
        click++;
        if(w > 990 || dy < 200){
            if(click % 2 === 1){
                nav.classList.add('nav-color');
                logo_small()
            }else{
                nav.classList.remove('nav-color');
                logo_medium()
            }
        }
    };
});