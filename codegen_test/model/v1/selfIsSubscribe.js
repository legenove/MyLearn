/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfIsSubscribe = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            is_subscribe   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/is_subscribe",
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
    SelfIsSubscribe: new SelfIsSubscribe
};