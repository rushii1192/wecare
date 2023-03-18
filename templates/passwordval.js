function Checkpassword(input) {
  var passw = /^[A-Za-z]\w{7,14}$/;

  if (input.value.match(passw)) {
    alert("Valid password!");

    document.form.password.focus();

    return true;
  } else {
    alert("Invalid password!");

    document.form.password.focus();

    return false;
  }
}

document.getElementById("form").addEventListener("submit", validateForm);
