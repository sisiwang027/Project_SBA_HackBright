function showAlert (results) {

    alert(results);
    $("#categoryname").val('');
  }

  function getInfo(evt) {
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"cg": $("#categoryname").val()};

    $.post("/add_category", formInput, showAlert);
  }

  $("#addcategory").on("submit", getInfo);