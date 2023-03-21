function ValidateEmail(input) {
  var validRegex =
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

  if (input.value.match(validRegex)) {
    alert("Valid email address!");

    document.form.email.focus();

    return true;
  } else {
    alert("Invalid email address!");

    document.form.email.focus();

    return false;
  }
}
document.getElementById("form").addEventListener("submit", validateForm);
