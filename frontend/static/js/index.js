const API_URL = "http://127.0.0.1:5000/students";

function logout() {
    if (!confirm("Are you sure you want to logout?")) return;

    fetch("/logout", { method: "POST", credentials: "include" })
        .then(res => res.json())
        .then(() => { window.location.href = "/login"; })
        .catch(() => alert("Logout failed. Try again."));
}

function showMessage(text, color = "success") {
    const msg = document.getElementById("message");
    msg.innerText = text;
    msg.className = `mt-3 fw-bold text-${color}`;
}

function addStudent() {
    const sname = document.getElementById("name").value.trim();
    const age = document.getElementById("age").value.trim();
    const course = document.getElementById("course").value.trim();

    if (!sname || !age || !course) {
        showMessage("All fields are required.", "danger");
        return;
    }

    if (isNaN(age) || Number(age) <= 0) {
        showMessage("Age must be valid.", "danger");
        return;
    }

    fetch(API_URL, {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sname, age: Number(age), course })
    })
        .then(res => res.json())
        .then(() => {
            showMessage("Student added successfully.");
            loadStudents();
        })
        .catch(() => showMessage("Failed to add student.", "danger"));
}

let studentsCache = [];
let currentPage = 1;
const studentsPerPage = 5;

function loadStudents(sort = "") {
    fetch(`${API_URL}?sort=${sort}`, { credentials: "include" })
        .then(res => res.json())
        .then(data => {
            studentsCache = data;
            currentPage = 1;
            renderTable(data);
        });
}

function renderTable(data) {
    const tableBody = document.getElementById("studentTableBody");
    tableBody.innerHTML = "";

    const start = (currentPage - 1) * studentsPerPage;
    const end = start + studentsPerPage;
    const studentsToShow = data.slice(start, end);

    const showingDiv = document.getElementById("showingText");
    if (data.length === 0) {
        showingDiv.innerText = "Showing 0-0 of 0";
        tableBody.innerHTML = `<tr><td colspan="6">No students found</td></tr>`;
        return;
    } else {
        showingDiv.innerText = `Showing ${start + 1}-${Math.min(end, data.length)} of ${data.length}`;
    }

    studentsToShow.forEach((s, i) => {
        tableBody.innerHTML += `
            <tr>
                <td>${start + i + 1}</td>
                <td>${s.name}</td>
                <td>${s.age}</td>
                <td>${s.course}</td>
                <td>${new Date(s.created_at).toLocaleDateString()}</td>
                <td>
                    <button class="btn-info" onclick="editStudent(${s.id}, '${s.name}', ${s.age}, '${s.course}')">Edit</button>
                    <button class="btn-danger" onclick="deleteStudent(${s.id})">Delete</button>
                </td>
            </tr>`;
    });

    renderPagination(data.length);
}

function renderPagination(total) {
    const totalPages = Math.ceil(total / studentsPerPage);
    const pagination = document.getElementById("pagination");
    pagination.innerHTML = "";

    pagination.innerHTML += `<li class="${currentPage === 1 ? 'disabled' : ''}"><a href="#" onclick="goToPage(${currentPage - 1})">Prev</a></li>`;
    for (let i = 1; i <= totalPages; i++) {
        pagination.innerHTML += `<li class="${currentPage === i ? 'active' : ''}"><a href="#" onclick="goToPage(${i})">${i}</a></li>`;
    }
    pagination.innerHTML += `<li class="${currentPage === totalPages ? 'disabled' : ''}"><a href="#" onclick="goToPage(${currentPage + 1})">Next</a></li>`;
}

function goToPage(p) {
    const totalPages = Math.ceil(studentsCache.length / studentsPerPage);
    if (p < 1 || p > totalPages) return;
    currentPage = p;
    renderTable(studentsCache);
}

let selectedStudentId = null;

function editStudent(id, name, age, course) {
    selectedStudentId = id;
    document.getElementById("name").value = name;
    document.getElementById("age").value = age;
    document.getElementById("course").value = course;

    document.getElementById("updateBtn").classList.remove("d-none");
    document.getElementById("cancelBtn").classList.remove("d-none");
    document.getElementById("addBtn").disabled = true;
}

function cancelEdit() {
    selectedStudentId = null;
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("course").value = "";
    document.getElementById("updateBtn").classList.add("d-none");
    document.getElementById("cancelBtn").classList.add("d-none");
    document.getElementById("addBtn").disabled = false;
    document.getElementById("message").innerText = "";
}

function updateStudent() {
    if (!selectedStudentId) return alert("No student selected");

    const sname = document.getElementById("name").value.trim();
    const age = document.getElementById("age").value.trim();
    const course = document.getElementById("course").value.trim();

    if (!sname || !age || !course) return showMessage("All fields are required.", "danger");
    if (isNaN(age) || Number(age) <= 0) return showMessage("Age must be valid.", "danger");

    fetch(`${API_URL}/${selectedStudentId}`, {
        method: "PUT",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sname, age: Number(age), course })
    })
        .then(res => res.json())
        .then(data => {
            if (data.error) return showMessage(data.error, "danger");
            showMessage(data.message, "success");
            cancelEdit();
            loadStudents();
        })
        .catch(() => showMessage("Something went wrong", "danger"));
}

function deleteStudent(id) {
    if (!confirm("Are you sure?")) return;
    fetch(`${API_URL}/${id}`, { method: "DELETE", credentials: "include" })
        .then(res => res.json())
        .then(() => loadStudents());
}

window.onload = loadStudents;