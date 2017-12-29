/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Reports = function () {
    /*
        @params obj 'data params'
            reason   'string' 
            target_id   'string' 
            target_type   'string' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/reports",
            method: "POST",
            data: {
                reason: obj.reason,
                target_id: obj.target_id,
                target_type: obj.target_type
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
    Reports: new Reports
};