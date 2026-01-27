const loginForm = document.getElementById("loginForm");
const loginMsg = document.getElementById("msg");

loginForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    loginMsg.textContent = "";
    loginMsg.className = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        loginMsg.textContent = "Both fields are required.";
        loginMsg.className = "alert alert-danger";
        return;
    }

    try {
        const endpoint = loginForm.getAttribute("action");

        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            window.location.href = "/dashboard";
        } else if (data.error) {
            loginMsg.textContent = data.error;
            loginMsg.className = "alert alert-danger";
        } else {
            loginMsg.textContent = "Login failed. Try again.";
            loginMsg.className = "alert alert-danger";
        }
    } catch (err) {
        console.error(err);
        loginMsg.textContent = "Something went wrong. Try again.";
        loginMsg.className = "alert alert-danger";
    }
});