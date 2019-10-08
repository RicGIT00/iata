document.getElementById("signin").addEventListener("click",function(){
  var id = document.getElementById("your_id").value;
  var senha = document.getElementById("your_pass").value;

  // Login RH validation
  if(id==='am' && senha === '123') {
    location.href='jobs-rh.html';
  } else {
    // Error message
    document.getElementById("error-message").style.display = 'block';    
    
    // Reset id and password value
    id = document.getElementById("your_id").value = '';
    senha = document.getElementById("your_pass").value = '';  
  }
});

// Disable error message when click in input id section
document.getElementById("your_id").addEventListener("click",function(){ 
  document.getElementById("error-message").style.display = 'none';
});