const API_URL = "http://127.0.0.1:5000/students";

let studentsCache = [];
let currentPage = 1;
const studentsPerPage = 5;
let selectedStudentId = null;

function showMessage(text, type = "success") {
    const msg = document.getElementById("message");
    msg.textContent = text;
    msg.className = type;
}


function resetForm() {
    selectedStudentId = null;
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("course").value = "";
    document.getElementById("updateBtn").classList.add("d-none");
    document.getElementById("cancelBtn").classList.add("d-none");
    document.getElementById("addBtn").disabled = false;
    showMessage("");
}

function addStudent() {
    const sname = document.getElementById("name").value.trim();
    const age = document.getElementById("age").value.trim();
    const course = document.getElementById("course").value.trim();

    if (!sname || !age || !course) return showMessage("All fields are required.", "danger");
    if (isNaN(age) || Number(age) <= 0) return showMessage("Age must be valid.", "danger");

    fetch(API_URL, {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ sname, age: Number(age), course })
    })
        .then(res => res.json().then(data => ({ status: res.status, body: data })))
        .then(({ status, body }) => {
            if (status >= 400) showMessage(body.error || "Failed to add student.", "danger");
            else {
                showMessage(body.message || "Student added successfully.", "success");
                resetForm();
                loadStudents();
            }
        })
        .catch(() => showMessage("Something went wrong.", "danger"));
}

function updateStudent() {
    if (!selectedStudentId) return showMessage("No student selected.", "danger");

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
        .then(res => res.json().then(data => ({ status: res.status, body: data })))
        .then(({ status, body }) => {
            if (status >= 400) showMessage(body.error || "Failed to update student.", "danger");
            else {
                showMessage(body.message || "Student updated successfully.", "success");
                resetForm();
                loadStudents();
            }
        })
        .catch(() => showMessage("Something went wrong.", "danger"));
}

function deleteStudent(id) {
    if (!confirm("Are you sure you want to delete this student?")) return;

    fetch(`${API_URL}/${id}`, { method: "DELETE", credentials: "include" })
        .then(res => res.json().then(data => ({ status: res.status, body: data })))
        .then(({ status, body }) => {
            if (status >= 400) showMessage(body.error || "Failed to delete student.", "danger");
            else {
                showMessage(body.message || "Student deleted successfully.", "success");
                loadStudents();
            }
        })
        .catch(() => showMessage("Something went wrong.", "danger"));
}

function loadStudents(sort = "") {
    fetch(`${API_URL}?sort=${sort}`, { credentials: "include" })
        .then(res => res.json())
        .then(data => {
            studentsCache = data;
            currentPage = 1;
            renderTable(data);
        })
        .catch(() => showMessage("Failed to load students.", "danger"));
}

function renderTable(data) {
    const tableBody = document.getElementById("studentTableBody");
    const showingDiv = document.getElementById("showingText");
    tableBody.innerHTML = "";

    const start = (currentPage - 1) * studentsPerPage;
    const end = start + studentsPerPage;
    const studentsToShow = data.slice(start, end);

    if (data.length === 0) {
        showingDiv.textContent = "Showing 0-0 of 0";
        tableBody.innerHTML = `<tr><td colspan="6" class="text-center">No students found</td></tr>`;
        renderPagination(0);
        return;
    }

    showingDiv.textContent = `Showing ${start + 1}-${Math.min(end, data.length)} of ${data.length}`;

    studentsToShow.forEach((s, i) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${start + i + 1}</td>
            <td>${s.sname}</td>
            <td>${s.age}</td>
            <td>${s.course}</td>
            <td>${s.created_at ? new Date(s.created_at).toLocaleDateString() : "-"}</td>
            <td>
                <button class="btn btn-info btn-sm me-1" onclick="editStudent(${s.id}, '${s.sname.replace(/'/g, "\\'")}', ${s.age}, '${s.course.replace(/'/g, "\\'")}')">Edit</button>
                <button class="btn btn-danger btn-sm" onclick="deleteStudent(${s.id})">Delete</button>
            </td>
        `;
        tableBody.appendChild(tr);
    });

    renderPagination(data.length);
}

function renderPagination(total) {
    const totalPages = Math.ceil(total / studentsPerPage);
    const pagination = document.getElementById("pagination");
    pagination.innerHTML = "";

    const prevClass = currentPage === 1 ? "disabled" : "";
    const nextClass = currentPage === totalPages ? "disabled" : "";

    pagination.innerHTML += `<li class="page-item ${prevClass}"><a class="page-link" href="javascript:void(0)" onclick="goToPage(${currentPage - 1})">Prev</a></li>`;

    for (let i = 1; i <= totalPages; i++) {
        pagination.innerHTML += `<li class="page-item ${currentPage === i ? "active" : ""}"><a class="page-link" href="javascript:void(0)" onclick="goToPage(${i})">${i}</a></li>`;
    }

    pagination.innerHTML += `<li class="page-item ${nextClass}"><a class="page-link" href="javascript:void(0)" onclick="goToPage(${currentPage + 1})">Next</a></li>`;
}

function goToPage(p) {
    const totalPages = Math.ceil(studentsCache.length / studentsPerPage);
    if (p < 1 || p > totalPages) return;
    currentPage = p;
    renderTable(studentsCache);
}

function editStudent(id, name, age, course) {
    selectedStudentId = id;
    document.getElementById("name").value = name;
    document.getElementById("age").value = age;
    document.getElementById("course").value = course;

    document.getElementById("updateBtn").classList.remove("d-none");
    document.getElementById("cancelBtn").classList.remove("d-none");
    document.getElementById("addBtn").disabled = true;
    showMessage("");
}

function cancelEdit() {
    resetForm();
}

function logout() {
    if (!confirm("Are you sure you want to logout?")) return;

    fetch("/logout", { method: "POST", credentials: "include" })
        .then(res => {
            if (!res.ok) throw new Error("Logout failed");
            return res.json();
        })
        .then(() => { window.location.href = "/login"; })
        .catch(() => showMessage("Logout failed. Try again.", "danger"));
}

window.onload = loadStudents;
