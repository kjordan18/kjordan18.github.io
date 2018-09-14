// Get references to the tbody element, input field and button
var tbody = document.querySelector("tbody");
var datetimeInput = document.querySelector("#datetime");
var cityInput = document.querySelector("#city");
var stateInput = document.querySelector("#state");
var countryInput = document.querySelector("#country");
var shapeInput = document.querySelector("#shape");
var searchBtn = document.querySelector("#search");
var paginationBtn = document.querySelector("#pagination");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
searchBtn.addEventListener("click", handleSearchButtonClick);
// paginationhBtn.addEventListener("click", handlePaginationButtonClick);

// Set filteredAddresses to addressData initially
var filteredData = dataSet;
// console.log(addressData)

// renderTable renders the filteredAddresses to the tbody
function renderTable() {
  tbody.innerHTML = "";
  for (var i = 0; i < filteredData.length; i++) {
    // Get get the current address object and its fields
    var address = filteredData[i];
    var fields = Object.keys(address);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var row = tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var cell = row.insertCell(j);
      cell.innerText = address[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = datetimeInput.value.trim().toLowerCase();
  var filterCity = cityInput.value.trim().toLowerCase();
  var filterState = stateInput.value.trim().toLowerCase();
  var filterCountry = countryInput.value.trim().toLowerCase();
  var filterShape = shapeInput.value.trim().toLowerCase();

  // Set filteredData to an array of all addresses whose "state" matches the filter
  filteredData = dataSet.filter(function(a) {
    var datetime = a.datetime.toLowerCase();
    var city = a.city.toLowerCase();
    var state = a.state.toLowerCase();
    var country = a.country.toLowerCase();
    var shape = a.shape.toLowerCase();
  // Conditional statements for search bars
    if (filterDatetime && datetime != filterDatetime) {
      return false;
    }

    if (filterCity && city != filterCity) {
      return false;
    }

    if (filterState && state != filterState) {
      return false;
    }

    if (filterCountry && country != filterCountry) {
      return false;
    }

    if (filterShape && shape != filterShape) {
      return false;
    }
    return true;
  });
  console.log(filteredData)
  renderTable();
}



// Render the table for the first time on page load
renderTable();
