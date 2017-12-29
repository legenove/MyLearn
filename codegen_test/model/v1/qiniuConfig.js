/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QiniuConfig = function () {
    /*
        @params obj 'data params'
            bucket   'string' bucket in query
            
        @success
            status 200    type:object
            token   'string' 
            upload_url   'string' 
            domain   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/qiniu/config",
            method: "GET",
            data: {
                bucket: obj.bucket
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
    QiniuConfig: new QiniuConfig
};