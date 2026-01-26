const forgotForm = document.getElementById("forgotForm");
const msgDiv = document.getElementById("msg");

forgotForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    msgDiv.innerHTML = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        msgDiv.innerHTML = `<div class="alert alert-danger">Please fill in all fields.</div>`;
        return;
    }

    try {
        const endpoint = forgotForm.getAttribute("action");
        const response = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, new_password: password })
        });

        const data = await response.json();

        if (response.ok) {
            msgDiv.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
            setTimeout(() => { window.location.href = "/login"; }, 1000);
        } else {
            msgDiv.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
        }
    } catch (err) {
        console.error(err);
        msgDiv.innerHTML = `<div class="alert alert-danger">Something went wrong. Try again.</div>`;
    }
});