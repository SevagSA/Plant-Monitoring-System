const BarnowlHci = require('barnowl-hci'); // 1: Include the interface package

let barnowl = new BarnowlHci();

setTimeout(()=>{
process.exit();
},3000);


barnowl.addListener(BarnowlHci.SocketListener, {});

barnowl.on("raddec", function(raddec) {
  console.log(raddec);
});

barnowl.on("infrastructureMessage", function(message) {
  console.log(message);
});