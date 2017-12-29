/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Push = function () {
    /*
        @params obj 'data params'
            platform   'string' 
            audience   'ref' 
            extras   'ref' 
            message_type   'string' 
            alert   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/push",
            method: "POST",
            data: {
                platform: obj.platform,
                audience: obj.audience,
                extras: obj.extras,
                message_type: obj.message_type,
                alert: obj.alert
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
    Push: new Push
};