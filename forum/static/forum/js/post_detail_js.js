document.addEventListener('DOMContentLoaded', () => {

    /* JS ktory zobrazuje form, django ifmi je zabezpecene aby sa ukazal iba ked je user prihlaseny,
            taktiez je zabezpecene aby aj ked sa user dostane do otvorenej form ako neprihlaseny, tak po stlaceni
            submitu sa vo view dekoracnou anotaciou zabezpeci ze ak neni prihlaseny tak bude presmerovany na login
            ktory je uvedeny v settings.py */
    document.getElementById('reply-btn').addEventListener('click', () => {
        const replyForm = document.getElementById('reply-form');
        if (replyForm.style.display === 'none' || replyForm.style.display === '') {
            replyForm.style.display = 'block';
        } else {
            replyForm.style.display = 'none';
        }
    });


    /* modalne edit comment okno */

    const editButtons = document.querySelectorAll('.partial-li-comment-edit-button');
    const editModal = document.getElementById("id-edit-modal");
    const closeBtn = document.getElementById("id-btn-close-modal");
    const editModalInput = document.getElementById("id-edit-modal-input");
    const saveBtn = document.getElementById("id-btn-save-edit-modal");
    let commentId;
    editButtons.forEach((button) => {
        button.addEventListener("click", () => {
            editModal.classList.add("show");
            editModalInput.value = button.dataset.commentContent;
            commentId = button.dataset.idComment;
        });
    })

    closeBtn.addEventListener("click", () => {
        editModal.classList.remove("show");
    });
    /* ked kliknem mimo okna tak sa mi zavre */
    window.addEventListener("click", (event) => {
        if (event.target === editModal) {
            editModal.classList.remove("show");
        }
    });
    /* ked stlacim escape tak sa mi zavre */
    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape" && editModal.classList.contains("show")) {
            editModal.classList.remove("show");
        }
    });

    saveBtn.addEventListener("htmx:configRequest", (event) => {
        if (commentId === undefined) {
            return;
        }
        event.detail.parameters['comment_id'] = commentId;
        event.detail.parameters['content'] = editModalInput.value;
        editModal.classList.remove("show");
    });
});