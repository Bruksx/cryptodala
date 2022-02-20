//Declaration of variables
const modal = document.querySelector('.buy-modal');
const sellModal = document.querySelector('.selling-modal');
const buyModal = document.querySelector('.buy-button-click');
const buyMdal = document.querySelector('.button-click');
const sellBtton = document.querySelector('.button-sell-click');
const sellButton = document.querySelector('.sell-button-click');
const close = document.querySelector('.close');
const closeSell = document.querySelector('.close-sell');
const hamburger = document.querySelector('.hamburger-menu');
const buyControl = document.querySelector('.buy-control');
const sellControl = document.querySelector('.sell-control');


//Show or hide User profile
/*const userImage = document.querySelector('.user-img');
userImage.addEventListener('click', ()=>{
    let menuBar = document.querySelector('.menu-bar');

    menuBar.style.right = '-100%';
    let spa = document.querySelector('.spa-1').style.display = 'none';
    let spaMarket = document.querySelector('.spa-market').style.display = 'none';
    let signup = document.querySelector('.sign-up-cont').style.display = 'nonr';
    let signin = document.querySelector('.sign-in-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'block'
}) */

//User Menu List
const userMenu = document.querySelector('.triangle-down');
let userMenuOpen = false
userMenu.addEventListener('click', ()=>{
   let menuBar = document.querySelector('.user-menu-bar');
   if(userMenuOpen === false){
       menuBar.style.display = 'block'
       userMenuOpen = true;
   } else{
    menuBar.style.display = 'none'
    userMenuOpen = false;
   }
})

//Buy and Sell
buyControl.addEventListener('click', ()=>{
    modal.style.display = 'block';

    let sell = document.querySelector('.sell-toggle');
    sell.addEventListener('click', ()=>{
        let sell = document.querySelector('.sell-toggle');
        let buy = document.querySelector('.buy-toggle');

        buy.style.backgroundColor = '#FFD700';
        buy.style.color = "black"
      
        sell.style.backgroundColor = "black";
        sell.style.color = "#FFD700"

        let sellModalPay = document.querySelector('.sell-modal-pay');
        let sellModalBuy = document.querySelector('.sell-modal-buy');

        sellModalPay.textContent = 'SELL'
        sellModalBuy.textContent = 'RECEIVE'

        buy.addEventListener('click', ()=>{
        let sell = document.querySelector('.sell-toggle');
        let buy = document.querySelector('.buy-toggle');

        buy.style.backgroundColor = 'black';
        buy.style.color = "#FFD700"
      
        sell.style.backgroundColor = "#FFD700";
        sell.style.color = "black"

        let sellModalPay = document.querySelector('.sell-modal-pay');
        let sellModalBuy = document.querySelector('.sell-modal-buy');

        sellModalPay.textContent = 'PAY'
        sellModalBuy.textContent = 'BUY'
        })
    })
})

sellControl.addEventListener('click', ()=>{
    sellModal.style.display = 'block'

    let buy = document.querySelector('#buy-toggle');
    
        buy.addEventListener('click', ()=>{
        let sell = document.querySelector('#sell-toggle');
        let buy = document.querySelector('#buy-toggle');

        buy.style.backgroundColor = 'black';
        buy.style.color = "#FFD700"
      
        sell.style.backgroundColor = "#FFD700";
        sell.style.color = "black"

        let sellModalPay = document.querySelector('.sell-modal-sell');
        let sellModalBuy = document.querySelector('.sell-modal-receive');

        sellModalPay.textContent = 'PAY';
        sellModalBuy.textContent = 'BUY';

        sell.addEventListener('click', ()=>{
            let sell = document.querySelector('#sell-toggle');
            let buy = document.querySelector('#buy-toggle');
    
            buy.style.backgroundColor = '#FFD700';
            buy.style.color = "black"
          
            sell.style.backgroundColor = "black";
            sell.style.color = "#FFD700"
    
            let sellModalPay = document.querySelector('.sell-modal-sell');
            let sellModalBuy = document.querySelector('.sell-modal-receive');
    
            sellModalPay.textContent = 'SELL'
            sellModalBuy.textContent = 'RECEIVE'
        })
        })
    })

buyMdal.addEventListener('click', ()=>{
    let menuBar = document.querySelector('.menu-bar');

    menuBar.style.right = '-100%';
    modal.style.display = 'block';
    open = false
})

sellBtton.addEventListener('click', ()=>{
    let menuBar = document.querySelector('.menu-bar');

        menuBar.style.right = '-100%';
    sellModal.style.display = 'block'
    open = false
})

buyModal.addEventListener('click', ()=>{
    modal.style.display = 'block'
})

close.addEventListener('click', ()=>{
    modal.style.display = 'none'
})

sellButton.addEventListener('click', ()=>{
    sellModal.style.display = 'block'
})

closeSell.addEventListener('click', ()=>{
    sellModal.style.display = 'none'
})


let open = false
hamburger.addEventListener('click', ()=>{
    if(open === false){
    let menuBar = document.querySelector('.menu-bar');

    menuBar.style.right = '0%';
    
     open = true;
    } else if(open === true){
        let menuBar = document.querySelector('.menu-bar');

        menuBar.style.right = '-100%';
         open = false
    }
})

//SPA FOR SIGNIN
const signInButton = document.querySelector('.sign-in-button');
signInButton.addEventListener('click', ()=>{
    let spa = document.querySelector('.spa-1').style.display = 'none';
    let spaMarket = document.querySelector('.spa-market').style.display = 'none';
    let signIn = document.querySelector('.sign-in-cont').style.display = 'block';
    let signup = document.querySelector('.sign-up-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
    
});

//SPA FOR SIGNUP
const signUpButton = document.querySelector('.sign-up-button');
signUpButton.addEventListener('click', ()=>{
    let spa = document.querySelector('.spa-1').style.display = 'none';
    let spaMarket = document.querySelector('.spa-market').style.display = 'none';
    let signup = document.querySelector('.sign-up-cont').style.display = 'block';
    let signin = document.querySelector('.sign-in-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
})

//SPA FOR HOME
const homeButton = document.querySelector('.home');
homeButton.addEventListener('click', ()=>{
    let spa = document.querySelector('.spa-1').style.display = 'block';
    let spaMarket = document.querySelector('.spa-market').style.display = 'block';
    let signup = document.querySelector('.sign-up-cont').style.display = 'none';
    let signin = document.querySelector('.sign-in-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
})

const homeBtn = document.querySelector('.index');
homeBtn.addEventListener('click', ()=>{
    let spa = document.querySelector('.spa-1').style.display = 'block';
    let spaMarket = document.querySelector('.spa-market').style.display = 'block';
    let signup = document.querySelector('.sign-up-cont').style.display = 'none';
    let signin = document.querySelector('.sign-in-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
})


const signInBtn = document.querySelector('.sign-in-btn');
signInBtn.addEventListener('click', ()=>{
    let menuBar = document.querySelector('.menu-bar');

    menuBar.style.right = '-100%';
    let spa = document.querySelector('.spa-1').style.display = 'none';
    let spaMarket = document.querySelector('.spa-market').style.display = 'none';
    let signIn = document.querySelector('.sign-in-cont').style.display = 'block';
    let signup = document.querySelector('.sign-up-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
    
});

//SPA FOR SIGNUP
const signUpBtn = document.querySelector('.sign-up-btn');
console.log(signUpBtn);
signUpBtn.addEventListener('click', ()=>{
    let menuBar = document.querySelector('.menu-bar');

    menuBar.style.right = '-100%';
    let spa = document.querySelector('.spa-1').style.display = 'none';
    let spaMarket = document.querySelector('.spa-market').style.display = 'none';
    let signup = document.querySelector('.sign-up-cont').style.display = 'block';
    let signin = document.querySelector('.sign-in-cont').style.display = 'none';
    let profile = document.querySelector('.profile').style.display = 'none'
})

//SwiperJS
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 'auto',
    spaceBetween: 90,
    centeredSlides: true,
    grabCursor: true,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

/*Integrating coins to UI
 fetch("http://api.coinlayer.com/api/list?access_key=933cbf217cacff6efbee47f534cdc1f6")
 .then((response) => response.json())
 .then((data) => {
  console.log(data);
  let cryptoData = data.crypto;
  let coinbtc = document.querySelector('.coin-btc');
  coinbtc.innerHTML = cryptoData.BTC.name
  let coinCircle = document.querySelector('.circle-btc');
  let imageBtc = cryptoData.BTC.icon_url;
  coinCircle.style.backgroundImage = `url(${imageBtc})`
 })

 /*fetch('http://api.coinlayer.com/api/live?access_key=933cbf217cacff6efbee47f534cdc1f6')
 .then((response)=>response.json())
 .then(data => {
     let btcPrice = data.rates.BTC;
     let priceBtc = document.querySelector('.btc-price');
     priceBtc.innerHTML = btcPrice.toFixed(2)
 })*/