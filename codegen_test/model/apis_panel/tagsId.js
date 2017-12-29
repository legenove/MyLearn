/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TagsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            is_leaf   'boolean' 
            name   'string' 
            parent_id   'integer' 
            date_created   'string' 
            path   'array' 
            id   'integer' 
            icon   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags/" + obj.id + "",
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
            id   'integer' int id in query
            name   'string' 
            icon   'string' 
            
        @success
            status 200    type:object
            is_leaf   'boolean' 
            name   'string' 
            parent_id   'integer' 
            date_created   'string' 
            path   'array' 
            id   'integer' 
            icon   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags/" + obj.id + "",
            method: "PUT",
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
    
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 204    type:object
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags/" + obj.id + "",
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
    TagsId: new TagsId
};