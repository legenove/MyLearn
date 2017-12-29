/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AlbumsId = function () {
    /*
        @params obj 'data params'
            id   'string' album id in path
            
        @success
            status 200    type:object
            questions_count   'integer' 
            people_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/albums/" + obj.id + "",
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
    AlbumsId: new AlbumsId
};