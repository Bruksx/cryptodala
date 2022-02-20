const select = document.querySelector('.select-js')


fetch('/static/index/js/countries.json')
  .then((response) => response.json())
  .then((data) => {
      let countries = data.countries
      let output = ''
      countries.forEach((country)=>{
         output+= `
          <option>${country.code}</option>
         `
      })
      select.innerHTML = output
  });

  //Email and mobile functionality
  const emailOption = document.querySelector('.email-option');
  const mobileOption = document.querySelector('.mobile-option');

  emailOption.addEventListener('click', ()=>{
    emailOption.style.backgroundColor = 'black';
    emailOption.style.color = 'gold';

    mobileOption.style.backgroundColor = 'rgb(214, 212, 209)';
    mobileOption.style.color = 'rgb(150, 142, 142)';

    const selectElement = document.querySelector('.select-js').style.display = 'none';
    const mobileInput = document.querySelector('.mobile-input').style.display = 'none';

    const email = document.querySelector('.email-input').style.display = 'block'
  });

  mobileOption.addEventListener('click', ()=>{
    mobileOption.style.backgroundColor = 'black';
    mobileOption.style.color = 'gold';

    emailOption.style.backgroundColor = 'rgb(214, 212, 209)';
    emailOption.style.color = 'rgb(150, 142, 142)';

    const selectElement = document.querySelector('.select-js').style.display = 'block';
    const mobileInput = document.querySelector('.mobile-input').style.display = 'block';

    const email = document.querySelector('.email-input').style.display = 'none'
  });


