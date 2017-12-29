/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ReviewsAccountsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            nickname   'ref' 
            is_black   'boolean' 
            id   'ref' 
            is_verified   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/reviews/accounts/" + obj.id + "",
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
    ReviewsAccountsId: new ReviewsAccountsId
};