const BarnowlHci = require('barnowl-hci');

let barnowl = new BarnowlHci();

barnowl.addListener(BarnowlHci.SocketListener, {});


setTimeout(function() {
	barnowl.on("raddec", function(raddec) {
	  console.log(raddec);
	});

	barnowl.on("infrastructureMessage", function(message) {
	  console.log(message);
	});
}, 3000);