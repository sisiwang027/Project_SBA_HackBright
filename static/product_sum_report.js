Handlebars.registerHelper("formatFloat", function(data){
      // add function formatFloat to format data.   
      return data.toFixed(2);
    });

  // Make Line Chart of Melon Sales over time

  function showChart(data) {

    $("#ChartContainer").empty();
    $("#ChartContainer").append("<canvas id='dataChart'></canvas>");

    var ctx_chart = $("#dataChart").get(0).getContext("2d");

    var myChart = new Chart(ctx_chart, data);

  }

  
  function showData (report_json) {
    // show the result of submiting form.

    $.get('/static/product_sum_report.hbs', function (data) {

      var theTemplate = Handlebars.compile(data);

      var context = report_json;

      var theCompiledHtml = theTemplate(context);

      $("#handlebars-table").html(theCompiledHtml);

    }, 'html');
  }


  function getInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"months": $("#months").val()};

    $.get("/product_sum.json", formInput, showData);
    $.get("/prod_pichart.json", formInput, showChart);
  }


  function getTopInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"months": $("#months").val()};

    $.get("/top_prod_barchart.json", formInput, showChart);
  }


  $("#month-filter").on("submit", getInfo);
  $("#showTop").on("click", getTopInfo);