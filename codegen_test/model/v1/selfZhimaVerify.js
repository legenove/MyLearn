/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfZhimaVerify = function () {
    /*
        @params obj 'data params'
            params   'string' 芝麻回调参数
            sign   'string' 芝麻回调签名
            
        @success
            status 200    type:object
            real_name_flag   'boolean' 
            certify_result   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/zhima_verify",
            method: "GET",
            data: {
                params: obj.params,
                sign: obj.sign
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
    
    /*
        @params obj 'data params'
            cert_no   'string' 
            name   'string' 
            
        @success
            status 201    type:object
            url   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/zhima_verify",
            method: "POST",
            data: {
                cert_no: obj.cert_no,
                name: obj.name
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
    SelfZhimaVerify: new SelfZhimaVerify
};