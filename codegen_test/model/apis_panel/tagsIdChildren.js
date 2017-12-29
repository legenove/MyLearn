/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TagsIdChildren = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:array
            is_leaf   'boolean' 
            parent_id   'integer' 
            id   'integer' 
            name   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tags/" + obj.id + "/children",
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
            url: "/tags/" + obj.id + "/children",
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
    TagsIdChildren: new TagsIdChildren
};