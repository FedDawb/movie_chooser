$('.responsive').slick({
  // centerMode: true,
  // centerPadding: '60px',
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 5,
    slidesToScroll: 5,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
            arrows: false,
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
            arrows: false,
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

/*
  document.querySelector(`#button`).addEventListener('click', function(e){
      alert('Hello Bex');
      console.log(e)
  });

document.querySelectorAll('.btn-outline-success').forEach(elm => {
      elm.addEventListener('click', e=>{
        let title=elm.closest('div').querySelector('p >b').innerHTML;
        alert(`I clicked on ${title}`)
      })
})
*/