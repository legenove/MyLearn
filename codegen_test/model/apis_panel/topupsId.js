/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TopupsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            status   'string' 
            
        @success
            status 200    type:object
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topups/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status
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
    TopupsId: new TopupsId
};