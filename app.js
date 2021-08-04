function predict_price(){
	url = 'http://127.0.0.1:5000/predict_price';
	var http = new XMLHttpRequest();
	var one = document.getElementById('location').value;
	var two = document.getElementById('area').value;
	var three = document.getElementById('bath').value;
	var four = document.getElementById('bhk').value;
	params = '1='+one+'&2='+two+'&3='+three+'&4='+four;
	http.open('POST', url, true);
	http.setRequestHeader('Content-type','application/x-www-form-urlencoded');
	http.onreadystatechange = function(){
    if(http.readyState ==4 && http.status == 200){
        data = http.responseText;

    var obj = JSON.parse(data);
    var res = [];
    for(var i in obj)
    	res.push(obj[i]);
    document.getElementById('output').innerHTML = "The property is avaibable for Rs "+res+" Lakhs only";
        
    }
	}
http.send(params);
};


function httpGet(url, callback){
	const request = new XMLHttpRequest();
	request.open('GET', url, true);
	request.onload = function(){
		callback(request);
	}
	request.send();
}

function onload(){
	httpGet('http://127.0.0.1:5000/get_location', function(request){
		data = request.responseText;

	var obj = JSON.parse(data);
	var res = [];
	for (var i in obj)
		res.push(obj[i]);

	for (let i=0; i<res[0].length; i++){
		var x = document.getElementById("location");
		var option = document.createElement('option');
		option.text = res[0][i];
		x.add(option);
	}

	})
};