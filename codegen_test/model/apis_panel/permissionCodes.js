/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PermissionCodes = function () {
    /*
        @params obj 'data params'
            type   'string' permission code type in query
            
        @success
            status 200    type:array
            name   'string' 
            key   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/permission_codes",
            method: "GET",
            data: {
                type: obj.type
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
    PermissionCodes: new PermissionCodes
};