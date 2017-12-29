/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var VerifyTags = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:array
            id   'integer' 
            qualification_type   'string' 
            all_children   'array' 
            name   'string' 
            icon   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/verify/tags",
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
    VerifyTags: new VerifyTags
};