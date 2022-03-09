const modal = document.querySelector('.buy-modal');
const sellButton = document.querySelector('.sell-button-click');
const sellModal = document.querySelector('.selling-modal');
const closeSell = document.querySelector('.close-sell');
const hamburger = document.querySelector('.hamburger-menu');
const buyModal = document.querySelector('.buy-button-click');
const close = document.querySelector('.close');
const buyMdal = document.querySelector('.button-click');
const sellBtton = document.querySelector('.button-sell-click');

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

  /*profile form*/
  const changeDetails = document.querySelector('.change-details');

  changeDetails.addEventListener('click', ()=>{
    const profileForm = document.querySelector('.profile-form');
    profileForm.style.display = 'block'
    const closeForm = document.querySelector('.close-form');
    closeForm.addEventListener('click', ()=>{
        const profileForm = document.querySelector('.profile-form');
        profileForm.style.display = 'none'
    })
  })

  /*Help and support*/
  const helpSupport = document.querySelector('.help-support');

  helpSupport.addEventListener('click', ()=>{
    const helpButton = document.querySelector('.help-button');
    helpButton.style.display = 'block'
    const closeHelp = document.querySelector('.close-help');
    closeHelp.addEventListener('click', ()=>{
        const helpButton = document.querySelector('.help-button');
        helpButton.style.display = 'none'
    })
  })

  /*Verification Image */
  const verifyImage = document.querySelector('.verify-profile');

  verifyImage.addEventListener('click', ()=>{
    const verifyButton = document.querySelector('.verify-button');
    verifyButton.style.display = 'block'
    const closeVerify = document.querySelector('.close-verify');
    closeVerify.addEventListener('click', ()=>{
        const verifyButton = document.querySelector('.verify-button');
       verifyButton.style.display = 'none'
    })
  })
  /*profile form ends */

  /*Checked state*/
  const checkedNotif = document.querySelector('.notification-checked');
  checkedNotif.addEventListener('click', ()=>{
    if(checkedNotif.checked === true){
        let passwordHashed = document.querySelector('.hashed');
        let passwordNon = document.querySelector('.non-hashed');
        passwordHashed.style.display = 'block'
        passwordNon.style.display = 'none'
    } else if(checkedNotif.checked === false){
        let passwordHashed = document.querySelector('.hashed');
        let passwordNon = document.querySelector('.non-hashed');
        passwordHashed.style.display = 'none'
        passwordNon.style.display = 'block'
    }  
  })

  //verification button
  const verifyButton = document.querySelector('.verification-button');
  let verifyCount = true
  verifyButton.addEventListener('click', ()=>{
      let verificationModal = document.querySelector('.verification-drop-down');
      if(verifyCount === true){
        verificationModal.style.display = 'block';
        verifyCount = false;
      } else if(verifyCount === false){
        verificationModal.style.display = 'none';
        verifyCount = true;
      }

      let close = document.querySelector('.close-help-verification');
      close.addEventListener('click', ()=>{
        let verificationModal = document.querySelector('.verification-drop-down');
        verificationModal.style.display = 'none';
      })
  })

 //
 const settingButton = document.querySelector('.settings-button');
 let settingCount = true
 settingButton.addEventListener('click', ()=>{
     let settingModal = document.querySelector('.notification-setting');
     if(settingCount === true){
       settingModal.style.display = 'block';
       settingCount = false;
     } else if(settingCount === false){
       settingModal.style.display = 'none';
       settingCount = true;
     }
 })
