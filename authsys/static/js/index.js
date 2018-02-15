function showPassword() {

    //document.getElementById("check").style.visibility = "hidden";
    var key_attr = $('#password').attr('type');
    
    if(key_attr != 'text') {
        
        $('.checkbox').addClass('show');
        $('#password').attr('type', 'text');
        
    } else {
        
        $('.checkbox').removeClass('show');
        $('#password').attr('type', 'password');
        
    }
    
}

function checkPasswords() {
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    if (password1 !== password2){
        //alert("unequal");
        document.getElementById("btn-login").disabled = true;
        document.getElementById("password2").style.border = "2px solid #ff00003d";
    }else {
        document.getElementById("password2").style.border = "1px solid #ccc";
        document.getElementById("btn-login").disabled = false;
    }

}