/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdQualification = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            status   'string' 
            account   'ref' 
            account_id   'ref' 
            title   'string' 
            reasons   'string' 
            explain   'string' 
            tag_id   'ref' 
            name   'string' 
            tag_name   'string' 
            images   'array' 
            type   'string' 
            id   'ref' 
            additional   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "/qualification",
            method: "GET",
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
    AccountsIdQualification: new AccountsIdQualification
};