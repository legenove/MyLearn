/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var RolesId = function () {
    /*
        @params obj 'data params'
            type   'string' 
            name   'string' 
            permission_codes   'array' 
            description   'string' 
            
        @success
            status 200    type:object
            description   'string' 
            date_updated   'string' 
            permission_codes   'array' 
            date_created   'string' 
            type   'string' 
            id   'integer' 
            name   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/roles/<<id>>",
            method: "PUT",
            data: {
                type: obj.type,
                name: obj.name,
                permission_codes: obj.permission_codes,
                description: obj.description
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
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/roles/<<id>>",
            method: "DELETE",
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
    RolesId: new RolesId
};