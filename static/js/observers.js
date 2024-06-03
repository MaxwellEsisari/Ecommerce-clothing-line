const header = document.querySelector("header");
const sectionOne = document.querySelector(".intro-section");

const sectionOneOptions = {
  rootMargin: "-200px 0px 0px 0px"
};

const sectionOneObserver = new IntersectionObserver(function(
  entries,
  sectionOneObserver
) {
  entries.forEach(entry => {
    if (!entry.isIntersecting) {
      header.classList.add("nav-scrolled");
    } else {
      header.classList.remove("nav-scrolled");
    }
  });
},
sectionOneOptions);

sectionOneObserver.observe(sectionOne);


function setNewImage(){
  var imag = document.getElementById("img1")
  imag.src="img/yeezyslides.jpg";
}

function setOldImage(){
  var imag = document.getElementById("img1")
  imag.src="img/yeezyslides2.jpg";
}

let slider = tns({
  container : ".my-favorite-slide",
  "slideBy" : "1",
  "speed" : 400,
  "nav" : false,
  autoplay :true,
  controls: false,
  autoplayButtonOutput : false,

  responsive :{
    1600:{
      items :4,
      gutter: 20
    },
    1024:{
      items :3,
      gutter :20
    },
    768:{
      items :2,
      gutter :20
    },
    480:{
      items :1,
      gutter :20
    },
  }

})

