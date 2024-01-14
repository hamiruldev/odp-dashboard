"use strict";
// var title = `{{ title }}`
// console.log("title", title)

function fetchData(apiUrl) {
  return axios
    .get(apiUrl)
    .then((response) => {
      // Process the data as needed
      return response;
    })
    .catch((error) => {
      // Handle errors
      console.error("Error fetching data:", error);
      return error;
    });
}

async function fetchDataAsync(apiUrl, site) {
  try {
    const results = await fetchData(apiUrl);

    if (site == "branch") {
      const { data } = results;


      // console.log("data---->" , data)

      document.querySelector(".branchText").textContent = data.count;

      // document.querySelector(
      //   "#BranchProgressBar"
      // )?.ej2_instances[0].labelStyle.text == "masuk";

      // .text = `${
      //   data.count / 100
      // }% Complete (Success)`;

    //  document.querySelector("#BranchProgressBar").ej2_instances[0].value = data.count * 100;

      // document.querySelector("#BranchProgressBar").ej2_instances[0].refesh();
    }

    if (site == "profile") {
      const { data } = results;

      document.querySelector(".agentText").textContent = data.length;

      // document.querySelector("#AgentProgressBar").ej2_instances[0].value = 50;

      // document.querySelector(
      //   "#AgentProgressBar"
      // ).ej2_instances[0].labelStyle.text = `% Complete (Success)`;

      // document.querySelector("#AgentProgressBar").ej2_instances[0].refesh();

      return data.length;
    }

    if (site == "inventory") {
      const { data } = results;
      document.querySelector(".InventoryText").textContent = data.count;

      // document.querySelector(
      //   "#ListingProgressBar"
      // ).ej2_instances[0].labelStyle.text == `${
      //   data.count / 100
      // }% Complete (Success)`;
      
      // document.querySelector("#ListingProgressBar").ej2_instances[0].value = 70;
      // document.querySelector("#ListingProgressBar").ej2_instances[0].refesh();
    }

    if (site == "customer") {
      const { data } = results;
      document.querySelector(".customerText").textContent = data.count;

      // document.querySelector(
      //   "#CustomerProgressBar"
      // ).ej2_instances[0].labelStyle.text = `${
      //   data.count / 100
      // }% Complete (Success)`;

      // document.querySelector(
      //   "#CustomerProgressBar"
      // ).ej2_instances[0].value = 70;

    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}
