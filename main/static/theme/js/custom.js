$(function ($) {
    "use strict"

    
   /* Offset start */
	var html_body = $('html, body'),
  nav = $('nav'),
  navOffset = nav.offset().top,
  $window = $(window);
/* offset ends */



    // baner Slider
    $('.banner_info').slick({
        dots: false,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear',
        slidesToShow:1,
        slidesToScroll: 1,
        responsive: [
          {
            breakpoint: 940,
            settings: {
              arrows:false,
            }
          }
        ]
      });
      // tur slider 
      
      
    // baner Slider
    $('.banner_info2').slick({
        dots: false,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear', 
        slidesToShow:1,
        slidesToScroll: 1,       
        responsive: [
          {
            breakpoint: 991,
            settings: {
              arrows:false,
            }
          }
        ]
      });
      // tur slider  

    $('.tur-slider').slick({
      
        slidesToShow:3,
        slidesToScroll: 1,
        autoplay:true,
        arrows:true,
        dot:false,
        speed:1000,      
        responsive: [
          {
            breakpoint: 1350,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              arrows:false,
              infinite: true
            }
          },
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              arrows:false,
              infinite: true,
            }
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              arrows:false
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              arrows:false
            }
          },
          {
            breakpoint: 500,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows:false
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
        ]
      });

      //top travel slider

    $('.top-t-slider').slick({
      
        slidesToShow:3,
        slidesToScroll: 1,
        autoplay:true,
        arrows:true,
        dot:false,
        speed:1000,      
        responsive: [
          {
            breakpoint: 1350,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              arrows:false,
              infinite: true
            }
          },
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 1,
              arrows:false,
              infinite: true,
            }
          },
          {
            breakpoint: 992,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              arrows:false
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 1,
              arrows:false
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1,
              arrows:false
            }
          }
          // You can unslick at a given breakpoint now by adding:
          // settings: "unslick"
          // instead of a settings object
        ]
      });
// veno box light box plugin
$('.venobox').venobox(); 

    /*---------------------------------------------------
            Click To Top
        ----------------------------------------------------*/
    $(document).on('click', '.totop a[href=#top]', function () {

        $('body,html').animate({

            scrollTop: 0

        }, 600);

        return false;

    });

    jQuery(window).on('scroll', function () {

        /*---------------------------------------------------
            Click To Top
        ----------------------------------------------------*/
        var $scrollTopSelector = $('.totop');
        if ($(this).scrollTop() > 550) {
            $scrollTopSelector.fadeIn();
        } else {
            $scrollTopSelector.fadeOut();
        }

    })
    jQuery(window).on('load', function () {

        /*---------------------------------------------------
            Site Preloader
        ----------------------------------------------------*/
        var $sitePreloaderSelector = $('.site-preloader');
        $sitePreloaderSelector.fadeOut(500);


    });



});


//Project             : Velra - Travel Transport Business Template.
//Version             : 1.0
//Author              : Thesoftking
//Front-end developer : Mamunur Rashid