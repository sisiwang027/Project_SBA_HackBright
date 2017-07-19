Handlebars.registerHelper("formatFloat", function(data){
      // add function formatFloat to format data.
      
      return data.toFixed(2);
    });

  // Make Line Chart of Melon Sales over time

  function showLineChart(data) {

    $("#lineChartContainer").empty();
    $("#lineChartContainer").append("<canvas id='lineChart'></canvas>");

    var ctx_line = $("#lineChart").get(0).getContext("2d");

    var myLineChart = Chart.Line(ctx_line, data);

    // $("#lineLegend").html(myLineChart.generateLegend());

  }

  function showData (report_json) {
    // show the result of submiting form.
    
    $.get('/static/sale_sum_report.hbs', function (data) {

      // var tableScrip = $("#sale_sum_report").html();
      // var theTemplate = Handlebars.compile(tableScrip);

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

    $.get("/sale_sum.json", formInput, showData);
    $.get("/sale-qty-linechart.json", formInput, showLineChart);
  }

  function getRevenueInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"months": $("#months").val()};

    $.get("/sale-revenue-linechart.json", formInput, showLineChart);
  }

  function getProfitInfo(evt) {
     // get infomation of form 
    // prevent change to some-script, and show the text by alerting.
    evt.preventDefault();

    var formInput = {"months": $("#months").val()};

    $.get("/sale-profit-linechart.json", formInput, showLineChart);
  }


  $("#month-filter").on("submit", getInfo);
  $("#showRevenue").on("click", getRevenueInfo);
  $("#showProfit").on("click", getProfitInfo);

