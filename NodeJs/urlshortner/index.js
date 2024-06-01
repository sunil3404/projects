const express = require("express")
const mongoose = require("mongoose")
const bodyParser = require("body-parser")
const user = require("./models/user")
const app = express()


app.use(express.json());
app.use(bodyParser.urlencoded({
    extended: true
}));


mcClient = mongoose.connect("mongodb://172.17.0.1:27017/urlshortner" )
							.then(console.log("Connected to MongoDb"))
 
app.listen('3000', (req, res) => {
	console.log("App listening on port 3000")

})

app.post("/user", (req, res) => {

		const myuser = new user.newuser({
            username: req.body.username,
            email : req.body.email,
            password : req.body.password
        });

        myuser.save(function (err) {
            if (err) {
                throw err;
            } else {
            	console.log("Success");
                res.send("Success");
            }
        });

})
