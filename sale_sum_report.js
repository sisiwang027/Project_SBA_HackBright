"use strict";

Handlebars.registerHelper("formatFloat", function(data){
      // add function formatFloat to format data.
      
      return data.toFixed(2);
    });

  // Make Line Chart of Melon Sales over time
  var ctx_line = $("#lineChart").get(0).getContext("2d");

  var options = {
      responsive: true
    };

function showQtyChart(data) {

     var myLineChart = Chart.Line(ctx_line, {
                                    data: data,
                                    options: options
                                });
    $("#lineLegend").html(myLineChart.generateLegend());

  }

  function showData (report_json) {
    // show the result of submiting form.
    
    var tableScrip = $("#sale_sum_report").html();
    var theTemplate = Handlebars.compile(tableScrip);

    var context = report_json;

    var theCompiledHtml = theTemplate(context);

    $("#handlebars-table").html(theCompiledHtml);

  }


  function getInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"months": $("#months").val()};

    $.get("/sale_sum.json", formInput, showData);
    $.get("/sale-qty-linechart.json", formInput, showQtyChart);
  }


  $("#month-filter").on("submit", getInfo);