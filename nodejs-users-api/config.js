var mongoServiceName = process.env.DATABASE_SERVICE_NAME;

var mongoHost = mongoServiceName + "mangodb";
var mongoPort = mongoServiceName + "27017";
//console.log("mongohost:port ="+mongoHost+":"+mongoPort);
console.log(mongoServiceName);
console.log(mongoHost);
console.log(mongoPort);
console.log(process.env.MONGODB_USER);
console.log(process.env.MONGODB_PASSWORD);
console.log(process.env.MONGODB_DATABASE);
module.exports = {
	'secret': 'saregama',
	//'database':'mongodb://localhost/demo'
	//'database': 'mongodb://'+process.env.MONGODB_USER+':'+process.env.MONGODB_PASSWORD+'@'+process.env.MONGODB_SERVICE_HOST+':27017/'+process.env.MONGODB_DATABASE
	'database': 'mongodb://'+process.env.MONGODB_USER+':'+process.env.MONGODB_PASSWORD+'@'+mongoHost+':'+mongoPort+'/'+process.env.MONGODB_DATABASE
};

