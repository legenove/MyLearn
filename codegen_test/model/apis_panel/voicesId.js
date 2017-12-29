/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var VoicesId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            status   'string' 
            voice_from   'string' 
            
        @success
            status 200    type:object
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/voices/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status,
                voice_from: obj.voice_from
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
    VoicesId: new VoicesId
};