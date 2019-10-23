var base_url = "http://127.0.0.1:8000/"

function all_good_no_redirect(headertext,maintext) {
    return Swal.fire(headertext, maintext, "success")
}

function not_all_good_no_redirect(headertext,maintext) {
    return Swal.fire(headertext, maintext, "error")
}

function all_good(headertext, maintext, nexturl) {
    return Swal.fire({
        title: headertext,
        text: maintext,
        type: "success"}).then(function(){
            window.location = base_url + nexturl;
        });
}

function not_all_good(headertext, maintext, nexturl) {
    return Swal.fire({
        title: headertext,
        text: maintext,
        type: "error"}).then(function(){
            window.location = base_url + nexturl;
        });
}

function profile_form_validation_response() {
    if (document.ProfileForm.alert.value==1){       
        all_good2("All Good", "Your profile update has been saved", "home/")
    }
    if (document.ProfileForm.alert.value==0){
        not_all_good("Oops!", "There was a problem with your profile update.", "home/")
    }
}

function edit_template_form_validation_response() {
    if (document.EditQuoteTemplateForm.alert.value==1){       
        all_good("All Good", "Your template update has been saved", "home/")
    }
    if (document.EditQuoteTemplateForm.alert.value==0){
        not_all_good("Oops!", "There was a problem with your template update.", "home/")
    }
}
