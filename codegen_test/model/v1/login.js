/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Login = function () {
    /*
        @params obj 'data params'
            username   'string' 
            password   'string' 
            
        @success
            status 200    type:object
            title   'ref' 
            is_verified   'boolean' 
            price   'integer' 
            avatar   'ref' 
            nickname   'string' 
            id   'ref' 
            answers_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/login",
            method: "POST",
            data: {
                username: obj.username,
                password: obj.password
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Login: new Login
};