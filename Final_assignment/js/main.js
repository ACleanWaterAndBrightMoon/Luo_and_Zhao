$(document).ready(function () {
  var mySwiper = new Swiper(".swiper-container", {
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    speed: 800,
    direction: "horizontal",
    loop: true,
    effect: "fade",
    observer: true,
    observeParents: true,
    // 如果需要分页器
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    // 如果需要前进后退按钮
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  var mybottomSwiper3 = new Swiper(".swiper-container-bottom3", {
    autoplay: true,
    speed: 1000, //可选选项，自动滑动
    effect: "flip",
  });
  var mybottomSwiper1 = new Swiper(".swiper-container-bottom1", {
    autoplay: true,
    speed: 2000,
    effect: "fade",
  });
  var mybottomSwiper2 = new Swiper(".swiper-container-bottom2", {
    autoplay: true,
    speed: 2500,
    effect: "cube",
  });
  var mybottomSwiper = new Swiper(".swiper-container-bottom", {
    autoplay: true,
    loop: true,
    direction: "vertical",
    slidesPerView: 1,
    speed: 1500,
  });
  $(window).scroll(function () {
    if ($(document).scrollTop() >= 400) {
      $(".side-button-top").css("display", "block");
      $(".side-button-bottom").css("display", "block");
    }
    if ($(document).scrollTop() < 400) {
      $(".side-button-top").css("display", "none");
      $(".side-button-bottom").css("display", "none");
    }
  });
  $(".side-button-top").click(function () {
    $("html,body").animate({ scrollTop: 0 }, 500);
  });
  $(".side-button-bottom").click(function () {
    $("html,body").animate({ scrollTop: document.body.scrollHeight }, 500);
  });
  var p = 0,
    t = 0;

  $(window).scroll(function (e) {
    p = $(document).scrollTop();

    if (t <= p && p > 60) {
      //向下滚
      $("nav[name='change-navbar']").fadeOut(500);
    } else if (t <= p && p <= 60) {
      $("nav[name='change-navbar']").css({
        position: "fixed",
        top: 0,
        left: 0,
      });
    } else if (t >= p && p <= 60) {
      //向上滚
      $("nav[name='change-navbar']").css({
        position: "absolute",
        top: "auto",
      });
    } else {
      $("nav[name='change-navbar']").fadeIn(500);
    }
    setTimeout(function () {
      t = p;
    }, 0);
  });
});
