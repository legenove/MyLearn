/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TenantsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
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
            url: "/tenants/" + obj.id + "",
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            comment   'string' 
            mobile   'string' 
            privileges   'array' 
            password   'string' 
            
        @success
            status 200    type:object
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            mobile   'string' 
            privileges   'array' 
            date_created   'string' 
            id   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants/" + obj.id + "",
            method: "PUT",
            data: {
                comment: obj.comment,
                mobile: obj.mobile,
                privileges: obj.privileges,
                password: obj.password
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
    TenantsId: new TenantsId
};