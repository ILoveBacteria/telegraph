function submitAndLoadingButton(buttonId, formId, text = "Loading...") {
    const element = document.getElementById(buttonId);
    element.setAttribute("disabled", "");
    element.innerHTML = "<span class=\"spinner-border spinner-border-sm\" role=\"status\" aria-hidden=\"true\"></span>" +
        " " + text;
    document.getElementById(formId).submit();
}

function updateCountryCode() {
    const codeElement = document.getElementById("country_code");
    const value = document.getElementById("id_country").value;
    const phoneField = document.getElementById("id_phone");
    codeElement.innerHTML = value;
    if (value === "---") {
        phoneField.setAttribute("disabled", "");
    } else {
        phoneField.removeAttribute("disabled");
    }
}
