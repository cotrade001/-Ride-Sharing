document.addEventListener("DOMContentLoaded", function () {
    // Get the links and modals
    let registerLink = document.querySelector("#userLoginModal a.text-decoration-none");
    let loginLink = document.querySelector("#userRegisterModal a");

    let loginModal = new bootstrap.Modal(document.getElementById("userLoginModal"));
    let registerModal = new bootstrap.Modal(document.getElementById("userRegisterModal"));

    // When "Register here" is clicked, hide login modal and show register modal
    registerLink.addEventListener("click", function (event) {
        event.preventDefault();
        loginModal.hide();
        setTimeout(() => registerModal.show(), 500); // Delay to allow smooth transition
    });

    // When "Login" is clicked, hide register modal and show login modal
    loginLink.addEventListener("click", function (event) {
        event.preventDefault();
        registerModal.hide();
        setTimeout(() => loginModal.show(), 500); // Delay to allow smooth transition
    });
});
