var timeoutID;
var timeout = 45000;

function setup() {
    //Sets the button as an event listener on click to call the makePost
	document.getElementById("theButton").addEventListener("click", makePost, true);
	document.getElementById("selection").addEventListener("change", display, true);
	
    //Calls a function after a specified amount of time; called every 45 seconds
	timeoutID = window.setTimeout(poller, timeout);
}

function display(){
    var selection = document.getElementById('selection')
    if (selection[selection.selectedIndex].value =="other"){
        document.getElementById("other").style = "display:block"
    }else{
        document.getElementById("other").style = "display:none"    
    }
} 

function makePost() {
	var httpRequest = new XMLHttpRequest();

	if (!httpRequest) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}
	var first = document.getElementById("first").value
	var last = document.getElementById("last").value
	var flavor = document.getElementById("selection").value
	if (flavor == "other"){
	    flavor = document.getElementById("other").value
	}
	var row = [first, last, flavor]
	httpRequest.onreadystatechange = function() { handlePost(httpRequest, row) };
	
	//posts to the server to add to the dictionary
	httpRequest.open("POST", "/new_item");
	httpRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

	var data;
	data = "first=" + first + "&last=" + last + "&flavor=" + flavor;
	httpRequest.send(data);
}

function handlePost(httpRequest, row) {
    //
	if (httpRequest.readyState === XMLHttpRequest.DONE) {
		if (httpRequest.status === 200) {
			addRow(row);
			clearInput();
		} else {
			alert("There was a problem with the post request.");
		}
	}
}

function poller() {
	var httpRequest = new XMLHttpRequest();

	if (!httpRequest) {
		alert('Giving up :( Cannot create an XMLHTTP instance');
		return false;
	}
    //Defines a function to be called upon state change
	httpRequest.onreadystatechange = function() { handlePoll(httpRequest) };
	httpRequest.open("GET", "/items");
	httpRequest.send();
}

function handlePoll(httpRequest) {
	if (httpRequest.readyState === XMLHttpRequest.DONE) {
		if (httpRequest.status === 200) {
			var tab = document.getElementById("theTable");
			//delete all rows
			while (tab.rows.length > 0) {
				tab.deleteRow(0);
			}
			
			
            /*
            TODO: Remove selection options to later be reentered with new choices
            */
            
			//update the rows accordingly
			var json_response = JSON.parse(httpRequest.responseText);
			var rows = json_response['results']
			
			/*
			    choices holds the json choices sent from the server
			*/
			var choices = json_response['choices']
			
			for (var i = 0; i < rows.length; i++) {
				addRow(rows[i]);
			}
			
			for (var i=0; i<choices.length; i++){
			    addChoice(choices[i]);
			}
				
            /*
            TODO: Implement stats, the computation can happen either in the js or py file.
                your choice
            */
			timeoutID = window.setTimeout(poller, timeout);
			
		} else {
			alert("There was a problem with the poll request.  you'll need to refresh the page to recieve updates again!");
		}
	}
}

function clearInput() {
	document.getElementById("first").value = "";
	document.getElementById("last").value = "";
	document.getElementById("selection").value = "";
	document.getElementById("other").value = ""
	document.getElementById("other").style = "display:none"
}

function addRow(row) {
	var tableRef = document.getElementById("theTable");
	var newRow   = tableRef.insertRow();

	var newCell, newText;
	for (var i = 0; i < row.length; i++) {
		newCell  = newRow.insertCell();
		newText  = document.createTextNode(row[i]);
		newCell.appendChild(newText);
	}
}

function addChoice(choice) {
    /*
    TODO: Implement function to add new choices to the elements to the drop down menu
    */
}
window.addEventListener("load", setup, true);
