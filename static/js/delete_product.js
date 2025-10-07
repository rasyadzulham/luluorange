document.addEventListener('DOMContentLoaded', function() {
    let selectedProductId = null;
    let selectedUrl = null;

    const modal = document.getElementById('confirm-modal');
    const confirmBtn = document.getElementById('confirm-delete');
    const cancelBtn = document.getElementById('cancel-delete');

    // Tampilkan modal
    function showModal(productId, url) {
        selectedProductId = productId;
        selectedUrl = url;
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
        modal.querySelector('div').classList.remove('scale-90');
        modal.querySelector('div').classList.add('scale-100');
    }

    // Sembunyikan modal
    function hideModal() {
        modal.classList.add('opacity-0', 'pointer-events-none');
        modal.classList.remove('opacity-100');
        modal.querySelector('div').classList.add('scale-90');
        modal.querySelector('div').classList.remove('scale-100');
    }

    cancelBtn.addEventListener('click', hideModal);

    confirmBtn.addEventListener('click', function() {
        if (!selectedUrl || !selectedProductId) return;

        fetch(selectedUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => response.json())
        .then(data => {
            hideModal();
            if (data.success) {
                const productDiv = document.getElementById(`product-${selectedProductId}`);
                if (productDiv) productDiv.remove();

                showToast(
                    "Product Deleted",
                    data.message || "The product has been deleted successfully.",
                    "success"
                );
            } else {
                showToast(
                    "Failed to Delete",
                    "Could not delete the product. Please try again.",
                    "error"
                );
            }
        })
        .catch(() => {
            hideModal();
            showToast(
                "Error",
                "Something went wrong while deleting the product.",
                "error"
            );
        });
    });

    document.querySelectorAll('.delete-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-id');
            const url = this.getAttribute('href');
            showModal(productId, url);
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
