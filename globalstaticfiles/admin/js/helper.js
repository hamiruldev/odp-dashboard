"use strict";

function getDate() {
  var currentDate = new Date();

  // Get month (0-11, where 0 is January)
  var currentMonth = currentDate.getMonth() + 1; // Adding 1 to make it 1-12

  // Get year (four digits)
  var currentYear = currentDate.getFullYear();

  // Get day of the month (1-31)
  var currentDay = currentDate.getDate();

  return { currentMonth, currentYear, currentDay };
}

function reorderModule() {
  // Extract module elements
  var modules = document.querySelectorAll(".module");

  var desiredSequence = [
    "app-users",
    "app-profiles",
    "app-teams",
    "app-branchs",
    "app-inventory",
    "app-auth",
    "app-token_blacklist",
  ];

  // Reorder modules based on the desired sequence
  var reorderedModules = [];

  desiredSequence.forEach(function (moduleName) {
    var module = Array.from(modules).find(function (m) {
      return m.classList.contains(moduleName);
    });
    if (module) {
      reorderedModules.push(module);
    }
  });

  // Append reordered modules back to the container
  var contentMain = document.getElementById("nav-sidebar");
  contentMain &&
    reorderedModules.forEach(function (module) {
      contentMain.appendChild(module);
    });
}
