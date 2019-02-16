function checkLicenseNumber() {
    if ($("#license_number").val() === "") {
        $("#license_number_error").removeClass('hide');
        $("#license_number_error").text("Please Enter Valid License Number");
    }
    else {
        $("#license_number_error").addClass('hide');

        var data = {
            "license_number": $("#license_number").val(),
            "action": "getLicenseNumber"
        };

        var settings = {
            "method": "GET",
            "url": "/checkLicenseNumber/",
            "data": data,

            "success": function (data) {
                if (data["registered"] === true) {
                    $("#license_number_error").removeClass('hide');
                    $("#license_number_error").text("Please Enter Valid License Number, as it is already registered with us.");
                }
                else {
                    $('#confirmationModal').modal();
                }
            }
        };
        $.ajax(settings);

    }
}
