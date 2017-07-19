var numAttr = 1;

  function addOneAttr(evt) {
    // add one attribute name and value input box
    evt.preventDefault();

    numAttr++;

    var attrName = "Attribute Name : <input type='text' name='attrname" + numAttr + "' id='attrname" + numAttr +"' >";

    var attrVal = "Attribute Value : <input type='text' name='attrvalue" + numAttr + "' id='attrvalue" + numAttr +"' >";

    var attrRemove = "<a href='#'" + " id='removeAttr" + numAttr + "' removeattrid=" + numAttr + " class='remove-btn'>Remove</a>";

    // <button id='removeAttr1' removeAttr-id='1' class='remove-btn'>Remove</button>

    // var attrRemove = "<button id='removeAttr" + numAttr + " removeattrid=" + numAttr + " class='remove-btn'>Remove</button>";
    
    $('#attr-add').append("<div class='input_attrs' id='attr" + numAttr + "'>" + attrName + attrVal + attrRemove +"</div>");

    console.log(numAttr);
            
  }

  // function removeOneAttr(env) {
//     // remove one attribute name and value input box

//     numAttr--;

//     $('#input_attrs_field').parent('div').remove();

//     console.log(numAttr);

//   }

  function removeOneAttr(evt) {

            var attrId = $(this).attr('removeattrid');
            console.log(attrId);

            $('#attr' + attrId ).remove();
        }


  function showAlert (results) {
    // show the result of submiting form.

    alert(results);
    $("#productname").val('');
    
    $("#saleprice").val('');
    $("#description").val('');
    $("#attrname1").val('');
    $("#attrvalue1").val('');
    $("#attr-add").remove();

  }

  function getInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"cg": $("#category").val(), "pname": $("#productname").val(), "sprice": $("#saleprice").val(),
                     "pdescription": $("#description").val(), "attrname1": $("#attrname1").val(),  "attrvalue1": $("#attrvalue1").val(), "attr_num": numAttr};

    for (var i = 2; i <= numAttr; i++) {
      //add all attribute to dictionary forInput
      attrname = "attrname" + String(i);
      attrvalue ="attrvalue" + String(i);
      formInput[attrname] = $("#" + attrname).val();
      formInput[attrvalue] = $("#" + attrvalue).val();

    }

    $.post("/add_product", formInput, showAlert);
  }


  $("#addproduct").on("submit", getInfo);
  $('#addOneAttr').on('click', addOneAttr);
  $('#input_attrs_field').on('click', '.remove-btn', removeOneAttr);


