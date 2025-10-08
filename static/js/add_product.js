document.addEventListener("DOMContentLoaded", function() {
  const addModal = document.getElementById("addModal");
  const addBtn = document.getElementById("openAddModal");
  const cancelAdd = document.getElementById("cancelAdd");
  const addForm = document.getElementById("addProductForm");
  const addProductUrl = document.getElementById("addProductForm").dataset.url;

  // buka modal
  addBtn.addEventListener("click", () => addModal.classList.remove("hidden"));
  cancelAdd.addEventListener("click", () => addModal.classList.add("hidden"));

  // submit AJAX
  addForm.addEventListener("submit", e => {
    e.preventDefault();
    const formData = new FormData(addForm);
    
    fetch(addProductUrl, {
      method: "POST",
      body: formData,
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        showToast("Success", "Product added successfully!", "success");
        addModal.classList.add("hidden");
        addForm.reset();

        document.dispatchEvent(new CustomEvent('productUpdated'));
      } else {
        showToast("Error", "Failed to add product.", "error");
        console.error(data.errors);
      }
    })
    .catch(err => {
      showToast("Error", "Something went wrong!", "error");
      console.error(err);
    });
  });
});
