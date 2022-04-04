$(document).ready(function() {
    $("#next1").click(function() {
        $("#uploaddiv").hide();
        $("#otpdiv").show();
    });

    $("#next2").click(function() {
        $("#otpdiv").hide();
        $("#ledgerdiv").show();
        console.log("clicked")
    });


});

function showAadhar() {
    $("#pop").show();
}

function hideAadhar() {
    $("#pop").hide();
}