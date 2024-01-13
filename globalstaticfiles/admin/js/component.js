"use strict";
// var title = `{{ title }}`
// console.log("title", title)

// URL to fetch data from
var BackEndPath = 'http://127.0.0.1:8000'
var apiUrlBranch = `${BackEndPath}/api/v1/branch/api/branch/?page=1`;
var apiUrlProfile = `${BackEndPath}/api/v1/profile/`;
var apiUrlInventory = `${BackEndPath}/api/v1/inventory/`;

async function loadAgentData(args) {
  // console.log("args", args.progressBar.labelStyle.text);
  const dataAPi = await fetchDataAsync(apiUrlProfile, "profile");

  args.progressBar.value = 50;
  args.progressBar.labelStyle.text = "50%";

  // args.progressBar.refresh();
}

var linechartObj = new ej.charts.Chart({
  // width: "400",
  height: "300",
  // title: "Monthly Sales",

  //Initializing Primary X Axis
  primaryYAxis: {
    minimum: 0,
    maximum: 100,
    majorTickLines: { width: 0 },
    labelFormat: "{value}%",
    lineStyle: { width: 0 },
    labelStyle: { size: "11px" },
    titleStyle: { size: "13px" },
  },
  //Initializing Primary X Axis
  primaryXAxis: {
    valueType: "Category",
    majorGridLines: { width: 0 },
    labelStyle: { size: "11px" },
  },

  tooltip: {
    enable: true,
  },
  legendSettings: {
    visible: false,
    padding: 5,
    shapeHeight: 8,
    shapeWidth: 8,
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
  series: [
    {
      dataSource: [
        { Period: "2017", Percentage: 60 },
        { Period: "2018", Percentage: 56 },
        { Period: "2019", Percentage: 71 },
        { Period: "2020", Percentage: 85 },
        { Period: "2021", Percentage: 73 },
      ],
      type: "Column",
      name: "Online",
      xName: "Period",
      yName: "Percentage",
      fill: "#2485FA",
      marker: {
        dataLabel: {
          visible: true,
          position: "Middle",
          font: { color: "white" },
        },
      },
    },
  ],
});

var pie = new ej.charts.AccumulationChart({
  //Initializing Series
  height: "300",

  series: [
    {
      dataSource: ej.base.Browser.isDevice
        ? [
            { x: "Chrome", y: 59.28, text: "59.28%" },
            { x: "Safari", y: 4.73, text: "4.73%" },
            { x: "Opera", y: 6.12, text: "6.12%" },
            { x: "Edge", y: 7.48, text: "7.48%" },
            { x: "Others", y: 22.39, text: "22.39%" },
          ]
        : [
            { x: "Chrome", y: 59.28, text: "59.28%" },
            { x: "UC Browser", y: 4.37, text: "4.37%" },
            { x: "Opera", y: 3.12, text: "3.12%" },
            { x: "Sogou Explorer", y: 1.73, text: "1.73%" },
            { x: "QQ", y: 3.96, text: "3.96%" },
            { x: "Safari", y: 4.73, text: "4.73%" },
            { x: "Internet Explorer", y: 6.12, text: "6.12%" },
            { x: "Edge", y: 7.48, text: "7.48%" },
            { x: "Others", y: 9.57, text: "9.57%" },
          ],
      dataLabel: {
        visible: true,
        position: "Outside",
        name: "text",
        font: { fontWeight: "600" },
        connectorStyle: { length: "20px", type: "Curve" },
      },
      radius: ej.base.Browser.isDevice ? "40%" : "70%",
      xName: "x",
      yName: "y",
      startAngle: ej.base.Browser.isDevice ? 55 : 35,
      explode: true,
      explodeOffset: "10%",
      explodeIndex: 0,
      name: "Browser",
    },
  ],
  center: { x: "50%", y: "50%" },
  enableSmartLabels: true,
  enableBorderOnMouseMove: false,
  enableAnimation: false,
  legendSettings: {
    visible: true,
    position: "Bottom",
  },
  //Initializing Tooltip
  tooltip: {
    enable: true,
    format: "<b>${point.x}</b><br>Browser Share: <b>${point.y}%</b>",
    header: "",
  },
  //Initializing Title
  // title: "Browser Market Share",
});

const ProgressBar1 = new ej.progressbar.ProgressBar({
  type: "Linear",
  height: "30",
  width: "100%",
  showProgressValue: true,
  value: 0,
  trackThickness: 20,
  progressThickness: 20,
  labelStyle: {
    textAlignment: "Center",
    color: "#ffffff",
  },
  role: "Success",
  // load: progressLoad,
  animation: {
    enable: true,
    duration: 2000,
    delay: 0,
  },
});

const ProgressBar2 = new ej.progressbar.ProgressBar({
  type: "Linear",
  height: "30",
  width: "100%",
  showProgressValue: true,
  value: 0,
  trackThickness: 20,
  progressThickness: 20,
  labelStyle: {
    textAlignment: "Center",
    color: "#ffffff",
  },
  role: "Success",
  // load: progressLoad,
  animation: {
    enable: true,
    duration: 2000,
    delay: 0,
  },
});

const ProgressBar3 = new ej.progressbar.ProgressBar({
  type: "Linear",
  height: "30",
  width: "100%",
  showProgressValue: true,
  value: 0,
  trackThickness: 20,
  progressThickness: 20,
  labelStyle: {
    textAlignment: "Center",
    color: "#ffffff",
  },
  role: "Success",
  // load: progressLoad,
  animation: {
    enable: true,
    duration: 2000,
    delay: 0,
  },
});

const ProgressBar4 = new ej.progressbar.ProgressBar({
  type: "Linear",
  height: "30",
  width: "100%",
  showProgressValue: true,
  value: 0,
  trackThickness: 20,
  progressThickness: 20,
  load: loadAgentData,
  textRender: (args) => {
    console.log("args textRender--->", args);
    // Here you can customize the code.
  },
  valueChanged: (args) => {
    // Here you can customize the code.
    console.log("args valueChanged--->", args);
  },
  labelStyle: {
    textAlignment: "Center",
    color: "#ffffff",
    // text: "40% Complete (Success)",
  },
  role: "Success",
  animation: {
    enable: true,
    duration: 2000,
    delay: 0,
  },
});

linechartObj.appendTo("#myChart");
pie.appendTo("#myPieChart");

// ProgressBar1.appendTo("#ListingProgressBar");
// ProgressBar2.appendTo("#CustomerProgressBar");
// ProgressBar3.appendTo("#BranchProgressBar");
// ProgressBar4.appendTo("#AgentProgressBar");

if(window.location.pathname == '/admin/'){
  fetchDataAsync(apiUrlBranch, "branch");
  fetchDataAsync(apiUrlProfile, "profile");
  fetchDataAsync(apiUrlInventory, "customer");
  fetchDataAsync(apiUrlInventory, "inventory");
}


