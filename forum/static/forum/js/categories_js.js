document.addEventListener('DOMContentLoaded', () => {

    let selectedCategory;
    const selectCategoryButtons = document.querySelectorAll('.btn-select-category');
    selectCategoryButtons.forEach((button) => {
        button.addEventListener("click", () => {
            selectedCategory = button.dataset.category;
        });
    });


    const btnMostLikes = document.getElementById("btn-likes");
    const btnNewestFirst = document.getElementById("btn-newest");
    const btnOldestFirst = document.getElementById("btn-oldest");
    btnMostLikes.addEventListener("htmx:configRequest", (event) => {
        if (selectedCategory === undefined) {
            return;
        }
        event.detail.parameters['category'] = selectedCategory;
        event.detail.parameters['sort_by'] = "likes";
    });

    btnNewestFirst.addEventListener("htmx:configRequest", (event) => {
        if (selectedCategory === undefined) {
            return;
        }
        event.detail.parameters['category'] = selectedCategory;
        event.detail.parameters['sort_by'] = "descending_date";
    });

    btnOldestFirst.addEventListener("htmx:configRequest", (event) => {
        if (selectedCategory === undefined) {
            return;
        }
        event.detail.parameters['category'] = selectedCategory;
        event.detail.parameters['sort_by'] = "ascending_date";
    });
});