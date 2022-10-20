function submit_and_loading_button(button_id, form_id) {
    const element = document.getElementById(button_id);
    element.setAttribute("disabled", "")
    element.innerHTML = "<span class=\"spinner-border spinner-border-sm\" role=\"status\" aria-hidden=\"true\"></span>" +
        " Loading..."
    document.getElementById(form_id).submit();
}
