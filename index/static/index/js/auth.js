//variables
var mobile = document.getElementsByClassName("mobile-input")[0]
var country_code= document.getElementsByClassName("select-js")[0]
var email = document.getElementsByClassName("email-input")[0]
var password = document.getElementsByClassName("password-input")


function register(){
    //check if email or mobile was selected
    
    if (mobile.style.display ==""){
        var contact_type ="mobile"
    }

    else if (mobile.style.display =="block"){
        var contact_type ="mobile"
    }

    else{
        var contact_type ="email"
    }

    var request = new XMLHttpRequest
    request.onload = function(){
        alert(this.responseText)
        
    }
    //alert("email="+email.innerHTML+"&mobile="+mobile+"&password="+password.innerHTML)
    request.open("POST", "/register")
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    if (contact_type=="email"){
        request.send("contact_type="+contact_type+"&email="+email.value+"&password="+password[2].value)
    }
    else{
        request.send("contact_type="+contact_type+"&country_code="+country_code.value+"&mobile="+mobile.value+"&email="+email.value+"&password="+password[2].value)
    }
    
}