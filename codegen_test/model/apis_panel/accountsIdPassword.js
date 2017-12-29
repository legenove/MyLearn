/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdPassword = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            new_password   'string' 
            password   'string' 
            
        @success
            status 200    type:object
            ok   'boolean' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "/password",
            method: "PUT",
            data: {
                new_password: obj.new_password,
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
    AccountsIdPassword: new AccountsIdPassword
};