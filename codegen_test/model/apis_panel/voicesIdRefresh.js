/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var VoicesIdRefresh = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            status   'string' 
            review_status   'string' 
            source   'string' 
            duration   'integer' 
            voice   'string' 
            type   'string' 
            id   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/voices/" + obj.id + "/refresh",
            method: "PUT",
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
    VoicesIdRefresh: new VoicesIdRefresh
};