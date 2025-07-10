document.addEventListener("DOMContentLoaded", function () {
    // Get modal elements
    const seekerLoginModal = new bootstrap.Modal(document.getElementById("seekerLoginModal"));
    const seekerRegisterModal = new bootstrap.Modal(document.getElementById("seekerRegisterModal"));

    // Register link in login modal
    document.querySelector("#seekerLoginModal p a").addEventListener("click", function (event) {
        event.preventDefault();
        seekerLoginModal.hide();
        setTimeout(() => seekerRegisterModal.show(), 500);
    });

    // Login link in register modal
    document.querySelector("#seekerRegisterModal p a").addEventListener("click", function (event) {
        event.preventDefault();
        seekerRegisterModal.hide();
        setTimeout(() => seekerLoginModal.show(), 500);
    });
});