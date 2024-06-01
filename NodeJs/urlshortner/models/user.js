const mongoose = require("mongoose")

const user = {
    username: {
        type : String
    },
    email: {
        type : String
    },
    password: {
        type : String,
    }
};

const newuser =
    mongoose.model("User", user);

module.exports  = {newuser}