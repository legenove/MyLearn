/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Tenants = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            mobile   'string' 
            privileges   'array' 
            date_created   'string' 
            id   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants",
            method: "GET",
            data: {
                account_id: obj.account_id,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
            comment   'string' 
            mobile   'string' 
            privileges   'array' 
            password   'string' 
            account_id   'integer' 
            
        @success
            status 201    type:object
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            mobile   'string' 
            privileges   'array' 
            date_created   'string' 
            id   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants",
            method: "POST",
            data: {
                comment: obj.comment,
                mobile: obj.mobile,
                privileges: obj.privileges,
                password: obj.password,
                account_id: obj.account_id
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
    Tenants: new Tenants
};