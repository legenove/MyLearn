/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AdminsId = function () {
    /*
        @params obj 'data params'
            role_ids   'array' 
            
        @success
            status 200    type:object
            role_ids   'array' 
            nickname   'string' 
            id   'integer' 
            avatar   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/admins/<<id>>",
            method: "PUT",
            data: {
                role_ids: obj.role_ids
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
            url: "/admins/<<id>>",
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
    AdminsId: new AdminsId
};