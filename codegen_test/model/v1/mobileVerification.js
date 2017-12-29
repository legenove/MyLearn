/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var MobileVerification = function () {
    /*
        @params obj 'data params'
            mobile   'string' 
            code_type   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/mobile/verification",
            method: "POST",
            data: {
                mobile: obj.mobile,
                code_type: obj.code_type
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
    MobileVerification: new MobileVerification
};