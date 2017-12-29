/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var MobileVerified = function () {
    /*
        @params obj 'data params'
            mobile   'string' 
            verification_code   'string' 
            client   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/mobile/verified",
            method: "POST",
            data: {
                mobile: obj.mobile,
                verification_code: obj.verification_code,
                client: obj.client
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
    MobileVerified: new MobileVerified
};