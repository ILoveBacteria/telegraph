function submitAndLoadingButton(buttonId, formId, text = "Loading...") {
    const element = document.getElementById(buttonId);
    element.setAttribute("disabled", "");
    element.innerHTML = "<span class=\"spinner-border spinner-border-sm\" role=\"status\" aria-hidden=\"true\"></span>" +
        " " + text;
    document.getElementById(formId).submit();
}

function updateCountryCode() {
    const codeElement = document.getElementById("country_code");
    codeElement.innerHTML = document.getElementById("id_country").value;
}
