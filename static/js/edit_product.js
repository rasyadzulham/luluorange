document.addEventListener("DOMContentLoaded", function() {
  const modal = document.getElementById("editModal");
  const form = document.getElementById("editProductForm");
  const cancelBtn = document.getElementById("cancelEdit");

  // Open modal and load product data
  document.querySelectorAll(".edit-btn").forEach(btn => {
    btn.addEventListener("click", function(e) {
      e.preventDefault();
      const id = this.dataset.id;
      fetch(`/product/${id}/update/`)
        .then(res => res.json())
        .then(data => {
          document.getElementById("productId").value = id;
          document.getElementById("productName").value = data.name;
          document.getElementById("productCategory").value = data.category;
          document.getElementById("productPrice").value = data.price;
          document.getElementById("productDescription").value = data.description;
          document.getElementById("productThumbnail").value = data.thumbnail || "";
          document.getElementById("productFeatured").checked = data.is_featured;
          document.getElementById("productRating").value = data.rating || 0;
          modal.classList.remove("hidden");
        });
    });
  });

  // Cancel button
  cancelBtn.addEventListener("click", () => {
    modal.classList.add("hidden");
  });

  // Submit edit form via AJAX
  form.addEventListener("submit", function(e) {
    e.preventDefault();
    const id = document.getElementById("productId").value;
    const formData = new FormData(form);
    
    fetch(`/product/${id}/update/`, {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
      }
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        showToast("Success", "Product updated successfully!", "success");
        modal.classList.add("hidden");

        const card = document.getElementById(`product-${id}`);
        if (card) {
          // Update name, price, rating
          card.querySelector('.product-name').textContent = data.product.name;
          card.querySelector('.product-price').textContent = `IDR ${data.product.price}`;
          card.querySelector('.product-rating').textContent = `⭐️ ${data.product.rating}`;

          // Update thumbnail
          const thumb = card.querySelector('.product-thumbnail');
          if (thumb && data.product.thumbnail) {
            thumb.src = data.product.thumbnail;
          }

          // Update category badge
          const categoryBadge = card.querySelector('.category-badge');
          if (categoryBadge) {
            categoryBadge.textContent = data.product.category_display || data.product.category;
          }

          const lovedBadge = card.querySelector('.product-is_recommended');
            const ratingValue = parseFloat(data.product.rating);

            if (ratingValue >= 4.5) {
            if (!lovedBadge) {
                const badgeContainer = card.querySelector('.absolute.top-3.right-3.flex');
                const newBadge = document.createElement('span');
                newBadge.className = "inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-red-100 text-red-800 product-is_recommended";
                newBadge.textContent = "Loved by everyone!";
                badgeContainer.appendChild(newBadge);
            }
            } else {
            if (lovedBadge) lovedBadge.remove();
            }

          // Update featured badge
          const featuredBadge = card.querySelector('.product-is_featured');
          if (data.product.is_featured) {
            if (!featuredBadge) {
              const badgeContainer = card.querySelector('.absolute.top-3.right-3.flex');
              const newBadge = document.createElement('span');
              newBadge.className = "inline-flex items-center px-2 py-1 rounded text-xs font-medium bg-yellow-100 text-yellow-800 product-is_featured";
              newBadge.textContent = "Featured";
              badgeContainer.appendChild(newBadge);
            }
          } else {
            if (featuredBadge) featuredBadge.remove();
          }
        }
      } else {
            showToast("Error", "Failed to update product.", "error");
            console.error("Validation errors:", data.errors);
        
      }
    });
  });
});