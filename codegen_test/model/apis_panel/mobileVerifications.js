/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var MobileVerifications = function () {
    /*
        @params obj 'data params'
            mobile   'string' mobile in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            verification_code   'string' 
            date_expired   'integer' 
            mobile   'string' 
            is_used   'boolean' 
            date_created   'integer' 
            verify_count   'integer' 
            id   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/mobile/verifications",
            method: "GET",
            data: {
                mobile: obj.mobile,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
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
    MobileVerifications: new MobileVerifications
};