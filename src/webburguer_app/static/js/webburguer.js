function closeModal(id) {

    const modal = document.getElementById("id" + id);

    modal.classList.remove('show');
    modal.setAttribute('aria-hidden', 'true');
    modal.setAttribute('style', 'display: none');

    const modalBackdrops = document.getElementsByClassName('modal-backdrop');

    document.body.removeChild(modalBackdrops[0]);
}