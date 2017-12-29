/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var WxTemplatesId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:array
            key   'string' 
            value   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/wx/templates/" + obj.id + "",
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            values   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/wx/templates/" + obj.id + "",
            method: "POST",
            data: {
                values: obj.values
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
    WxTemplatesId: new WxTemplatesId
};