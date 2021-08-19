$(document).ready(function () {
    $("#submit").on('click', function () {
        $.ajax({
            url: '/predict',
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
                "url": $("#searchTxt").val()
            }),
            cache: 'false',
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
                console.log("error");
            }
        })
            .done(function (data) {
                let title = "";
                let text = "";
                let icon = "error";

                if (!data.success) {
                    title = "Cannot connect to url"
                    icon = "error";
                } else {
                    title = data.predictions[0].result;
                    text = `Score: ${data.predictions[0]["phishing percentage"]}`;
                    if (data.predictions[0].result === "URL is probably phishing") {
                        title = data.predictions[0].result;
                        icon = "error";
                    } else {
                        icon = "success";
                    }
                }
                swal({
                    title: title,
                    text: text,
                    icon: icon
                });
            });
        event.preventDefault();
    });
});


$(document).ready(function () {
    $("#feedback").on('click', function () {
        $('#reportModal').modal('hide');
        $.ajax({
            type: "POST",
            url: '/feedback',
            data: {
                title: document.getElementById("slct").value,
                content: document.getElementById("comment_text").value
            },
            success: function (data) {
                console.log('success');
                swal({
                    title: "Send Feedback success",
                    text: "Thanks for your feedback",
                    icon: "success",
                });
            },
            error: function (data) {
                console.log("error");
            }
        })
    });
});