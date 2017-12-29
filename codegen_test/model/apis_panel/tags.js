/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Tags = function () {
    /*
        @params obj 'data params'
            is_root   'boolean' 
            name   'string' 
            
        @success
            status 200    type:array
            ancestors   'array' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags",
            method: "GET",
            data: {
                is_root: obj.is_root,
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
    
    /*
        @params obj 'data params'
            name   'string' 
            icon   'string' 
            
        @success
            status 201    type:object
            is_leaf   'boolean' 
            name   'string' 
            parent_id   'integer' 
            date_created   'string' 
            path   'array' 
            id   'integer' 
            icon   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags",
            method: "POST",
            data: {
                name: obj.name,
                icon: obj.icon
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
    Tags: new Tags
};