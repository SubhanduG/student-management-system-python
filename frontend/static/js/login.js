const loginForm = document.getElementById("loginForm");
const loginMsg = document.getElementById("msg");

loginForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    loginMsg.innerHTML = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    try {
        const endpoint = loginForm.getAttribute("action");
        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            window.location.href = "/dashboard";
        } else {
            loginMsg.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        }
    } catch (err) {
        console.error(err);
        loginMsg.innerHTML = `<div class="alert alert-danger">Something went wrong. Try again.</div>`;
    }
});