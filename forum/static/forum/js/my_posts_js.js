document.addEventListener('DOMContentLoaded', () => {

    const editModal = document.getElementById("id-edit-modal");
    const closeBtn = document.getElementById("id-btn-close-modal");
    const editModalInput = document.getElementById("id-edit-modal-input");
    const saveBtn = document.getElementById("id-btn-save-edit-modal");
    let postId;
    function attachButtonListeners() {
        const editButtons = document.querySelectorAll('.my-post-edit-btn');
        editButtons.forEach((button) => {
            button.addEventListener("click", () => {
                editModal.classList.add("show");
                editModalInput.value = button.dataset.postContent;
                postId = button.dataset.idPost;
            });
        });
    }
    attachButtonListeners();
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
        if (postId === undefined) {
            return;
        }
        event.detail.parameters['post_id'] = postId;
        event.detail.parameters['content'] = editModalInput.value;
        console.log(postId);
        editModal.classList.remove("show");
    });

    htmx.on('#my-posts-list', 'htmx:afterSwap', () => {
        attachButtonListeners();
    });
});