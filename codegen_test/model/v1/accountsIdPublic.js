/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdPublic = function () {
    /*
        @params obj 'data params'
            id   'integer' account id in path
            
        @success
            status 200    type:object
            introduction   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/" + obj.id + "/public",
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
    AccountsIdPublic: new AccountsIdPublic
};